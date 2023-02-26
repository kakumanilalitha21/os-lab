//round robin scheduling algorithm
def findWaitingTime(processes, n, bt,wt, quantum):
    rem_bt = [0] * n
    for i in range(n):
        rem_bt[i] = bt[i]
    t = 0
    while(1):
        done = True
        for i in range(n):
            if (rem_bt[i] > 0) :
                done = False # There is a pending process
                if (rem_bt[i] > quantum):
					t += quantum
					rem_bt[i] -= quantum 
				else:
					t = t + rem_bt[i]
					wt[i] = t - bt[i]
					
					rem_bt[i] = 0
				
		# If all processes are done
		if (done == True):
			break
			

def findTurnAroundTime(processes, n, bt, wt, tat):

	for i in range(n):
		tat[i] = bt[i] + wt[i]
def findavgTime(processes, n, bt, quantum):
	wt = [0] * n
	tat = [0] * n

	
	findWaitingTime(processes, n, bt,
						wt, quantum)

	
	findTurnAroundTime(processes, n, bt,
								wt, tat)

	
	print("Processes Burst Time	 Waiting",
					"Time Turn-Around Time")
	total_wt = 0
	total_tat = 0
	for i in range(n):

		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" ", i + 1, "\t\t", bt[i],
			"\t\t", wt[i], "\t\t", tat[i])

	print("\nAverage waiting time = %.5f "%(total_wt /n) )
	print("Average turn around time = %.5f "% (total_tat / n))
	

proc = []
n = int(input("enter no. of processes:"))


burst_time = []
for i in range(n):
    p=int(input("enter process id:"))
    proc.append(p)
    bt=int(input("enter burst time:"))
    burst_time.append(bt)

# Time quantum
quantum =int(input("enter time quantum:"))
findavgTime(proc, n, burst_time, quantum)