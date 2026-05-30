from downloader import download_fasta


with open("proteins.txt") as file:

    for line in file:

        protein_id = line.strip()

        download_fasta(protein_id)