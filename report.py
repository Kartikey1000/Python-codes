def main():
    spacecraft={"name":"JAmes Webb"}
    #spacecraft["distance"]=0.01
    spacecraft.update({"distance":0.01,"orbit":"Sun"})
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    =========Report=========

    Name:{spacecraft.get("name","Unknown")}
    Distance: {spacecraft.get("distance","Unknown")} AU 
    Orbit:{spacecraft.get("orbit","unknown")}

    ========================

"""

main()