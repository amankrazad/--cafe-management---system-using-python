#                       <---cafe mangement--->
name = input("enter ur name:\n")
print("<--welcome to azad cafe-->",name)
menu = {
    "latte":90,
    "mocha":79,
    "espresso":69,
    "doppio":57,
    "tea":37,
}
print("what u would like to order..")
print("our cafe menu is",menu)
total_order = 0
order = input("enter ur order:")
if order in menu:
    total_order += menu[order]
    print("ur order",order,"is confirmed")
    print("do u want to order something else")
    order2 = input()
    if order2 == "yes":
        print("what u want ur second order")
        order2 = input()
        total_order += menu[order2]
        if order2 in menu:
            print("ur second is confirmed",order2)
            print("ur total bill is",total_order)
    else:
        print("thank u\nur bill is",total_order)

else:
    print("sorry this order is not avaible in our cafe right now\nwould like to order something else")
