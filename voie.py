# Make it unicode font
from tkinter import *
from fpdf import FPDF
from tkinter import messagebox
import os
from datetime import datetime

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
    selected_service = medicine_listbox.get(ANCHOR)
    if selected_service:
        quantity = int(quantity_entry.get())
        price = services[selected_service]
        item_total = price * quantity
        invoice_items.append((selected_service, quantity, item_total))
        total_amount_entry.delete(0, END)
        total_amount_entry.insert(END, str(calculate_total()))
        update_invoice_text()

def calculate_total():
    total = 0.0
    for item in invoice_items:
        total += item[2]
    return total

def generate_invoice():
    if not invoice_items:
        messagebox.showerror("Грешка", "Добавете услуги към фактурата първо!")
        return

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Header with "Invoice" and current date and time
    pdf.cell(200, 10, "Фактура", ln=True, align="C")
    pdf.cell(200, 10, datetime.now().strftime("%d/%m/%Y %H:%M:%S"), ln=True, align="C")
    pdf.cell(200, 10, "", ln=True)  # Add empty line

    # Customer name
    customer_name = customer_entry.get()
    pdf.cell(0, 10, f"Име на Фирма: {customer_name}", ln=True)

    # Customer ID
    customer_id = id_entry.get()
    pdf.cell(0, 10, f"EИК на Фирма: {customer_id}", ln=True)

    # Invoice items
    pdf.cell(0, 10, "Услуги:", ln=True)
    for item in invoice_items:
        pdf.cell(0, 10, f"Услуга: {item[0]}, Брой: {item[1]}, Общо: {item[2]}", ln=True)

    # Total amount
    total_amount = calculate_total()
    pdf.cell(0, 10, f"Обща стоймост: {total_amount}", ln=True)

    # Save the PDF with a custom name
    file_name = f"C:/Invoice/{customer_name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.pdf"
    pdf.output(file_name)
    messagebox.showinfo("Успешно", f"Фактурата е създадена и запазена в:\n{file_name}")

    # Clear invoice items
    invoice_items.clear()
    update_invoice_text()

def update_invoice_text():
    invoice_text.delete(1.0, END)
    for item in invoice_items:
        invoice_text.insert(END, f"Услуга: {item[0]}, Брой: {item[1]}, Общо: {item[2]}\n")

# Labels, Listbox, Entries, and Buttons
medicine_label = Label(window, text="Услуга:", font=unicode_font)
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

# Start the GUI event loop
window.mainloop()
