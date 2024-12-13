Menu={"coffe":40,'pasta':50,
      'pizza':60,'burger':55}


print("HEllo, here's the menu card\nCoffe: Rs40\nPasta: Rs50\nPizza : Rs60\nBurger: Rs55")


#TAking oreder/ Managing Workflow

while True:
    OrderedItem= input("Which item you want to order")
    FinalCost=0
    if OrderedItem.lower() == "done":
        break
    if OrderedItem.lower() in Menu: # accepts all input from user by converting into lowercase
        print(f'Your order {OrderedItem} is on the way\n')
        FinalCost+=Menu[OrderedItem.lower()]
        print(f"Your bill is {FinalCost} RS")
    else:
        print("Sorry, your ordered item isn't in our Menu Card")

    Ask_Another_Ordered_Item= input(f"Anything else you want to order except {OrderedItem} (YES/NO)")
    if Ask_Another_Ordered_Item.lower() == "yes":
        Another_Item= input("Which another item you want to have! :)")
        if Another_Item in Menu:
            print(f'Your {Another_Item} item is on the way :)')
            print(f"Your bill is {FinalCost} RS")
        else:
            print("Please order something from our Menu")

    else:
         print(f"Thank You, Your Final bill is {FinalCost}\n Press Done to Leave")





