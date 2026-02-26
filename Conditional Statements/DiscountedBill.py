def DiscountedBill(Bill):

    if Bill!=0:
        if Bill <= 1000:
            return Bill - (Bill*0.1)
        elif Bill <= 5000:
            return Bill - (Bill*0.15) 
        elif Bill <= 10000:
            return Bill - (Bill*0.2)
        else: return Bill - (Bill*0.25)
    else: return "Invalid Input"

print(DiscountedBill(int(input('Enter the Bill Amount: '))))

