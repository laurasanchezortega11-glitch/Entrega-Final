import os
import csv

results_dir = "../data/results"

with open("../data/protein_families.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Protein", "Family"])

    for result in os.listdir(results_dir):

        if result.endswith(".tbl"):

            protein = result.replace(".tbl", "")

            with open(f"{results_dir}/{result}") as tbl:

                for line in tbl:

                    if line.startswith("#"):
                        continue

                    line = line.strip()

                    if not line:
                        continue

                    family = line.split()[0]

                    writer.writerow([protein, family])