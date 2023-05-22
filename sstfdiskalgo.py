from matplotlib import pyplot as plt
def sstfDiskScheduling(sequence, head):
    plt.rcParams['xtick.bottom']=plt.rcParams['xtick.labelbottom']=False
    plt.rcParams['xtick.top']=plt.rcParams['xtick.labeltop']=True
    temp=sequence.copy()
    temp.insert(0,head)
    size=len(temp)
    x=temp
    y=[]
    headmovement=0
    seek_time=0
    for i in range(0,size):
        y.append(-i)
        if i != size-1:
           while len(sequence) != 0:
              min_track = sequence[0]
        # finding track with the lowest seek time
              for j in range(len(sequence)):

                track_seek_time = abs(sequence[j] - head)
                if min_track - head > track_seek_time:
                    min_track = sequence[j]

              seek_time += abs(head - min_track)
              head = min_track
              tracks.remove(min_track)
              headmovement+=min_track
    string1='head movement='+str(headmovement)
    string2=str(temp)
    plt.plot(x,y,color="green",markerfacecolor="blue",marker="o",markersize=6,linewidth=2,label="fcfs")
    plt.ylim=(0,size)
    plt.yticks=([])
    plt.xlim=(0,199)
    plt.title("sstf")
    plt.show()
    seek_time = 0
    while len(sequence) != 0:
        min_track = sequence[0]
        # finding track with the lowest seek time
        for j in range(len(sequence)):

            track_seek_time = abs(sequence[j] - head)
            if min_track - head > track_seek_time:
                min_track = sequence[j]

        seek_time += abs(head - min_track)
        head = min_track
        tracks.remove(min_track)
    print(seek_time)


if __name__ == '__main__':
    tracks = [82,170,43,140,24,16,190]
    head = 50
    print(sstfDiskScheduling(tracks, head))

