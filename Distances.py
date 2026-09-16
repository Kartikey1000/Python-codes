distance={
    "V1":"163",
    "V2":"136",
    "p10":"80 AU",
    "NH":"58",
    "P11":"44 AU"
}

def main():
    spacecraft=input("enter a sapcecraft: ")
    try:
        au= float(distance[spacecraft])
    except KeyError:
        print(f"Can't find the {spacecraft}")
        return
    except ValueError:
        print(f"Can't Convert '{distance[spacecraft]}' to a float ")
        return

    m= convert(au)
    print(f"{m} m away")

def convert(au):
    return au*149597870700

main() 