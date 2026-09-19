import sys 

if len(sys.argv) !=2:
    sys.exit("Too few or too many comand line arguments")

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a python file")

try:
    with open(sys.argv[1]) as file:
        lines=file.readlines()
except FileNotFoundError:
    sys.exit("File doesn't exit")

count=0

for line in lines:
    line=line.strip()

    if line=="":
        continue

    if line.startswith("#"):
        continue
    count+=1

print(count)