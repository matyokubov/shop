import json

def add(product):
    products = json.load(open("data/products.json"))
    product = {"id": products[-1]["id"]+1}|product
    products.append(product)
    products = str(products).replace("'", '"')
    data = open("data/products.json", 'w')
    data.write(products)

# add({
#     "name": "ccc",
#     "weight": "x",
#     "description": "lorem ipsum",
#     "image": "path3",
#     "color": "black",
#     "price": 25
# })