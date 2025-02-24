python ~/Programs/esm/scripts/extract.py esm2_t33_650M_UR50D example.fa embeddings/esm2_t33_650M_UR50D --repr_layers 33 --include mean
python ~/Programs/esm/scripts/extract.py esm2_t30_150M_UR50D example.fa embeddings/esm2_t30_150M_UR50D --repr_layers 26 --include mean
python ~/Programs/esm/scripts/extract.py esm2_t36_3B_UR50D example.fa embeddings/esm2_t36_3B_UR50D --repr_layers 11 --include mean
python ~/Programs/esm/scripts/extract.py esm1b_t33_650M_UR50S example.fa embeddings/esm1b_t33_650M_UR50S --repr_layers 4 6 --include mean
python ~/Programs/esm/scripts/extract.py esm2_t12_35M_UR50D example.fa embeddings/esm2_t12_35M_UR50D --repr_layers 7 --include mean

#conda activate esm
#if need all layers use "--repr_layers 0 33"
