from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_invoice(invoice_number, customer_name, items, output_file):
    c = canvas.Canvas(output_file, pagesize=A4)
    width, height = A4

    # Company Info
    company_name = "My Company Inc."
    company_address = "123 Business Rd\nCityville, India"
    company_logo = None  # Add path to logo image if needed

    # Header Section
    c.setFillColor(colors.darkblue)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(30, height - 50, company_name)
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.black)
    c.drawString(30, height - 70, company_address)

    # Optional Logo
    if company_logo:
        c.drawImage(company_logo, width - 100, height - 80, width=60, preserveAspectRatio=True)

    # Invoice Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(30, height - 110, "INVOICE")

    # Invoice Details
    c.setFont("Helvetica", 10)
    c.drawString(30, height - 130, f"Invoice #: {invoice_number}")
    c.drawString(30, height - 145, f"Date: {datetime.today().strftime('%Y-%m-%d')}")
    c.drawString(30, height - 160, f"Billed To: {customer_name}")

    # Table Header Background
    c.setFillColor(colors.lightgrey)
    c.rect(30, height - 190, width - 60, 20, fill=1)

    # Table Headers
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(35, height - 185, "Item")
    c.drawString(250, height - 185, "Quantity")
    c.drawString(350, height - 185, "Price")
    c.drawString(450, height - 185, "Total")

    y = height - 210
    total_amount = 0
    c.setFont("Helvetica", 10)

    # Table Rows
    for item in items:
        name, qty, price = item
        total = qty * price
        total_amount += total

        c.drawString(35, y, name)
        c.drawString(250, y, str(qty))
        c.drawString(350, y, f"${price:.2f}")
        c.drawString(450, y, f"${total:.2f}")
        y -= 20

    # Total
    c.setFont("Helvetica-Bold", 11)
    c.drawString(350, y - 10, "Total Amount:")
    c.drawString(450, y - 10, f"${total_amount:.2f}")

    # Footer
    c.setFont("Helvetica", 9)
    c.setFillColor(colors.grey)
    c.drawString(30, 50, "Thank you for your business!")
    c.drawString(30, 40, "Contact us: support@mycompany.com")

    c.save()
    print(f"Stylish invoice saved as '{output_file}'")

# You can call this function using input-based code as shown earlier

    print(f"Invoice saved as '{output_file}'")

# --- Main Program ---
def main():
    print("=== INVOICE GENERATOR ===")

    invoice_number = input("Enter invoice number: ")
    customer_name = input("Enter customer name: ")

    items = []
    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        try:
            qty = int(input("Enter quantity: "))
            price = float(input("Enter price per item: "))
            items.append((item_name, qty, price))
        except ValueError:
            print("Invalid input. Please enter numeric values for quantity and price.")

    if not items:
        print("No items added. Exiting.")
        return

    filename = f"{invoice_number.replace('/', '-')}.pdf"
    generate_invoice(invoice_number, customer_name, items, filename)

if __name__ == "__main__":
    main()
