product_name = input("Enter the product name: ")
price = float(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))
if(quantity < 0):
    print("Quantity cannot be negative. Please enter a valid quantity.")
else:
    quantity = int(input("Enter the quantity: "))
total_cost = price * quantity
gst = total_cost * 0.18
final_amount = total_cost + gst
receipt = {
    "Product Name": product_name,
    "Price": price,
    "Quantity": quantity,
    "Total Cost": total_cost,
    "GST (18%)": gst,
    "Final Amount": final_amount
}
print("Final Receipt:")
print("Product Name:", receipt["Product Name"])
print("Price:", receipt["Price"])
print("Quantity:", receipt["Quantity"])
print("Total Cost:", receipt["Total Cost"])
print("GST (18%):", receipt["GST (18%)"])
print("Final Amount:", receipt["Final Amount"])