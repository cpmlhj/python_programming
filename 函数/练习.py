# 商品
products = [
    [1000, 'iphone', 'phone', 12000],
    [1001, 'ipad', 'pad', 9000],
    [1002, 'macbook', 'laptap', 20000],
]

# 购物车 product_id product_number
cart = {1000: 5, 1001: 2}


#
# for item in cart:
#     print(item, cart[item])
#     for product in products:
#         if product[0] == item:
#             print(product[1])

def idtoname(product_id):
    """
    product id to product name
    :param product_id:
    :return:
    """
    for product in products:
        if product[0] == product_id:
            return product[1]
            break


def idtoprict(prodct_id):
    """
    prodcut_id to product_price
    :param prodct_id:
    :return:
    """
    for product in products:
        if product[0] == prodct_id:
            print(product[3])
            return product[3]
            break;


def add_product(product_id, add_num):
    target = cart.get(product_id)
    target = target if target else 0 + add_num
    cart[product_id] = target


def del_product(product_id):
    if product_id in cart.keys():
        cart[product_id] -= 1
        if cart[product_id] == 0:
            cart.pop(product_id)
    print(cart)


# add_product(1003, 5)
del_product(1000)


def showcart():
    """
    展示购物车的商品
    :return:
    """
    total_money = 0
    for item in cart:
        print(f"购买商品{idtoname(item)}的数量为{cart[item]}")
        total_money += idtoprict(item) * cart[item]
    print(f"总费用是：{total_money}")


# showcart()


# 高阶函数

def self_reduce(arr1, arr2):
    def count_num(idx):
        return arr1[idx] + arr2[idx]

    new_list = [x for x in map(count_num, range(len(arr1)))]
    print(new_list)


arr1 = [1, 3, 5, 7, 9]
arr2 = [2, 4, 6, 8, 10]
self_reduce(arr1, arr2)
