from datetime import datetime
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()
subtotal = float(input("Please enter the subtotal: "))
if day_of_week in {1, 2} and subtotal >= 50:
    discount = subtotal * 0.1  # 10% discount
    subtotal -= discount
else:
    discount = 0
    sales_tax = subtotal * 0.06
total_due = subtotal + sales_tax
print("Discount amount:", discount)
print("Sales tax amount:", sales_tax)
print("Total amount due:", total_due)
