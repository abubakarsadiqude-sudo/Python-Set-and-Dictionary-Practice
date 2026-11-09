inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15,
    "Monitor": 8
}

while True:

    print("\n===== SHOP INVENTORY MANAGEMENT =====")
    print("1. Add New Product")
    print("2. Remove Product")
    print("3. Update Product Quantity")
    print("4. Search Product")
    print("5. Display All Products")
    print("6. Display Products Below 10")
    print("7. Calculate Total Items")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    # 1. Add New Product
    if choice == "1":

        product = input("Enter product name: ").title()

        if product in inventory:
            print("Product already exists!")

        else:
            quantity = int(input("Enter product quantity: "))

            inventory[product] = quantity

            print("Product added successfully!")

    # 2. Remove Existing Product
    elif choice == "2":

        product = input("Enter product name: ").title()

        if product in inventory:
            inventory.pop(product)
            print("Product removed successfully!")

        else:
            print("Product not found!")

    # 3. Update Product Quantity
    elif choice == "3":

        product = input("Enter product name: ").title()

        if product in inventory:

            quantity = int(input("Enter new quantity: "))

            inventory.update({product: quantity})

            print("Product quantity updated successfully!")

        else:
            print("Product not found!")

    # 4. Search for a Product
    elif choice == "4":

        product = input("Enter product name: ").title()

        if product in inventory:

            print("Product:", product)
            print("Quantity:", inventory[product])

        else:
            print("Product not found!")

    # 5. Display All Products
    elif choice == "5":

        print("\n===== ALL PRODUCTS =====")

        for product, quantity in inventory.items():

            print(f"{product}: {quantity}")

    # 6. Display Products Below 10
    elif choice == "6":

        print("\n===== LOW STOCK PRODUCTS =====")

        found = False

        for product, quantity in inventory.items():

            if quantity < 10:

                print(f"{product}: {quantity}")
                found = True

        if not found:
            print("All products have sufficient stock.")

    # 7. Calculate Total Items
    elif choice == "7":

        total = sum(inventory.values())

        print("Total Items in Inventory:", total)

    # 8. Exit
    elif choice == "8":

        print("Thank you for using Inventory Management System!")
        break

    else:
        print("Invalid choice! Please enter 1-8.")
    
    


    