import json


def write_order_to_json(item, quantity, price, buyer, date):

    order_data_dict = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }

    with open('orders.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        data['orders'].append(order_data_dict)

    with open('orders.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, sort_keys=True, indent=4)


order_data_01 = {
    "item": "good 01",
    "quantity": 5,
    "price_rub": 15200,
    "buyer": "client01",
    "date": "2021-05-01"
}

order_data_02 = {
    "item": "good 02",
    "quantity": 10,
    "price_rub": 30400,
    "buyer": "client02",
    "date": "2021-05-02"
}

write_order_to_json(*list(order_data_01.values()))
write_order_to_json(*list(order_data_02.values()))
