
def create_num(all_num):

    # a = 0
    # b = 0
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:

        # print(a)
        yield a  # 如果函数中有yield语句，那么这个就不是一个函数而是一个生成器的模板

        a, b = b, a + b
        current_num += 1
    return "ok！！！"


# 如果在调用creat_num的时候，发现这个函数中有yield，
# 不是在调用函数，而是创建一个生成器对象

obj2 = create_num(2)

while True:
    try:
        ret = next(obj2)
        print(ret)
    except Exception as ret:
        print(ret.value)
        break
# for num in obj:
# print(num)
