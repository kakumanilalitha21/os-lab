from matplotlib import pyplot as plt 
def fcfs(sequence,head):
    sequence1=sequence.copy()
    sequence1.insert(0,head)
    plt.rcParams['xtick.bottom']=plt.rcParams['xtick.labelbottom']=False
    plt.rcParams['xtick.top']=plt.rcParams['xtick.labeltop']=True
    temp=sequence.copy()
    temp.insert(0,head)
    size=len(temp)
    x=temp
    y=[]
    headmovement=0
    for i in range(0,size):
        y.append(-i)
        if i != size-1:
            headmovement+=abs(temp[i]-temp[i+1])
    string1='head movement='+str(headmovement)
    string2=str(temp)
    plt.plot(x,y,color="green",markerfacecolor="blue",marker="o",markersize=6,linewidth=2,label="fcfs")
    plt.ylim=(0,size)
    plt.yticks=([])
    plt.xlim=(0,199)
    plt.title("fcfs")
    plt.show()
    seektime=0
    for i in range(len(sequence)):
        seektime+=abs(sequence1[i]-sequence1[i+1])
    return seektime
if __name__=="__main__":
    
    sequence=list(map(int,input("enter the sequence:").strip().split()))
    head=int(input("enter the current position of head:"))
    print("seek time:",fcfs(sequence,head))

