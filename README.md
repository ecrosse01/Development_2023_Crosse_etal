# Molecular Signalling in the Human HSC Niche: Repository (Development, 2023)

This repo contains code used for the single cell and ligand-receptor analyses in the below publication:

## An interactive resource of molecular signalling in the developing human haematopoietic stem cell (HSC) niche
**Edie I Crosse**, Anahi Binagui-Casas, Sabrina Gordon-Keylock, Stanislav Rybtsov, Sara Tamagno, Didrik Olofsson, Richard A Anderson, Alexander Medvinsky

URL: TBD

### Abstract:
The emergence of definitive human haematopoietic stem cells (HSCs) during Carnegie Stages (CS) 14-17 in the aorta-gonad-mesonephros (AGM) region is a tightly regulated process. Previously, we conducted spatial transcriptomic analysis of the human AGM region at the end of this period (CS16/17) and identified secreted factors involved in HSC development. Here, we extend our analysis to investigate the progression of dorso-ventral polarized signalling around the dorsal aorta over the entire period of HSC emergence. Our results reveal a dramatic increase in ventral signalling complexity from the CS13 to CS14 transition, coinciding with the first appearance of definitive HSCs. We further observe stage-specific changes in signalling up to CS17 which may underpin the  step-wise maturation of HSCs described in the mouse model. The data-rich resource is also presented in an online interface enabling in silico analysis of molecular interactions between spatially defined domains of the AGM region. This resource will be of particular interest for researchers studying mechanisms underlying human HSC development as well as those developing in vitro methods for the generation of clinically relevant HSCs from pluripotent stem cells. 


## Available files

### `SingleCell.py`

Pipeline for single cell analyses from Figures 5 and 6. The ScanPy pipeline (Wolf et al., 2018) was used to explore and integrate the dataset with other dorsal aorta single cell datasets spanning stages CS13 – CS15 from a publicly available resource (Zeng et al., 2019). For all datasets, cells with less than 200 genes and genes that were in less than 3 cells were filtered out. Cells with a percentage of mitochondrial genes >1 were also filtered out. Contaminating HB genes were also removed from the CS13 dorsal aorta dataset. The reads per cell were normalized and logarithmised. The variance effects of total counts per cell, cell cycle and mitochondrial genes were regressed out. Each dataset was then subset to include only genes with highly variable expression. The tool Scanorama (Hie et al., 2019) was used to integrate datasets. Then nearest neighbours was computed using 10 principal components and the neighbourhood graph was embedded in two dimensions in a  Uniform Manifold Approximation and Projection (UMAP) (Becht et al., 2018). Clustering of sub-populations within the UMAP were made using the Leiden algorithm (Traag et al., 2019). Following cluster identification by gene signature and any known identities from prior sorting strategies, the data was then subset into two parts to include haematopoietic and endothelial populations in one subset and stromal and epithelial populations in the second. Partition-based graph abstraction (PAGA)(Wolf et al., 2019) was used to make lineage inferences from the neighbourhood graphs.

### `NATMI.sh`

Code for usage of the tool NATMI (Hou et al., 2020) used for predicting ligand-receptor interactions across spatial domains and single cell clusters and which is the foundation for the web interactive exploration tool. The internal default ligand-receptor database ‘lrc2p’ was used which has literature supported ligand-receptor pairs – please see Supplementary data 1 from the original NATMI publication for literature references for each predicted ligand-receptor pair. Weight values of type ‘mean’ and a detection threshold of 0.2 were used. Interactions based on specificity, (the mean expression of the ligand/receptor in a spatial domain or cluster divided by the sum of the mean expression of that ligand/receptor across all domains/clusters/) were considered rather than interactions based on expression level as this gives a better resolution of differential contributions of the different populations. 

