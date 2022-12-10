import json
from modules.extra_tools import forEach
from prettytable import PrettyTable

user = lambda: json.load(open("test_user.json"))
loadData = lambda: json.load(open("data/products.json"))

def products():
    table = PrettyTable()
    data = loadData()
    table.field_names = json.load(open("data/options.json"))
    rows = []
    def get_rows(product):
        rows.append(list(product.values()))
    forEach(data, get_rows)
    table.add_rows(rows)
    table.align = "r"
    res = table.get_string(sortby="Price ($)")
    print(res)

def buy():
    product_id = int(input("Choose product ID for buy: "))
    products = loadData()
    old_user = user()
    try:
        purchase = products[product_id]
        if old_user["balance"] - purchase["price"] < 0:
            print("You need to more money")
        else:
            old_user["balance"] = old_user["balance"] - purchase["price"]
            old_user["purchases"] = old_user["purchases"] + [product_id]
            products = str(products).replace("'", '"')
            new_user_data = open("test_user.json", 'w')
            new_user_data.write(str(old_user).replace("'", '"'))
            print(f"You purchased {purchase['name']}")
    except IndexError:
        print(f"Product not found [{product_id}]")

def main():
    products()
    print(f"Your Balance: {user()['balance']}$")
    buy()
    main()

if __name__ == "__main__":
    main()