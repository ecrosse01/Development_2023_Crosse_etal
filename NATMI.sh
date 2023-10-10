#!/bin/bash

# Set up pathdirs
MATRIX="/path/to/directory/em_raw.csv"
ANNO="/path/to/directory/metadata.csv"
export MATRIX
export ANNO

# Switch to the NATMI directory
cd NATMI


# NATMI commands used in paper
python ExtractEdges.py --species human --emFile $MATRIX --annFile $ANNO --interDB lrc2p --coreNum 4 --out Early_niche_web_raw

python VisInteractions.py --sourceFolder Early_niche_web_raw --interDB lrc2p --weightType mean --detectionThreshold 0.2 --drawNetwork y --plotWidth 6 --plotHeight 6 --layout circle --fontSize 15 --edgeWidth 6 --maxClusterSize 0 --clusterDistance 0.6

python VisInteractions.py --sourceFolder Early_niche_web_raw --drawClusterPair y --keepTopEdge 15

python VisInteractions.py --sourceFolder Early_niche_web_raw --drawLRNetwork PTGS2 CAV1 --plotWidth 4 --plotHeight 4 --layout circle --fontSize 15 --edgeWidth 6 --maxClusterSize 0 --clusterDistance 0.6

python VisInteractions.py --sourceFolder LCM_Seq_CS13 --drawLRNetwork POSTN PTK7 --plotWidth 4 --plotHeight 4 --layout circle --fontSize 15 --edgeWidth 6 --maxClusterSize 0 --clusterDistance 0.6
