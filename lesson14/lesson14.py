

def Unmanned(L, N, track):
    time_car_to_reach_end_road = 1

    for i in range(1, L):
        kl = 1

        for j in range(N):
            if track[j][0] == i:
                red_green = track[j][1] + track[j][2]
                zikl = time_car_to_reach_end_road//red_green
                m = time_car_to_reach_end_road - (zikl*red_green)
                if m >= track[j][1]:
                    kl = 1
                else:
                    kl = 1 + track[j][1]-m
        time_car_to_reach_end_road += kl
    return time_car_to_reach_end_road
