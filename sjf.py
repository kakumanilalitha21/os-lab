nprocess=int(input("enter no of processes:"))
prolist=[]
for i in range(nprocess):
    ele=input("enter process name:")
    prolist.append(ele)
bt=[]
for i in range(nprocess):
    t=int(input("enter burst time:"))
    bt.append(t)
at=[]
for i in range(nprocess):
    a=int(input("enter arrival time:"))
    at.append(a)
ct=[]    
for i in range(nprocess):
    for j in range(nprocess):
        if at[i]<at[j]:
            at.sort()
            if bt[i]<bt[j]:
                bt.sort()
x=0           
for i in range(nprocess):
    x=x+bt[i]
    ct.append(x)    
print("ct:",ct)
tat=[]
for i in range(nprocess):
    tat.append(ct[i]-at[i])
print("tat:",tat)
wt=[]
for i in range(nprocess):
    wt.append(tat[i]-bt[i])
print("wt:",wt)
sum=0
sum2=0
for i in range(nprocess):
    sum=sum+tat[i]
    sum2=sum2+wt[i]
print("avgtat:",sum/nprocess)
print("avgwt:",sum2/nprocess)
    

    
    
    
    
    
    