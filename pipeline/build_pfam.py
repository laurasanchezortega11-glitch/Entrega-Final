import os


with open("../PFAMdescargas/families.txt") as file:

    for line in file:

        family = line.strip()

        cmd = f"hmmfetch ../PFAMdescargas/Pfam-A.hmm {family} >> ../PFAMdescargas/miniPfam.hmm"

        print(cmd)

        os.system(cmd)
        