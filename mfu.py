from collections import defaultdict
def mfu(pages,capacity):
    memory=[]
    pagefaults=0
    freq=defaultdict(int)
    for page in pages:
        if page not in memory:
            pagefaults+=1
            if len(memory)<capacity:
                memory.append(page)
                freq[page]=1
            else:
                lfupage=max(memory,key=lambda p:freq[p])
                memory.remove(lfupage)
                memory.append(page)
                freq[page]=1
        else:
            freq[page]+=1
    return pagefaults
pages=list(map(int,input("enter page sequence:").strip().split()))
capacity=int(input("enter capacity:"))
print("pagefaults:",mfu(pages,capacity))
