import sys
import csv
from tabulate import tabulate

if len(sys.argv)!=2:
    sys.exit()
if not sys.argv[1].endswith(".csv"):
    sys.exit()

try:
    with open(sys.argv[1]) as file:
        reader= csv.reader(file)
        table=list(reader)

except FileNotFoundError:
    sys.exit()

print(tabulate(table[1:],headers=table[0],tablefmt="grid"))