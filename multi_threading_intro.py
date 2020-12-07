import time
import threading


def cube(arr):
    for i in arr:
        time.sleep(1)
        print(i*i*i)


def sq(arr):
    for i in arr:
        time.sleep(1)
        print(i*i)


if __name__ == "__main__":
    arr = [2,3,8,9]
    t = time.time()
    # cube(arr)
    # sq(arr)
    t1 = threading.Thread(target=sq, args=(arr,))
    t2 = threading.Thread(target=cube, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    print("done in : ",time.time()-t)
