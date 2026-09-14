distance={
    "V1":"163",
    "V2":"136",
    "p10":"80",
    "NH":"58",
    "P11":"44"
}
'''
def main():
    for name,dist in distance.items():#will return only keys.keys()function and .values() will return only value but items return key and value both
        #print(f"{name} is {distance[name]}Au from Earth")
        print(f"{name} is {dist}Au from Earth")



main()
'''
def main():
    for dist in distance.values():
        print(f"{dist} AU is {convert(dist)} m ")

def convert(au):
    return int(au) * 149597870700#if don't want to use the int then in dict remove the colons from numbers

main()
