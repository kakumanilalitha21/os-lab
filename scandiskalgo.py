from matplotlib import pyplot as plt


def scanDiskScheduling(tracks, head, direction):
    left = list()
    right = list()
    left.insert(0,head)
    right.insert(0,head)
    seek_time = 0

    for i in range(len(tracks)):
        if tracks[i] <= head:
            left.append(tracks[i])
        else:
            right.append(tracks[i])

    left.sort()
    right.sort()

    if not direction:
        for i in range(len(left)-1, -1, -1):
            seek_time += abs(head - left[i])
            head = left[i]
        seek_time += abs(head - 0)
        head = 0

        for i in range(len(right)):
            seek_time += abs(head - right[i])
            head = right[i]
        x = sorted(left, reverse=True) + [0] + right

    else:
        for i in range(len(right)):
            seek_time += abs(head - right[i])
            head = right[i]
        seek_time += abs(head - 199)
        head = 199

        for i in range(len(left)-1, -1, -1):
            seek_time += abs(head - left[i])
            head = left[i]

        x =right + [199] + sorted(left, reverse=True)
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
             label="SCAN")
    plt.ylim = (0, len(x))
    plt.xlim(0, 199)
    plt.yticks([])
    plt.title('SCAN')
    plt.show()


if __name__ == '__main__':
    tracks = [82,170,43,140,24,16,190]

    head =50
    scanDiskScheduling(tracks, head, 1)
