# Import necessary libraries
import scanpy as sc
import pandas as pd
import seaborn as sns
import scanpy.external as sce
import scanorama
import numpy as np

# Set Scanpy settings and display versions
sc.settings.verbosity = 1  # verbosity: errors (0), warnings (1), info (2), hints (3)
sc.logging.print_versions()
sc.settings.set_figure_params(dpi=80, frameon=False, figsize=(3, 3), facecolor='white')

# Load the CS13 Aorta dataset
adata = sc.read("CS13_Aorta.h5ad")

# Remove contaminating hemoglobin genes
adata = adata.raw.to_adata()
non_HB = [name for name in adata.var_names if not name.startswith('HB')]
adataH = adata[:, non_HB]
adata = adataH
adata.raw = adata

# Plot UMAP after removing hemoglobin genes
sc.pl.umap(adata, color=['leiden', 'HBA1'])

# Load additional datasets
ddata = sc.read("Bing_CS13_Ao.h5ad")
edata = sc.read("Bing_CS14.h5ad")
fdata = sc.read("Bing_CS152.h5ad")
ddata.raw = ddata
edata.raw = edata
fdata.raw = fdata

# Identify highly variable genes for each dataset
sc.pp.highly_variable_genes(adata)
sc.pp.highly_variable_genes(ddata)
sc.pp.highly_variable_genes(edata)
sc.pp.highly_variable_genes(fdata)

# Filter datasets based on the identified highly variable genes
adata = adata[:, adata.var['highly_variable']]
ddata = ddata[:, ddata.var['highly_variable']]
edata = edata[:, edata.var['highly_variable']]
fdata = fdata[:, fdata.var['highly_variable']]

# List of datasets
adatas = [adata, ddata, edata, fdata]

# Integrate and correct datasets using Scanorama
scanorama.integrate_scanpy(adatas, dimred=50)
scanorama.correct_scanpy(adatas, dimred=50)

# Combine integrated matrices from Scanorama
scanorama_int = [ad.obsm['X_scanorama'] for ad in adatas]
all_s = np.concatenate(scanorama_int)
print(all_s.shape)

# Concatenate datasets into a single AnnData object
adata_concat = adata.concatenate(ddata, edata, fdata, batch_categories=['CS13', 'Bing_CS13', 'Bing_CS14', 'Bing_CS15'])
adata_concat.obsm["Scanorama"] = all_s

# Compute neighbors and UMAP based on the Scanorama integrated data
sc.pp.neighbors(adata_concat, n_pcs=10, use_rep="Scanorama")
sc.tl.umap(adata_concat)
sc.pl.umap(adata_concat, color='batch')

# Perform leiden clustering on the concatenated data
sc.tl.leiden(adata_concat)

# Plot UMAP with ket markers
sc.pl.umap(adata_concat, color=['batch', 'leiden', 'CDH5', 'APLNR', 'GJA5', 'PTPRC', 'RUNX1', 'MYB'], ncols=2)
