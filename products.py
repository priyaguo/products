#讀取檔案
#split 切割
products = []
with open('products.csv', 'r') as f:
    for line in f:
        if '商品,價格' in line:
            continue  #繼續for迴圈
        name, price = line.strip().split(',')
        products.append([name, price])
print(products)

#二維清單
products = []
while True:
    name = input('請輸入商品名稱:')
    if name == 'q':
        break
    price = str(input('請輸入商品價格:'))
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

# r → read 讀取
# w → write 寫入
# open 打開檔案
# f.write →寫入檔案
with open('products.csv','w',encoding = 'BIG5') as f:
    f.write('商品,價格' + '\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')

