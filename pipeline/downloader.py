import requests


def download_fasta(uniprot_id):

    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta"

    response = requests.get(url)

    filename = f"../data/fasta/{uniprot_id}.fasta"

    with open(filename, "w") as file:

        file.write(response.text)

    print(f"{uniprot_id} descargado")