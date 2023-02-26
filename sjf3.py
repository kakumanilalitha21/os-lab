def avg(bt,n):
    tat=wt=[]
    i=0
    while i<n:
        ct=0
        j=0
        while j<=i:
               ct=ct+bt[j]
               j+=1
        tat.append(ct)
        i=i+1
    print("average turn around time",sum(tat)/n)
    i=0
    while i<n:
            wt[i]=tat[i]-bt[i]
            i+=1
    print("average waiting time",sum(wt)/n)
b=[]
n=int(input("enter no of process:"))
for i in range(n):
    x=int(input("enter burst time:"))
    b.append(x)
b.sort()
avg(b,n)