#二維清單
products = []
while True:
    name = input('請輸入商品名稱:')
    if name == 'q':
        break
    price = int(input('請輸入商品價格:'))
    #p = []
    #p.append(name)
    #p.append(price)
    #products.append(p)
    products.append([name, price])
print(products)

for p in products:
    print(p[0],'的價格是',p[1])
# print(products[0][0])
# print(products[0][1])
# print(products[1][0])
# print(products[1][1])