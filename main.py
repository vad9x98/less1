def format_price(price):
    price = int(price)
    return 'Цена: ' + str(price) + ' руб.'
b = format_price(53)
print (b)