import threading
import time
import random
def produce(items):
    forever=10
    i=1
    j=10
    for i in range(j):
        time.sleep(random.uniform(0,2))
        items.append(i)
        print("produced:"+str(i))
        i=i+1
def consume(items):
    j=10
    for i in range(j):
        time.sleep(random.uniform(0,2))
        if len(items)==0:
            print("consumed:no items")
            continue
        item=items.pop(0)
        print("consumed:"+str(item))
items=[]
producer=threading.Thread(target=produce,args=(items,))
consumer=threading.Thread(target=consume,args=(items,))
producer.start()
consumer.start()