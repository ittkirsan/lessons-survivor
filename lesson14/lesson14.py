


def Unmanned(L, N, track):
    count = 1

    for i in range(1, L):
        kl = 1

        for j in range(N):
            if track[j][0] == i:
                red_green = track[j][1] + track[j][2]
                zikl = count//red_green
                m = count - (zikl*red_green)
                if m >= track[j][1]:
                    kl = 1
                else:
                    kl = 1 + track[j][1]-m
        count += kl
    return count
