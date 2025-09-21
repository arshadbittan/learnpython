def my_function():
  print("Hello from a function")

my_function()


#
#def sum(a,b):

    #print(a+b)
#c=int(input("enter a"))
#d=int(input("enter b"))
#sum(c,d)

#def sum_values(a, b):
    #result = a + b
    #print(result)
    #return result
    #print(result)

# Calling the function for testing
#print(sum_values(1, 2))

# === Food Order System ===

# Show Menu
#def show_menu():
   #print("1. Pizza  - $10")
    #print("2. Burger - $5")
    #print("3. Soda   - $2")


# Get price based on item
#def get_price(item):
 #   if item == 1:
  #      return 10
   # elif item == 2:
    #    return 5
    #elif item == 3:
     #   return 2
    #else:
     #   return 0   # invalid choice


# Take one order
#def take_order():
 #   show_menu()
  #  choice = int(input("Enter item number: "))
   # qty = int(input("Enter quantity: "))
    #price = get_price(choice) * qty
    #print(f"Added to cart: Item {choice}, Qty {qty}, Subtotal ${price}")
    #return price


# Checkout process
#def checkout():
 #   total = 0
  #  while True:
   #     total += take_order()
    #    more = input("Add more items? (y/n): ")
     #   if more.lower() != "y":
      #      break
    #return total


# Main function
#def main():
 #   print("Welcome to Food Order System 🍽️")
  # print("\n=== Final Bill ===")
   # print("Your total bill is: $", total_amount)
   # print("Thank you for your order! 🙌")


# Run the program
#main()

total_balance = 0
def bank():
    global total_balance
    print("\n=== Bank ===")
    print("press 1 for deposite")
    print("press 2 withdraw")
    print("press 2 for check balance")
    if input(" ") == "1":
        dep_amount= int(input("please enter amount"))
        total_balance= total_balance + dep_amount
        print("total balance is:",total_balance)

bank()