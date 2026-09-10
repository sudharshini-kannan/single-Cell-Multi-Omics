import scanpy as sc
import pandas as pd
import os


# =========================================================
# Real 10x Genomics PBMC Multiome Data Exploration
# =========================================================

# File paths
rna_path = (
    "data/raw/"
    "pbmc_granulocyte_sorted_3k_filtered_feature_bc_matrix.h5"
)

atac_annotation_path = (
    "data/raw/pbmc3k_multiome/"
    "atac_peak_annotation.tsv"
)

# Create results directory
os.makedirs("results", exist_ok=True)


# =========================================================
# 1. Load RNA data
# =========================================================

print("\nLoading 10x Genomics dataset...")

adata = sc.read_10x_h5(rna_path)

print("\n===== RNA DATA LOADED SUCCESSFULLY =====")

print("\nAnnData object:")
print(adata)

print("\nShape (cells × features):")
print(adata.shape)


# =========================================================
# 2. Inspect feature types
# =========================================================

print("\n===== FEATURE TYPES =====")

print(adata.var["feature_types"].value_counts())


# =========================================================
# 3. Inspect RNA gene information
# =========================================================

print("\n===== RNA GENE INFORMATION =====")

print("\nVariable columns:")
print(adata.var.columns.tolist())

print("\nFirst 10 features:")
print(adata.var.head(10))

print("\nFirst 10 cell barcodes:")
print(adata.obs_names[:10].tolist())

print("\nTotal features:")
print(adata.n_vars)

print("\nUnique gene names:")
print(len(set(adata.var_names)))

print("\nDuplicate gene names:")
print(adata.var_names.duplicated().sum())


# =========================================================
# 4. Load ATAC peak annotation
# =========================================================

print("\nLoading ATAC peak annotation...")

atac = pd.read_csv(
    atac_annotation_path,
    sep="\t"
)

print("\n===== ATAC PEAK ANNOTATION LOADED =====")

print("\nATAC annotation shape:")
print(atac.shape)

print("\nColumns:")
print(atac.columns.tolist())

print("\nFirst 5 rows:")
print(atac.head())


# =========================================================
# 5. RNA-ATAC gene overlap
# =========================================================

print("\n===== RNA-ATAC GENE OVERLAP =====")

rna_genes = set(adata.var_names)

atac_genes = set(
    atac["gene"].dropna()
)

shared_genes = rna_genes.intersection(
    atac_genes
)

print("\nUnique RNA genes:")
print(len(rna_genes))

print("\nUnique ATAC-associated genes:")
print(len(atac_genes))

print("\nShared RNA-ATAC genes:")
print(len(shared_genes))

print("\nFirst 20 shared genes:")
print(sorted(shared_genes)[:20])


# =========================================================
# 6. Save shared RNA-ATAC genes
# =========================================================

shared_genes_df = pd.DataFrame(
    sorted(shared_genes),
    columns=["gene"]
)

shared_genes_output = (
    "results/rna_atac_shared_genes.csv"
)

shared_genes_df.to_csv(
    shared_genes_output,
    index=False
)

print("\nShared genes saved to:")
print(shared_genes_output)


# =========================================================
# 7. ATAC peak type summary
# =========================================================

print("\n===== ATAC PEAK TYPE SUMMARY =====")

summary = []

for peak_type in [
    "promoter",
    "distal",
    "intergenic"
]:

    subset = atac[
        atac["peak_type"] == peak_type
    ]

    genes = set(
        subset["gene"].dropna()
    )

    shared = genes.intersection(
        rna_genes
    )

    summary.append(
        {
            "peak_type": peak_type,
            "annotation_rows": len(subset),
            "unique_associated_genes": len(genes),
            "genes_present_in_rna": len(shared)
        }
    )

    print(f"\n{peak_type.upper()}")

    print(
        "Annotation rows:",
        len(subset)
    )

    print(
        "Unique associated genes:",
        len(genes)
    )

    print(
        "Genes also present in RNA:",
        len(shared)
    )


# =========================================================
# 8. Save ATAC peak summary
# =========================================================

summary_df = pd.DataFrame(summary)

summary_output = (
    "results/atac_peak_summary.csv"
)

summary_df.to_csv(
    summary_output,
    index=False
)

print("\nATAC peak summary saved to:")
print(summary_output)


# =========================================================
# 9. Scientific interpretation
# =========================================================

print("\n===== IMPORTANT NOTE =====")

print("\nThis dataset currently provides:")

print("- Cell × gene RNA expression data")
print("- ATAC peak coordinates")
print("- ATAC peak-to-gene annotations")

print(
    "\nA cell × ATAC peak accessibility "
    "matrix is not currently loaded."
)

print(
    "\nTherefore, this analysis represents "
    "gene-level RNA-ATAC exploration, "
    "not full cell-level multiome integration."
)

print("\n===== ANALYSIS COMPLETE =====\n")