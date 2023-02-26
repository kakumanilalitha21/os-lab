n=int(input("enter no of processes:"))
print("enter processid bt and priority:")
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(n):
    for j in range(i+1,n):
        if l[i][2]>l[j][2]:
            l[i],l[j]=l[j],l[i]    
ct=0
for i in range(n):
    ct+=l[i][1]
    l[i].append(ct)
tat,wt=0,0
print("pid bt p ct tat wt")
for i in range(n):
    print(l[i][0]," ",l[i][1]," ",l[i][2]," ",l[i][3]," ",l[i][3]," ",l[i][3]-l[i][1])
ttat=0
twt=0
for i in range(n):
    ttat+=l[i][3]
    twt+=l[i][3]-l[i][1]
print("average tat:",ttat/n)
print("average wt:",twt/n)
    
    
    
    
    
    
    
    