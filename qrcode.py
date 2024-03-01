# make it unicode font
from tkinter import *
from fpdf import FPDF

window = Tk()
window.title("Фактуриране")



# Use a font that supports Unicode characters
unicode_font = ("Arial Unicode MS", 12)

services = {
    "Услуга 1": 10,
    "Услуга 2": 20,
    "Услуга 3": 15,
    "Услуга 4": 25
}
invoice_items = []
total_amount = 0.0

def add_service():
    selected_medicine = medicine_listbox.get(ANCHOR)
    if selected_medicine:
        quantity = int(quantity_entry.get())
        price = services[selected_medicine]
        item_total = price * quantity
        invoice_items.append((selected_medicine, quantity, item_total))
        total_amount_entry.delete(0, END)
        total_amount_entry.insert(END, str(calculate_total()))
        update_invoice_text()

def calculate_total():
    total = 0.0
    for item in invoice_items:
        total += item[2]
    return total

def generate_invoice():
    customer_name = customer_entry.get()  # Get customer name from an entry widget
    customer_id = id_entry.get()  # Get customer ID from an entry widget

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)  # Set font to Arial with size 12
    LMARGIN = 10  # Left margin
    NEXT = pdf.get_y() + 10  # Get current y position + 10 for next line
    C = 'C'  # Center align
    L = 'L'  # Left align

    # Add the Invoice title
    pdf.cell(0, 10, txt="Invoice", ln=True, align=C)  # ln=True moves to the next line after cell

    # Add Customer Name
    pdf.cell(0, 10, txt="Customer: " + customer_name, ln=True, align=L)

    # Add Customer ID
    pdf.cell(0, 10, txt="ЕИК: " + customer_id, ln=True, align=L)

    # Loop through invoice items and add them to the PDF
    for item in invoice_items:
        medicine_name, quantity, item_total = item
        pdf.cell(0, 10, txt=f"услуга: {medicine_name}, Брой: {quantity}, Общо: {item_total}", ln=True, align=L)

    # Add the Total Amount
    pdf.cell(0, 10, txt="Total Amount: " + str(calculate_total()), ln=True, align=L)

    # Save the PDF to a file named "invoice.pdf"
    pdf.output("invoice.pdf")

medicine_label = Label(window, text="услуга:", font=unicode_font)
medicine_label.pack()

medicine_listbox = Listbox(window, selectmode=SINGLE, font=unicode_font)
for medicine in services:
    medicine_listbox.insert(END, medicine)
medicine_listbox.pack()

quantity_label = Label(window, text="Брой:", font=unicode_font)
quantity_label.pack()

quantity_entry = Entry(window, font=unicode_font)
quantity_entry.pack()

add_button = Button(window, text="Добави услуга", command=add_service, font=unicode_font)
add_button.pack()

total_amount_label = Label(window, text="Обща стоймост:", font=unicode_font)
total_amount_label.pack()

total_amount_entry = Entry(window, font=unicode_font)
total_amount_entry.pack()

customer_label = Label(window, text="Име на Фирма:", font=unicode_font)
customer_label.pack()

customer_entry = Entry(window, font=unicode_font)
customer_entry.pack()

id_label = Label(window, text="EИК на Фирма:", font=unicode_font)
id_label.pack()

id_entry = Entry(window, font=unicode_font)
id_entry.pack()

generate_button = Button(window, text="Направи фактура", command=generate_invoice, font=unicode_font)
generate_button.pack()

invoice_text = Text(window, height=10, width=50, font=unicode_font)
invoice_text.pack()

def update_invoice_text():
    invoice_text.delete(1.0, END)
    for item in invoice_items:
        invoice_text.insert(END, f"Услуга: {item[0]}, Брой: {item[1]}, Общо: {item[2]}\n")

# Start the GUI event loop
window.mainloop()
