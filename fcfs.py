//first come first serve
nprocess=int(input("enter no of process running in background:"))
prolist=[]
for i in range(nprocess):
    process=input("enter process name:")
    prolist.append(process)
print("processes:",prolist)
btime=[]
for i in range(nprocess):
    time=int(input("enter burst time:"))
    btime.append(time)
print("burst times:",btime)
at=[]
for i in range(nprocess):
    
  a=int(input("enter arrival time:"))
  at.append(a)
ct=[]
x=btime[0]
ct.append(x)
for i in range(1,nprocess):
        x=x+btime[i]
        ct.append(x)
print("completion time:",ct)
tatime=[]
for i in range(nprocess):
    tatime.append(ct[i]-at[i])
print("turn around time:",tatime)
wtime=[]
for i in range(nprocess):
    wtime.append(tatime[i]-btime[i])
print("waiting time:",wtime)
sum=0
for i in range(nprocess):
    sum=sum+tatime[i]
avgtat=sum/nprocess
print("avg tat:",avgtat)
sum2=0
for i in range(nprocess):
    sum2=sum2+wtime[i]
avgwt=sum2/nprocess
print("avgwt:",avgwt)
