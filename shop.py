# Ronny Hayun, AM
# Shopping cart system 10/15/2026

import datetime

class Solution(object):
    
    # Function 1: Display all products and their prices
    def display_products(self, products, prices):
        """
        :type products: List[str]
        :type prices: List[float]
        :rtype: None
        """
        print("")
        print("========== AVAILABLE PRODUCTS ==========")
        print("")
        
        # Loop through the products list using numbers
        for i in range(len(products)):
            # Print the product number, name, and price
            print(str(i + 1) + ". " + products[i] + " $" + str(prices[i]))
            
        print("")

    # Function 2: Add a product to the cart (or add to quantity if already inside)
    def add_product(self, products, prices, shopping_cart, quantities):
        """
        :type products: List[str]
        :type prices: List[float]
        :type shopping_cart: List[str]
        :type quantities: List[int]
        :rtype: None
        """
        print("")
        print("========== AVAILABLE PRODUCTS ==========")
        print("")
        
        # Display the product list so the user knows what to choose
        for i in range(len(products)):
            print(str(i + 1) + ". " + products[i] + " $" + str(prices[i]))
            
        print("")
        user_choice = int(input("Enter product number: "))
        
        # Use a while loop to validate that the selection is between 1 and 6
        while user_choice < 1 or user_choice > 6:
            print("")
            print("Invalid product!")
            user_choice = int(input("Please choose a number between 1 and 6: "))
            
        # Match user choice to list index
        selected_index = user_choice - 1
        product_name = products[selected_index]
        
        # Check if the product is already in our cart list
        if product_name in shopping_cart:
            # Find which position the item is at in the cart
            cart_index = shopping_cart.index(product_name)
            # Add 1 to the matching quantity
            quantities[cart_index] = quantities[cart_index] + 1
            print("")
            print(product_name + " quantity increased to " + str(quantities[cart_index]) + "!")
        else:
            # Add new item name to cart list
            shopping_cart.append(product_name)
            # Add 1 to quantities list
            quantities.append(1)
            print("")
            print(product_name + " was added to your cart!")

    # Function 3: Remove a product from the cart
    def remove_product(self, shopping_cart, quantities):
        """
        :type shopping_cart: List[str]
        :type quantities: List[int]
        :rtype: None
        """
        # Check if cart is empty first
        if len(shopping_cart) == 0:
            print("")
            print("Your shopping cart is empty!")
            print("There is nothing to remove.")
            return
            
        print("")
        print("========== YOUR SHOPPING CART ==========")
        print("")
        
        # Display all items currently inside the shopping cart
        for i in range(len(shopping_cart)):
            print(str(i + 1) + ". " + shopping_cart[i] + " - Quantity: " + str(quantities[i]))
            
        print("")
        remove_choice = int(input("Which item would you like to remove? Enter item number: "))
        
        # Validate that choice is within valid range of current cart size
        while remove_choice < 1 or remove_choice > len(shopping_cart):
            print("")
            print("That item does not exist in your cart!")
            remove_choice = int(input("Please enter a valid item number: "))
            
        cart_index = remove_choice - 1
        product_name = shopping_cart[cart_index]
        
        # If quantity is greater than 1, just subtract 1 from quantity
        if quantities[cart_index] > 1:
            quantities[cart_index] = quantities[cart_index] - 1
            print("")
            print("One " + product_name + " was removed!")
            print(product_name + " quantity is now " + str(quantities[cart_index]) + ".")
        else:
            # If quantity is 1, completely remove item from both lists
            shopping_cart.pop(cart_index)
            quantities.pop(cart_index)
            print("")
            print(product_name + " was removed from your cart!")

    # Function 4: Display contents of cart and quantities
    def display_cart(self, products, prices, shopping_cart, quantities):
        """
        :type products: List[str]
        :type prices: List[float]
        :type shopping_cart: List[str]
        :type quantities: List[int]
        :rtype: None
        """
        # Check if cart is empty
        if len(shopping_cart) == 0:
            print("")
            print("Your shopping cart is empty!")
            return
            
        print("")
        print("========== YOUR SHOPPING CART ==========")
        print("")
        
        total_items = 0
        
        # Loop through cart and print information
        for i in range(len(shopping_cart)):
            item_name = shopping_cart[i]
            item_quantity = quantities[i]
            
            # Find matching price from products list
            product_index = products.index(item_name)
            item_price = prices[product_index]
            item_total = item_price * item_quantity
            
            # Add to total item counter
            total_items = total_items + item_quantity
            
            print(str(i + 1) + ". " + item_name + " - $" + str(item_price) + " x " + str(item_quantity) + " = $" + str(item_total))
            
        print("")
        print("Total Items: " + str(total_items))

    # Function 5: Calculate total cost of items in cart
    def calculate_total(self, products, prices, shopping_cart, quantities):
        """
        :type products: List[str]
        :type prices: List[float]
        :type shopping_cart: List[str]
        :type quantities: List[int]
        :rtype: float
        """
        subtotal = 0.0
        
        # Loop through cart items to sum total price
        for i in range(len(shopping_cart)):
            item_name = shopping_cart[i]
            item_quantity = quantities[i]
            
            # Find price from inventory
            product_index = products.index(item_name)
            item_price = prices[product_index]
            
            # Multiply price by quantity and add to subtotal
            subtotal = subtotal + (item_price * item_quantity)
            
        return subtotal

    # Function 6: Calculate discount percentage
    def calculate_discount(self, subtotal):
        """
        :type subtotal: float
        :rtype: float
        """
        # Determine discount based on subtotal amount
        if subtotal >= 40.0:
            return 0.15
        elif subtotal >= 20.0:
            return 0.10
        elif subtotal >= 10.0:
            return 0.05
        else:
            return 0.00

    # Function 7: Main game loop
    def shoppingCartSystem(self):
        """
        :type: None
        :rtype: None
        """
        # Product and price inventory lists
        products = ["Chips", "Soda", "Candy", "Cookies", "Water", "Sandwich"]
        prices = [2.0, 2.5, 1.5, 3.0, 1.0, 5.0]
        
        # Empty user cart lists
        shopping_cart = []
        quantities = []
        
        # Boolean control variable for main menu loop
        keep_shopping = True
        
        # Main menu loop
        while keep_shopping == True:
            
            # Display menu options
            print("")
            print("========== SMART SHOPPING CART ==========")
            print("")
            print("1. View Available Products")
            print("2. Add Product to Cart")
            print("3. Remove Product from Cart")
            print("4. View Shopping Cart")
            print("5. View Current Total")
            print("6. Checkout")
            print("")
            
            user_choice = int(input("Enter your choice: "))
            
            # Validate menu choice using while loop
            while user_choice < 1 or user_choice > 6:
                print("")
                print("Invalid option!")
                user_choice = int(input("Please enter a choice between 1 and 6: "))
                
            # Option 1: View Products
            if user_choice == 1:
                self.display_products(products, prices)
                
            # Option 2: Add Product
            elif user_choice == 2:
                self.add_product(products, prices, shopping_cart, quantities)
                
            # Option 3: Remove Product
            elif user_choice == 3:
                self.remove_product(shopping_cart, quantities)
                
            # Option 4: View Cart
            elif user_choice == 4:
                self.display_cart(products, prices, shopping_cart, quantities)
                
            # Option 5: View Total
            elif user_choice == 5:
                if len(shopping_cart) == 0:
                    print("")
                    print("Your shopping cart is empty!")
                else:
                    subtotal = self.calculate_total(products, prices, shopping_cart, quantities)
                    print("")
                    print("========== CURRENT TOTAL ==========")
                    print("")
                    for i in range(len(shopping_cart)):
                        item_name = shopping_cart[i]
                        item_quantity = quantities[i]
                        product_index = products.index(item_name)
                        item_price = prices[product_index]
                        item_total = item_price * item_quantity
                        print(item_name + " x " + str(item_quantity) + " = $" + str(item_total))
                        
                    print("")
                    print("Subtotal: $" + str(subtotal))
                    
            # Option 6: Checkout
            elif user_choice == 6:
                if len(shopping_cart) == 0:
                    print("")
                    print("Your shopping cart is empty!")
                    print("You cannot check out with an empty cart.")
                else:
                    # Calculate final math values
                    subtotal = self.calculate_total(products, prices, shopping_cart, quantities)
                    discount_rate = self.calculate_discount(subtotal)
                    amount_saved = subtotal * discount_rate
                    final_total = subtotal - amount_saved
                    
                    # Get today's date simply using datetime.date.today()
                    today_date = datetime.date.today()
                    
                    print("")
                    print("========== RECEIPT ==========")
                    print("")
                    print("Date: " + str(today_date))
                    print("")
                    
                    for i in range(len(shopping_cart)):
                        item_name = shopping_cart[i]
                        item_quantity = quantities[i]
                        product_index = products.index(item_name)
                        item_price = prices[product_index]
                        item_total = item_price * item_quantity
                        print(item_name + " x " + str(item_quantity) + "   $" + str(item_total))
                        
                    print("")
                    print("Subtotal:     $" + str(subtotal))
                    print("Discount:     " + str(int(discount_rate * 100)) + "%")
                    print("Amount Saved: $" + str(amount_saved))
                    print("")
                    print("TOTAL:        $" + str(final_total))
                    print("")
                    print("Thank you for shopping!")
                    
                    # Stop loop when finished
                    keep_shopping = False


# Run the shopping cart program
cart_app = Solution()
cart_app.shoppingCartSystem()