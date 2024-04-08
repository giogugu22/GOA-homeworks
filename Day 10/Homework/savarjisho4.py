ticket_price=10
user_input=int(input("How many tickets do you want to buy? "))
if user_input<5 :
    print(user_input*10)
else :
    print(ticket_price*0.7*user_input)