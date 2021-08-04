# Создайте список и выведите на экран всех покупателей, а для каждого покупателя подсчитайте общее количество приобретенных им товаров и их стоимость.
from typing import Optional

unnecessary_items = ['Покупатель', 'Товар', 'Количество', 'Стоимость']
full_text = []
with_int_text = []

with open("Homework.txt", "r", encoding="utf8") as customers:
    for attr in customers:
        split_attrs = attr.split()
        if len(split_attrs):
            full_text.append(split_attrs)

attrs_only_list = [row for row in full_text if row != unnecessary_items]
for elem in attrs_only_list:
    elem[2] = int(elem[2])
    elem[3] = int(elem[3])
    with_int_text.append(elem)


users = {}
for row in with_int_text:
    if row[0] in users:
        users[row[0]]["products_quantity"] += row[2]
        users[row[0]]["total_price"] += row[3]
    else:
        users[row[0]] = {
            "products_bought": row[2],
            "total_price": row[3],
            }
    return users


def get_products_info(data: list) -> dict:
    result = {}
    for row in data:
        if row[1] in result:
            result[row[1]]["bought_count"] += row[2]
            result[row[1]]["total_price"] += row[3]
        else:
            # Otherwise set initial values
            result[row[1]] = {
                "bought_count": row[2],
                "total_price": row[3],
            }
    return result


def main():
    data = load_data_from_file()

    user_stats = get_user_info(data)
    print("User stats: ", user_stats)

    product_stats = get_products_info(data)
    print("Product stats: ", product_stats)


if __name__ == "__main__":
    main()
