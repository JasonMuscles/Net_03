
def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        ret = yield a
        # 可以理解为：先yield a：ret = next(obj) ||后ret ：ret = obj.send("可以传值")
        # send尽可能不要用在next前
        print("》》》ret》》》", ret)
        a, b = b, a + b
        current_num += 1


obj = create_num(10)

ret = next(obj)
print(ret)

ret = obj.send("可以传值")
print(ret)
