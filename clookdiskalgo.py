from matplotlib import pyplot as plt
def clookDiskScheduling(tracks, head):
    left = list()
    right = list()
    #left.insert(0,head)
    right.insert(0,head)
    seek_time = 0
    #x=tracks.copy()
    for i in range(len(tracks)):
        if tracks[i] <= head:
            left.append(tracks[i])
        else:
            right.append(tracks[i])

    left.sort()
    right.sort()

    for i in range(len(right)):
        seek_time += abs(head - right[i])
        head = right[i]
    x = sorted(left, reverse=False) + [0] + right

    for i in range(len(left)):
        seek_time += abs(head - left[i])
        head = left[i]
    x =right + [right[-1]]+sorted(left, reverse=False)
    print(seek_time)
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
    y = []
    for i in range(len(x)):
        y.append(-i)

    #print(list(zip(x, y)))
    plt.plot(x, y, color="green",
             markerfacecolor="blue",
             marker="o",
             markersize=5,
             linewidth=2,
             label="CLOOK")
    plt.ylim = (0, len(x))
    plt.xlim(0, 199)
    plt.yticks([])
    plt.title('CLOOK')
    plt.show()
tracks = [82,170,43,140,24,16,190]
head = 50
clookDiskScheduling(tracks, head)
