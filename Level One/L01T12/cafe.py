# L0T12 : Data Structures - Lists and Dictionaries


# INSTRUCTUCTION: Image you own a Cafe! Café Bufé
#                  Create list  of at least 4 items
#                  Create dictionary called stock which will contain stock value for each item on menu
#                  Create another dictionary called price which will contain prices for each item on menu
#                  Calc total_stock


total_stock = 0
menu = [  # create list of four items
    (1, "Boerewors Roll"),
    (2, "Sweetie Pie"),
    (3, "Danish Pastry"),
    (4, "CupOCoffee"),
]

menu_dist = dict(menu)  # use dict() to create a dictionary from menu list
stock = {1: 3, 2: 42, 3: 23, 4: 10}  # create dictionary for amount of stock

price = {1: 21, 2: 9.99, 3: 14.99, 4: 12}  # create dictionary for price of each item


for key in menu_dist:  # use for loop with key as counter and menu_dist as the iterable
    item_value = (
        stock[key] * price[key]
    )  # create a item_value var to times the value at KEY position of stock and price
    total_stock += item_value   # Increment the total_stock value with item_value

print(f"R {total_stock:,.2f}")  # Print the total_stock value, with some formatting to output as Rands
