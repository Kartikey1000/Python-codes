def main():

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            date = input("Date: ")

            # Format: 9/8/1636
            if "/" in date:
                month, day, year = date.split("/")

                month = int(month)
                day = int(day)
                year = int(year)

                if month < 1 or month > 12:
                    continue

                if day < 1 or day > 31:
                    continue

            # Format: September 8, 1636
            elif "," in date:
                month, day, year = date.replace(",", "").split()

                if month not in months:
                    continue

                month = months.index(month) + 1
                day = int(day)
                year = int(year)

                if day < 1 or day > 31:
                    continue

            else:
                continue

            print(f"{year:04}-{month:02}-{day:02}")
            break

        except (ValueError, IndexError):
            continue


main()