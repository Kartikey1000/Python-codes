from fpdf import FPDF


def main():
    name = input("Name: ")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font("helvetica", style="B", size=30)
    pdf.cell(0, 20, "CS50 Shirtificate", align="C")

    pdf.image(
        "jharvard.png",
        x=35,
        y=50,
        w=140
    )

    # Cover original text
    pdf.set_fill_color(126, 16, 52)
    pdf.rect(75, 155, 60, 12, style="F")

    # Add user's name
    pdf.set_font("helvetica", style="B", size=20)
    pdf.set_text_color(255, 255, 255)

    name_width = pdf.get_string_width(name)
    x = (210 - name_width) / 2

    pdf.text(x=x, y=164, text=name)

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()