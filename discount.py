def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent/100)
        final_price = price - discount_amount
        return final_price
    else :
        return price 
    
price = float(input("Enter the original price: "))
discount_percent = float (input("Enter discount percent: "))

final_price = calculate_discount(price, discount_percent)

if final_price == price:
  print("no discount the price is :" , final_price)
else:
    print("price after discount is :", final_price)