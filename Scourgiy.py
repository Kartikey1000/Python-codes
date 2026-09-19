import csv
import sys

if len(sys.argv)!=3:
    sys.exit("Too fewor too many command line")

try:
    with open(sys.argv[1]) as file:
        reader =csv.DictReader(file)

        with open(sys.argv[2],"w",newline="") as output:
            writer = csv.DictWriter(output,fieldnames=["first","last","house"])

            writer.writeheader()

            for row in reader:
                last,first= row["name"].split(", ")

                writer.writerow({
                    "first":first,
                    "last":last,
                    "house":row["house"]
                })
except FileNotFoundError:
    sys.exit(f"could not read {sys.argv[1]}")