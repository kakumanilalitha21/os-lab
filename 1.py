def sjf_non_preemptive(jobs, n):
    # jobs: list of jobs to be executed
    # n: number of jobs
    jobs.sort(key = lambda x: x[1]) # sort jobs by arrival time
    current_time = 0
    wait_time = 0
    for i in range(n):
        if current_time < jobs[i][1]:
            current_time = jobs[i][1]
        wait_time += current_time - jobs[i][1]
        current_time += jobs[i][2] # add burst time
    avg_wait_time = wait_time / n
    return avg_wait_time
jobs=[['p1',0,5],['p2',1,6],['p3',2,9],['p4',3,8]]
n=4