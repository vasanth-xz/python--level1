print("Dhanush Supermarket")
print("No.44,Nehru street,puducherry")
print("-----------------------------")
print("Bill Receipt")
print("-----------------------------")
str1=input("Enter the serial Number:")
str2=input("Enter the particulars:")
rate=int(input("Enter the rate:"))
Quantity=int(input("Enter the Quantity:"))
Total=rate*Quantity
print("Total Amount Rs:",Total)
GST=Total*10/100
print("GST(10 per):",GST)
paid=Total+GST
print("Amount to be paid Rs:",Total)
