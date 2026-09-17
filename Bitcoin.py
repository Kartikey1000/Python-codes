import requests
import sys

def main():
    if len(sys.argv)!=2:
        sys.exit("Missing command line Argument")

    try:
        n=float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response=requests.get(" rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey")
        response.raise_for_status()
        data=response.json()

        price=float(data["data"]["priceUsd"])
        cost = n*price

        print(f"${cost:,.4f}")

    except requests.RequestException:
        sys.exit("Request failed")

main()

    
