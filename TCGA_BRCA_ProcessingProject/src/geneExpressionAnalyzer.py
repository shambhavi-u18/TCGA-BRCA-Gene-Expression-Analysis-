import pandas as pd 
import matplotlib.pyplot as plt

patient1 =  pd.read_csv(
    "TCGA_BRCA_PatientData/patient1_gene_count_data/patient1_data/patient1_data.tsv",
    sep="\t", 
    comment="#"); 

patient2 =  pd.read_csv(
    "TCGA_BRCA_PatientData/patient2_gene_count_data/patient2_data/patient2_data.tsv",
    sep="\t", 
    comment="#"); 

patient3 =  pd.read_csv(
    "TCGA_BRCA_PatientData/patient3_gene_count_data/patient3_data/patient3_data.tsv",
    sep="\t", 
    comment="#"); 

def processData(df, type): 
    df = df[df["gene_type"] == "protein_coding"] 
    df = df[["gene_name", "tpm_unstranded"]]
    df = df.rename(columns={"tpm_unstranded": f"tpm_{type}"})
    return df

p1 = processData(patient1, "p1")
p2 = processData(patient2, "p2")
p3 = processData(patient3, "p3")

allPatientsMerged = p1.merge(p2, on = "gene_name")
allPatientsMerged = allPatientsMerged.merge(p3, on = "gene_name")

allPatientsMerged["avg_counts"] = allPatientsMerged[["tpm_p1", "tpm_p2", "tpm_p3"]].mean(axis=1)

top10Gene_Counts = allPatientsMerged.sort_values(by="avg_counts", ascending=False).head(10)

print("Top 10 genes expressed in breast cancer tissue:")

top10Gene_Counts.plot(kind = "bar", x = "gene_name", y = "avg_counts", legend=False, figsize=(10, 6))

plt.show(); 