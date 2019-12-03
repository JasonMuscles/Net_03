import time


def task1():
    while True:
        print("---1---")
        time.sleep(0.5)
        yield


def task2():
    while True:
        print("---2---")
        time.sleep(0.5)
        yield


def main():
    t1 = task1()
    t2 = task2()
    # 先让t1运行一会儿，当t1遇到yield时，在放回到24行执行t2，当t2遇到
    # yield时再切换到t1，不断循环实现多任务的  协程
    while True:
        next(t1)
        next(t2)


if __name__ == '__main__':
    main()