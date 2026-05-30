import os

fasta_dir = "../data/fasta"
results_dir = "../data/results"
pfam_db = "../PFAMdescargas/miniPfam.hmm"

for file in os.listdir(fasta_dir):

    if file.endswith(".fasta"):

        protein_id = file.replace(".fasta", "")

        fasta_file = f"{fasta_dir}/{file}"

        result_file = f"{results_dir}/{protein_id}.tbl"

        cmd = (
            f"hmmscan --tblout {result_file} "
            f"{pfam_db} {fasta_file} > /dev/null"
        )

        print(f"Analizando {protein_id}")

        os.system(cmd)

print("Análisis terminado")
