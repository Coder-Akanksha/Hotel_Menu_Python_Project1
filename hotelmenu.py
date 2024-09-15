#define the menu of restaurant
menu = {
    'pizza':40,
    'pasta':50,
    'burgur':60,
    'salad':70,
    'coffee':80,

}
#Greet
print("Welcome to python retaurant")
print("pizza:Rs40\n pasta:Rs50\n burgur:Rs60\n salad:Rs70\n coffee:Rs80")

order_total=0
#80+70=150

item_1=input("Enter the name of item you want to order=")
if item_1 in menu:
    order_total+= menu[item_1] #0+50
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item{item_1} is not available yet")
    another_order = input("do you want to add another item ? (Yes?No)")
    if another_order =="Yes":
        item_2 = input("Enter the name of second item = ")
        if item_2 in menu:
            order_total+= menu[item_2]
            print(f"Item{item_2}has been added to order")
        else:
            print(f"ordered item{item_2}is not available!")

            print(f"The totale amount of item is to pay is{order_total}")