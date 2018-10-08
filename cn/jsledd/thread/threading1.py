import time
import threading


def loop1(in1):
    print('Start loop 1 at :', time.ctime())
    time.sleep(4)
    print('End loop 1 at:', time.ctime())


def loop2(in1, in2):
    print('Start loop 2 at :', time.ctime())
    time.sleep(2)
    print('End loop 2 at:', time.ctime())


def main():
    print("main Starting at:", time.ctime())

    t1 = threading.Thread(target=loop1, args=("thread1",))
    # 社会守护线程的方法，必须在start之前设置，否则无效
    t1.setDaemon(True)
    # t1.daemon = True
    t1.start()
    t2 = threading.Thread(target=loop2, args=("thread2", "thread3"))
    t2.start()
    t1.join()  # 等待子线程
    t2.join()
    print("All done at:", time.ctime())


if __name__ == "__main__":
    main()
