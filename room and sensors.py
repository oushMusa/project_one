def is_covered(room, sensors):

    from math import sin, cos, pi

    dept = 15

    L = [[sin(0.25*i*pi/dept),cos(0.25*i*pi/dept)] for i in range(dept)]

    def octos(x,y):

        return [[x,y],[-x,y],[x,-y],[-x,-y],[y,x],[-y,x],[y,-x],[-y,-x]]

    for sens_num in range(len(sensors)):

        sensor = sensors[sens_num]

        for pr in L:

            for oc in octos(pr[0],pr[1]):

                point = [oc[0]*sensor[2]+sensor[0], oc[1]*sensor[2]+sensor[1]]

                if point[0]>=0 and point[0]<=room[0] and point[1]>=0 and point[1]<=room[1]:

                    flag = 0

                    ss=0

                    for ss in range(len(sensors)):

                        if ss!=sens_num:

                            a = (sensors[ss][0] - point[0])**2+ (sensors[ss][1] - point[1])**2 <= sensors[ss][2]**2

                            flag+=a

                            if a:

                                break

                    if flag == 0:

                        return False

    return True



s = is_covered([200, 150], [[100, 75, 100], [0, 40, 60], [0, 110, 60], [200, 40, 60], [200, 110, 60]])
print(s)