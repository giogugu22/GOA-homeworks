product_price=int(input("ნივთის ფასი: "))
budget=int(input("თქვენი ბიუჯეტი"))
if budget>=product_price :
    print("თანხა საკმარისია")
else :
    print(product_price-budget)

