print("Welcome to the Tip Calculator")
bill=float((input("What is the total bill? $ ")))
tip_perct=int(input("What percentage tip you want to give 10, 12 0r 15? (in number) "))
noof_persons=int(input("How many people are splitting the bill? "))
total_bill= ((tip_perct/100)* bill)+bill
ind_bill=total_bill/noof_persons
final_bill=round(ind_bill,2)
final_bill="{:.2f}".format(final_bill)
print(f"Each person should pay: ${final_bill}")