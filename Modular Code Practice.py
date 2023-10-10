car_wash_request = input("Do you want a basic or premium wash?")
if car_wash_request == "basic":
    print("Prepare to pay.")
basic_money = input("That will be $6. Please insert money.")
if basic_money == "$6":
    print("basic soap")
    print("basic rinse")
    print("basic dry")
if car_wash_request == "premium":
    print("Prepare to pay.")
premium_money = input("That will be $12. Please insert money.")
if premium_money == "$12":
    print("premium soap")
    print("premium rinse")
    print("premium drying")