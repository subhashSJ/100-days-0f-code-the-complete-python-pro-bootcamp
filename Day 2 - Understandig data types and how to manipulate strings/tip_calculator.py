print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(
    input("What percentage tip would you like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill? "))

print(
    f"Each person should pay: ${'{:.2f}'.format(round((total_bill + (total_bill * tip_percentage)/ 100)/total_people, 2))}")
