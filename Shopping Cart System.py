prod_list = ['Laptop', 'Mouse', 'Mobile', 'Keyboard', 'Headphones']
price_list = [60000, 700, 20000, 1000, 500]

user_list=[]
while True:
    print("="*30)
    print("Welcome to Electronics Shopping Cart System")
    print("1. Admin")
    print("2. Customer")
    print("3. Exit")
    print("="*30)
    role=int(input("Choose your role 1. Admin or 2. Customer:"))
    
#Admin Section
    if role==1:
        while True:
            print("=" * 30)
            print("Welcome to admin section")
            print("=" * 30)
            print("1. Add product")
            print("2. Update product")
            print("3. Remove product")
            print("4. View Products")
            print("5. View Users")
            print("6. Exit")

            adm_menu_choice=int(input("Choose an option:"))

            if adm_menu_choice==1:
                print("="*30)
                print("Add Product")
                print("="*30)

                prod_name=input("Enter product name:")
                prod_price=int(input("Enter product price:"))

                if prod_price>0:
                    prod_list.append(prod_name)
                    price_list.append(prod_price)

                    print(prod_name," added successfully")
                else:
                    print("Price must be greater than zero")
                print("="*30)
                
            elif adm_menu_choice==2:
                print("="*30)
                print("Update product")
                print("="*30)

                if len(prod_list)==0:
                    print("No products is available")
                else:
                    print("Available Products")
                    for i in range(len(prod_list)):
                            print(i+1, ".", prod_list[i], "- Rs.", price_list[i])
                    prod_choice=int(input("which product want to update?"))

                    if prod_choice<=len(prod_list):
                        index=prod_choice-1

                        print("Selected product:",prod_list[index])
                        print("Current price:",price_list[index])

                        new_prod=input("enter new product name:")
                        new_price=int(input("enter new price:"))
                        if new_price>0:
                            prod_list[index]=new_prod
                            price_list[index]=new_price

                            print("Product updated successfully!")
                        else:
                            print("Price must be greater than zero")
                    else:
                        print("Invalid product choosen!")
                print("="*30)

            
            elif adm_menu_choice==3:
                print("="*30)
                print("Remove product")
                print("="*30)

                if len(prod_list)==0:
                    print("No products is available")
                else:
                    print("Available Products")
                    for i in range(len(prod_list)):
                            print(i+1, ".", prod_list[i], "- Rs.", price_list[i])
                    remove_prod=int(input("which product want to remove:"))

                    if remove_prod<=len(prod_list):
                        index=remove_prod-1

                        removed_product=prod_list.pop(index)
                        removed_price=price_list.pop(index)

                        print(removed_product,"product is removed")
                    else:
                        print("Invalid product choosen!")
                print("="*30)

            elif adm_menu_choice==4:
                print("="*30)
                print("View Products")
                print("="*30)

                if len(prod_list)==0:
                    print("No products is available currently")
                    
                else:
                    print("Available Products")
                    for i in range(len(prod_list)):
                        print(i+1, ".", prod_list[i], "- Rs.", price_list[i])
                print("="*30)
                

            elif adm_menu_choice==5:
                print("="*30)
                print("Registered Customers")
                print("="*30)

                if len(user_list)==0:
                    print("No customers found!")
                else:
                    for i in range(len(user_list)):
                        print(i+1,".",user_list[i])
                print("="*30)

            elif adm_menu_choice==6:
                print("=" * 30)
                print("Exiting Admin Section...")
                print("Returning to Main Menu")
                print("=" * 30)
                break
            else:
                print("Please select correct option from above only")
            
#Customer Section
    elif role==2:
        customer_name = input("Enter your name: ")
        user_list.append(customer_name)
        print("Welcome", customer_name)
        
        cart_list = []
        
        while True:
            print("=" * 30)
            print("WELCOME TO CUSTOMER SECTION")
            print("=" * 30)
            print("1. View Products")
            print("2. Add to Cart")
            print("3. View cart")
            print("4. Remove from Cart")
            print("5. Checkout")
            print("6. Exit")
            print("=" * 30)

            menu_choice = int(input("Choose an option: "))

            if menu_choice == 1:
                print("=" * 30)
                print("View Products")
                print("=" * 30)

                if len(prod_list) == 0:
                    print("No products available")
                else:
                    print("Available Products")
                    for i in range(len(prod_list)):
                        print(i+1, ".", prod_list[i], "- Rs.", price_list[i])


            elif menu_choice == 2:
                print("=" * 30)
                print("Add to cart")
                print("=" * 30)

                if len(prod_list) == 0:
                    print("No products available")
                else:
                    print("Available Products")
                    for i in range(len(prod_list)):
                        print(i+1, ".", prod_list[i], "- Rs.", price_list[i])

                    product_choice = int(input("Which product do you want to add to cart? "))
                    if product_choice >=1 and product_choice<=len(prod_list):
                        quantity=int(input("Enter quantity:"))
                        
                        selected_prod=prod_list[product_choice-1]
                        selected_price=price_list[product_choice-1]
                        
                        cart_list.append((selected_prod,selected_price,quantity))
                        print(selected_prod," is added")
                    else:
                        print("Invalid product! Please choose the product from above list only.")



            elif menu_choice == 3:
                if len(cart_list)==0:
                    print("Your cart is empty")
                else:
                    print("=" * 30)
                    print("Products in your cart")
                    print("=" * 30)

                    for i in range(len(cart_list)):
                        subtotal=cart_list[i][1]*cart_list[i][2]
                        print(i+1,".",cart_list[i][0],"- Rs.",cart_list[i][1],"quantity:",cart_list[i][2],"Subtotal=",subtotal)



            elif menu_choice == 4:
                removed_product=[]
                if len(cart_list)==0:
                    print("Your cart is empty. Please add the items")
                else:
                    print("=" * 30)
                    print("Products in your cart")
                    print("=" * 30)
                    for i in range(len(cart_list)):
                        print(i+1,".",cart_list[i][0],"- Rs.",cart_list[i][1])
                    remove=int(input("Which product do you want to remove:"))

                    if remove>=1 and remove<=len(cart_list):
                        removed_product=cart_list.pop(remove-1)
                        print(removed_product[0],"removed from cart")
                    else:
                        print("Invalid cart item!")
                    
                    

            elif menu_choice == 5:
                if len(cart_list)==0:
                    print("Your cart is empty")
                else:
                    """print("Products in your cart")
                    for i in range(len(cart_list)):
                        print(i+1,".",cart_list[i][0],"- Rs.",cart_list[i][1])"""

                    total=0
                    for i in range(len(cart_list)):
                        subtotal=cart_list[i][1]*cart_list[i][2]
                        print(i+1,".",cart_list[i][0],"- Rs.",cart_list[i][1],"quantity:",cart_list[i][2],"Subtotal=",subtotal)
                        total=total+cart_list[i][2]*cart_list[i][1]
                    print("="*30)
                    print("Total price - Rs.",total)
                    print("="*30)

                    confirm_purchase=input("Please confirm the purchase(yes/no):")
                    if confirm_purchase.lower()=='yes':
                        print("Your order is placed.")
                        cart_list.clear()
                    elif confirm_purchase.lower() == 'no':
                        print("Order cancelled. Your items are still in the cart.")
                    else:
                        print("Invalid! please enter yes or no")

                    
            elif menu_choice == 6:
                print("Thank you for visiting! Please visit again...")
                break

            else:
                print("Please select a valid option!")

        
    elif role==3:
        print("Thanks for visiting.")
        break

    else:
        print("Please select correct role")
