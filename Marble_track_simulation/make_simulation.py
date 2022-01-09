#create xyz points and writes it to "looping_points.txt"
import math
import numpy as np
import matplotlib.pyplot as plt
from path3d import *
"""path3d is a given file/library from my Uni (UCL) and is not my own work."""


def main():
    """creates a class which returns a string containing all the points 
    of the track. Then, the program writes these points into the 
    looping_points.txt tsv file, which will be used by other programs
    to create and analyse the track."""
    
    # a = input("Give point A in this format : X Y Z : ").split()
    # b = input("Give point B in this format : X, Y, Z : ").split()
    # print (a,b)
    # a = [2, 3, 0]
    #   b = [4, 4, 3]
    # v = [b[0] - a[0], b[1] - a[1], b[2] - a[2]]

    class Generate_points:

        def __init__(self, a):
            self.a = a
            self.str = ""
            self.bool1 = False
            self.v = [0, 0, 0]

        def g_p_line(self, b, p_index = 10):
            """generates p_index points between 
            point self.a and b, which are points"""
            #make every element of a, b and v into float
            for i in range(3):
                self.a[i] = float(self.a[i])
                # print(a[i])
                b[i] = float(b[i])
                # print(v[i])
            # create v and put into float
            self.v = [b[0] - self.a[0], b[1] - self.a[1], b[2] - self.a[2]]
            for i in range(3):
                self.v[i] = float(self.v[i])
            # add every point to self.str and also little catchy sentence
            # number of points index
            # p_index = 10
            # already created point n and bool
            if self.bool1 == False:
                n = 0
            else:
                n = 1
            # self.str += f" Points in a straight line between {self.a} and {b}\n"
            for i in range(n, p_index + 1):
                # print(i)
                round_of_points = (f"   {format(round(self.a[0] + 1/p_index*i * self.v[0], 4), '.5f')}    {format(round(self.a[1] + 1/p_index*i * self.v[1], 4), '.5f')}    {format(round(self.a[2] + 1/p_index*i * self.v[2], 4), '.5f')}\n")
                self.str += round_of_points
            
            # set bool 1 to True so the two same points won't be printed
            self.bool1 = True
            # make the last point into the first point
            self.a = b

            # print(f"{a}\n{b}\n{v}")
        

        def g_p_half_circle(self, d, r):
            """generates half circle points in the x and y plan.
            perpendicular to the vector, d argument is direction left or right
            and r is the cercle's diameter"""
            # determine the perpendicular vector
            # print(d)
            if d.lower() in ["r", "right", "d", "droite"]:
                # print("YES RIGHT")
                u = [self.v[1], -self.v[0], 0]
                # print(u)
            if d.lower() in ["l", "left", "g", "gauche"]:
                # print("YES LEFT")
                u = [-self.v[1], self.v[0], 0]
            
            # create the end point of the circle
            k = r / (math.sqrt(u[0]**2 + u[1]**2))
            # end_point = [float(format(round(self.a[0] + k * u[0], 3), '.5f')), float(format(round(self.a[1] + k * u[1], 3), '.5f')), float(format(self.a[2], '.5f'))]
            end_point = [float(self.a[0] + k * u[0]), float(self.a[1] + k * u[1]), float(self.a[2])]

            # create the middle point between end_point and a
            middle_point = []
            for i in range(3):
                # print(f"a point : {self.a} \n end point : {end_point}")
                middle_point.append(((self.a[i]) + (end_point[i])) / 2)
                # print(f"Middle point : {middle_point[i]}")
            # self.str += f"   {middle_point[0]}    {middle_point[1]}    {middle_point[2]}\n"
            # self.str += f"   {end_point[0]}    {end_point[1]}    {end_point[2]}"

            # create the circle point
            k1 = (r * 0.5) / (math.sqrt(self.v[0]**2 + self.v[1]**2))
            # circle_point = []
            # for i in range(2):
            #     circle_point.append(format(round(middle_point[i] + k1 * self.v[i], 3), '.5f'))
            circle_point = [format(round(middle_point[0] + k1 * self.v[0], 3), '.5f'), format(round(middle_point[1] + k1 * self.v[1], 3), '.5f'), format(self.a[2], '.5f')]
            # self.str += f"   {middle_point[0]}    {middle_point[1]}    {middle_point[2]}\n"
            self.str += f"   {circle_point[0]}    {circle_point[1]}    {circle_point[2]}\n"
            self.str += f"   {format(end_point[0], '.5f')}    {format(end_point[1], '.5f')}    {format(end_point[2], '.5f')}\n"
            self.a = [float(format(end_point[0], '.5f')), float(format(end_point[1], '.5f')), float(format(end_point[2], '.5f'))]
            self.v = [-self.v[0], -self.v[1], 0]
            # print(self.v)
            # print("yoyoyo", self.a, self.v)
    

        def g_p_vector(self, r, p_index = 5, z_dir = 0):
            """create p_index points following vector, r is the wanted length
            and z_dir is if you want to change vector's z component slightly"""
            
            k = r / (math.sqrt(self.v[0]**2 + self.v[1]**2 + (self.v[2])**2))
            
            # print("Points from vector : ")
            point_a = self.a
            for i in range(1, p_index + 1):
                round_of_points = f"   {format(round(self.a[0] + i/p_index * k * self.v[0], 3), '.5f')}    {format(round(self.a[1] + i/p_index * k * self.v[1], 3), '.5f')}    {format(round(self.a[2] + i/p_index * k * self.v[2] + i/p_index * z_dir, 3), '.5f')} \n"
                self.str += round_of_points
            
            # print(f"Last point : {round_of_points.split()}")
            # make last point of vector into a
            self.v = [float(round_of_points.split()[0]) - self.a[0], float(round_of_points.split()[1]) - self.a[1], float(round_of_points.split()[2]) - self.a[2]]
            for i in range(3):
                self.a[i] = float(round_of_points.split()[i])

            # return round_of_points()


        def g_p_looping(self, r, r1 = 1, dir = "gauche"):
            """does a looping of diameter r in the d direction 
            of the previous vector like this :     
                            *2
                        *3     *1
                        *0  *M *4     
            r is distance between first and last point,
            r1 is lateral distance
            d is 1 if goes left, otherwise right"""
            # give looping direction, 1 if left, r if right
            if dir == "gauche" or dir == "g" or dir == "left" or dir == "l":
                d = -1
            elif dir == "droite" or dir == "d" or dir == "right" or dir == "r":
                d = 1
            # start point, b is replacement of a for the middle point math
            # b = self.a
            # self.g_p_vector
            # b = [0, 0, 0]
            c = []
            # self.a = [0, 0, 0]
            for i in range(3):
                c.append(self.a[i])
            b = [c[0], c[1], c[2]]
            # print("c is :", c)
            class_endpoint = Generate_points(b)


            # # end point
            class_endpoint.v = self.v
            # print("start point is :", class_endpoint.a)
            class_endpoint.g_p_vector(r)
            # print("c is :", c)
            # print("start point is :", self.a)
            # print("end_point is :", b)

            # u vector perpendicular to x y 
            u = [-self.v[1], self.v[0], 0]
            #cross vector
            # print(self.v, u)
            cross = np.cross(self.v, u)
            # print("this is cross product vector : ", cross)
            k = r / (math.sqrt(cross[0]**2 + cross[1]**2 + (cross[2])**2))
            k2 = d * r1 / (math.sqrt(u[0]**2 + u[1]**2 + (u[2])**2))
            


            # middle point
            middle_point = []
            for i in range(3):
                # print(f"a point : {self.a} \n end point : {end_point}")
                middle_point.append(((self.a[i]) + (b[i])) / 2)
            # print("middle point is : ", middle_point) 

            # print('THIS IS THE TEST CLASS ENDPOINT')
            # print(class_endpoint)
            # print("END\n")
            # create looping points
            second_point, third_point, fourth_point = [], [], []
            for i in range(3):
                second_point.append(b[i] + cross[i] * 0.5*k + u[i]*0.25*k2)
                third_point.append(middle_point[i] + cross[i] * k + u[i]*0.5*k2)
                fourth_point.append(self.a[i] + cross[i] * 0.5*k + u[i]*0.75*k2)
            
            # for i in range(3):
            #     if i != 2:
            #         second_point.append(b[i])
            #         third_point.append(middle_point[i])
            #         fourth_point.append(self.a[i])
            #     else:
            #         second_point.append(b[2] + r / 2)
            #         third_point.append(middle_point[2] + r)
            #         fourth_point.append(self.a[2] + r / 2)
            
            
            # reminder : self.a is start_point, b is end_point
            # "actually creates the thing to return"
            middle_point_extra = []
            end_point_extra = []
            for i in range(3):
                middle_point_extra.append(middle_point[i] + u[i]*k2)
                end_point_extra.append(b[i] + u[i]*k2)
            all_points = [self.a, middle_point, second_point, third_point, fourth_point, middle_point_extra, end_point_extra]
            round_of_points = ""
            for i in range(1, len(all_points)):
                for j in range(3):
                    round_of_points += f"   {format(all_points[i][j], '.5f')}"
                round_of_points += "\n"
            # print("round of points : \n",round_of_points)

            # add to str
            self.str += round_of_points
            self.a = end_point_extra
        
        def g_p_right_angle(self, r, dir = "g"):

            self.g_p_vector(r, (r + 1)//2)
            self.v[2] = 0

            if dir == "gauche" or dir == "g" or dir == "left" or dir == "l":
                d = -1
            elif dir == "droite" or dir == "d" or dir == "right" or dir == "r":
                d = 1
            self.v = [d * self.v[1], d * -self.v[0], self.v[2]]

            self.g_p_vector(r, (r + 1)//2)
            # """creates a r length d direction right angle"""
            


        def __str__(self):
            """return all points to put into the file"""
            return self.str

    a = [0, 0 , 0]
    a = [0, 0, 8.2]
    b = [-4.5, 0, 5,9]
    points = Generate_points(a)
    points.g_p_line(b)
    # print("current vector is : ", points.v)
    points.g_p_looping(0.95, 0.3)
    points.g_p_vector(0.5, 1, 0.1)
    points.g_p_looping(0.95, 0.3, "droite")
    points.g_p_vector(2.3, 3, 0.65)
    points.g_p_line([-9.44970, 0.00000, 3.53400], 3)
    points.g_p_line([-11.09700, 0.00000, 3.53400], 1)
    points.g_p_line([-11.09700, 1.65000, 3.53400], 2)
    points.g_p_vector(2.2, 3)
    points.g_p_half_circle("droite", 1.3)
    points.g_p_vector(1.8, 3)
    points.g_p_vector(1.4, 3, -0.5)
    points.g_p_vector(0.6, 1, 0.146)
    points.g_p_line([-8, 0, 2.97800], 3)
    points.g_p_vector(0.8, 1)
    points.g_p_line([-7.201, 3.5, 2.500], 3)
    points.g_p_half_circle("left", 1.5)
    points.g_p_vector(0.8, 1)
    points.g_p_line([-7.20100,    2.70000,    2.00000], 3)
    points.g_p_vector(5)
    points.g_p_looping(0.8, 0.3, "gauche")
    points.g_p_vector(2.5, 3, 0.5)

    # LOGO 36
    # a = [0, 0 , 3]
    # points = Generate_points(a)
    # points.g_p_line([10, 0 , 0], 5)
    # points.g_p_line([5, -5, 0], 10)
    # points.g_p_line([5.1, -5, 0], 1)
    # points.g_p_half_circle("droite", 10)
    # points.g_p_vector(3)
    # points.g_p_right_angle(2, "g")
    # points.g_p_right_angle(1, "g")
    # points.g_p_looping(6, 3, "g")
    # points.g_p_looping(4, 2, "gauche")
    # points.g_p_looping(3, 2, "right")
    # points.g_p_looping(2, 1, "r")


    # points = Generate_points([10, 0 , 0])
    # points.g_p_line([5, -5, 0], 3)
    # points.g_p_looping(10, 3, "g")
    # points.g_p_looping(5, 2, "r")
    # points.g_p_looping(4, 2, "right")
    # points.g_p_looping(3, 1, "r")
    # points.g_p_looping(2, 0.5, "r")
    # points.g_p_looping(1, 0.25, "r")
    # points.g_p_vector(8)
    # points.g_p_vector(5, 3, 3)
    
#     points = Generate_points([5, -5, 0])
#     points.g_p_line([5.1, -5, 0], 1)
#     points.g_p_right_angle(10, "g")
#     points.g_p_right_angle(5, "g")
#     points.g_p_half_circle("droite", 10)
#     points.g_p_half_circle("g", 8)
#     points.g_p_half_circle("droite", 6)
#     points.g_p_half_circle("g", 4)
#     points.g_p_half_circle("gauche", 4)
    

    # d = input("Give point D in this format : X, Y, Z : ").split()
    with open("looping_points.txt", "w") as f:
        f.write(str(points.__str__()))
    # print(points)


def xyz_graph():
    """
    plot and show xyz coordinates
    """
    #give lists of respectively x, y and z points according to time
    # give_points = points.__str__().split('\n')
    # print(give_points)
    xyzPoints = np.loadtxt("looping_points.txt", unpack=True)

    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    xyzPath = path_points(xyzPoints, 75)
    x = xyzPath[0]
    y = xyzPath[1]
    z = xyzPath[2]
    
    list_of_t = []
    n = 1
    for i in range(len(x)):
        list_of_t.append(float(n))
        n += 1
    # print(list_of_t)
    t = list_of_t

    plt.plot(t, x, 'b', label = "X axis")
    plt.plot(t, y, 'r', label = "Y axis")
    plt.plot(t, z, 'g', label = "Z axis")
    plt.axis([0, 100, -15, 10])

    plt.xlabel("Time (s/10)")
    plt.ylabel("Values of xyz according to time (dm)")
    plt.title("Point values")
    plt.legend()
    #for i, j in zip(t, x):
    #   plt.text(i, j+0.5, '({}, {})'.format(i, j))

    plt.show()


if __name__ == "__main__":
    # pass
    main()
    # xyz_graph()

"""Code created by Ralph Goffart Winkin in the context of his 1st year of Bachelor,
which is used with path3d (library from UCLouvain), numpy and matplotlib, in which none of the 3 libraries
does contain any work of my own. test_sim.py and make_simulation are the only files created solely
and exclusively by myself. 7/12/2021"""
