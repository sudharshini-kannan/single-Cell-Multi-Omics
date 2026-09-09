import numpy as np
import pandas as pd
import anndata as ad
import mudata as md

# Set a random seed for reproducibility
np.random.seed(42)

# -----------------------------------
# Create example scRNA-seq data
# -----------------------------------

rna_data = np.random.rand(5, 4)

rna = ad.AnnData(
    X=rna_data,
    obs=pd.DataFrame(
        index=["Cell_1", "Cell_2", "Cell_3", "Cell_4", "Cell_5"]
    ),
    var=pd.DataFrame(
        index=["Gene_A", "Gene_B", "Gene_C", "Gene_D"]
    ),
)

# -----------------------------------
# Create example scATAC-seq data
# -----------------------------------

atac_data = np.random.randint(0, 2, size=(5, 6))

atac = ad.AnnData(
    X=atac_data,
    obs=pd.DataFrame(
        index=["Cell_1", "Cell_2", "Cell_3", "Cell_4", "Cell_5"]
    ),
    var=pd.DataFrame(
        index=[
            "Peak_1",
            "Peak_2",
            "Peak_3",
            "Peak_4",
            "Peak_5",
            "Peak_6",
        ]
    ),
)

# -----------------------------------
# Combine RNA + ATAC
# -----------------------------------

mdata = md.MuData(
    {
        "rna": rna,
        "atac": atac,
    }
)

# -----------------------------------
# Inspect the MuData object
# -----------------------------------

print("\n===== MULTI-OMICS DATASET =====")

print("\nMuData object:")
print(mdata)

print("\nRNA shape:")
print(mdata["rna"].shape)

print("\nATAC shape:")
print(mdata["atac"].shape)

print("\nRNA genes:")
print(mdata["rna"].var_names.tolist())

print("\nATAC peaks:")
print(mdata["atac"].var_names.tolist())

print("\nShared cells:")
print(mdata.obs_names.tolist())

# -----------------------------------
# Save the multi-omics dataset
# -----------------------------------

mdata.write("results/example_multiomics.h5mu")

print("\nMulti-omics dataset saved successfully!")