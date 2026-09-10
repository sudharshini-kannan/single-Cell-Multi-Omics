# 🧬 Single-Cell Multi-Omics Analysis

A hands-on bioinformatics project exploring the integration of multiple single-cell data modalities using real 10x Genomics data.

This project focuses on understanding how **gene expression** and **chromatin accessibility** can be explored together in a single-cell multi-omics workflow.

---

## 🎯 Project Objectives

* Learn the fundamentals of single-cell multi-omics analysis.
* Work with real 10x Genomics multiome data.
* Explore RNA and ATAC modalities.
* Understand the relationship between chromatin accessibility and gene expression.
* Build reproducible and lightweight bioinformatics workflows.
* Develop a GitHub portfolio project using Python and modern single-cell analysis tools.

---

## 🧪 Dataset

This project uses the **PBMC from a healthy donor with granulocytes removed through cell sorting (3k)** dataset generated using the **10x Genomics Cell Ranger ARC pipeline**.

### Dataset components used

| Data                  | Description                                             |
| --------------------- | ------------------------------------------------------- |
| RNA expression matrix | Cell × gene expression data                             |
| ATAC peaks            | Genomic regions associated with chromatin accessibility |
| ATAC peak annotation  | Peak-to-gene annotations                                |

### Dataset size

To keep the workflow suitable for a laptop with limited memory, only lightweight files are used.

The large ATAC fragment file is intentionally not downloaded.

---

## 📊 Current Dataset

### RNA Data

* **Cells:** 2,711
* **Features:** 36,601
* **Unique gene names:** 36,591
* **Duplicate gene names:** 10
* **Feature type:** Gene Expression

The RNA data is stored as a 10x Genomics `.h5` file.

---

### ATAC Data

The ATAC annotation contains:

* **125,117 peak annotations**
* **98,319 unique genomic peaks**

Peak annotations are classified as:

* Promoter
* Distal
* Intergenic

---

## 🔗 RNA–ATAC Gene-Level Analysis

The project compares genes detected in the RNA dataset with genes associated with ATAC peaks.

### Results

| Category                     | Result |
| ---------------------------- | -----: |
| Unique RNA genes             | 36,591 |
| Unique ATAC-associated genes | 27,844 |
| Shared RNA–ATAC genes        | 27,844 |

### ATAC Peak Summary

| Peak Type  | Annotation Rows | Unique Associated Genes | Genes Present in RNA |
| ---------- | --------------: | ----------------------: | -------------------: |
| Promoter   |          21,144 |                  18,279 |               18,279 |
| Distal     |         103,452 |                  23,884 |               23,884 |
| Intergenic |             521 |                       0 |                    0 |

---

## 🧬 Workflow

```text
10x Genomics Multiome Dataset
            │
            ├───────────────┐
            │               │
            ▼               ▼
       RNA Data        ATAC Annotation
            │               │
            ▼               ▼
     Gene Expression    Peak-to-Gene Mapping
            │               │
            └───────┬───────┘
                    │
                    ▼
          RNA–ATAC Gene Overlap
                    │
                    ▼
       Promoter / Distal Analysis
```

---

## 📁 Project Structure

```text
Single-Cell-Multiomics/
│
├── data/
│   └── raw/
│       ├── pbmc_granulocyte_sorted_3k_filtered_feature_bc_matrix.h5
│       │
│       └── pbmc3k_multiome/
│           ├── atac_peaks.bed
│           └── atac_peak_annotation.tsv
│
├── results/
│   ├── atac_peak_summary.csv
│   └── rna_atac_shared_genes.csv
│
├── src/
│   └── real_multiome.py
│
├── requirements.txt
├── test_installation.py
└── README.md
```

---

## 💻 Tools and Libraries

* Python
* Scanpy
* AnnData
* Muon
* MuData
* pandas
* NumPy
* mudatasets

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/sudharshini-kannan/single-Cell-Multi-Omics.git
```

Move into the project directory:

```bash
cd single-Cell-Multi-Omics
```

Create and activate a virtual environment:

```bash
python3 -m venv multiomics_env
source multiomics_env/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Analysis

```bash
python src/real_multiome.py
```

The script:

1. Loads the 10x Genomics RNA dataset.
2. Inspects RNA features and gene information.
3. Checks duplicate gene names.
4. Loads ATAC peak annotations.
5. Identifies genes shared between RNA and ATAC data.
6. Summarizes promoter, distal, and intergenic peak annotations.
7. Saves reproducible results.

---

## 📈 Output Files

### `results/rna_atac_shared_genes.csv`

Contains genes shared between:

* RNA expression data
* ATAC peak-associated gene annotations

### `results/atac_peak_summary.csv`

Contains a summary of:

* Peak types
* Number of annotations
* Unique associated genes
* Genes overlapping with RNA data

---

## ⚠️ Important Scientific Note

This project currently includes:

* ✅ Cell × gene RNA expression data
* ✅ ATAC peak coordinates
* ✅ ATAC peak-to-gene annotations

However, it does **not yet include a cell × ATAC peak accessibility matrix**.

Therefore, the current workflow represents:

> **Gene-level exploration of RNA expression and ATAC peak annotations rather than full cell-level RNA–ATAC integration.**

Future work will focus on lightweight approaches for extending this project toward true multi-modal single-cell integration.

---

## 🔮 Future Directions

* RNA quality control and filtering
* RNA normalization and highly variable gene selection
* PCA and dimensionality reduction
* UMAP visualization
* Cell clustering
* Cell-type annotation
* Exploration of lightweight cell-level ATAC data
* Construction of a MuData object containing multiple modalities
* RNA–ATAC multi-modal integration
* Visualization of relationships between chromatin accessibility and gene expression

---

## 👩‍💻 Author

**Sudharshini Kannan**
Molecular Biology Researcher | Bioinformatics & Genomics Enthusiast

GitHub: https://github.com/sudharshini-kannan
