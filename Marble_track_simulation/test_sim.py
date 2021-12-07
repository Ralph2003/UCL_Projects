from math import sqrt
from path3d import *
"""path3d is a given file/library from my Uni (UCL) and is not Ralph Goffart Winkin's own work."""
import numpy as np
import matplotlib.pyplot as plt

def main():
    steps = 500
    affichage_chemin(steps)
    v, a, t, ep, ek = donnees_physique(steps)
    xyz_graph()
    affichage_graphiques(v, a, t, ep, ek)


"""
===============
Partie sur l'affichage du chemin
==============="""

"""     XPath: array[3,steps]
            coordonnées des points sur le chemin en 3 dimensions
        sPath: array[N]
            distance curvilinéaire des points
        TPath: array[3,N]
            vecteur tangent aux points (|T| = 1)
        CPath: array[3,N]
            vecteur de courbure aux points (|C| = courbure = 1/rayon)
    """    
    
def affichage_chemin(steps):
    """affiche le chemin"""
    #points de passage
    xyzPoints = np.loadtxt("looping_points.txt", unpack=True)

    # chemin et vecteurs
    xyzPath = path_points(xyzPoints, steps)
    sPath, TPath, CPath = path_vectors(xyzPath)

    # points jalons à afficher sur le graphique
    length = sPath[-1]
    sMarks = np.linspace(0, length, 30)    
    xyzMarks = np.array([np.interp(sMarks, sPath, uPath) for uPath in xyzPath])
    TMarks = np.array([np.interp(sMarks, sPath, uPath) for uPath in TPath])
    CMarks = np.array([np.interp(sMarks, sPath, uPath) for uPath in CPath])

    # graphique 3D : chemin et vecteurs
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_box_aspect(np.ptp(xyzPath, axis=1))
    ax.plot(xyzPoints[0],xyzPoints[1],xyzPoints[2],'c.', label='points')
    ax.plot(xyzPath[0],xyzPath[1],xyzPath[2],'k-', lw=0.5, label='path')    
    ax.plot(xyzMarks[0],xyzMarks[1],xyzMarks[2],'r.', ms=2)
    scale = 0.5
    ax.quiver(xyzMarks[0],xyzMarks[1],xyzMarks[2],
            scale*TMarks[0],scale*TMarks[1],scale*TMarks[2],
            color='r', linewidth=0.5, label='T')
    ax.quiver(xyzMarks[0],xyzMarks[1],xyzMarks[2],
            scale*CMarks[0],scale*CMarks[1],scale*CMarks[2],
            color='g', linewidth=0.5, label='C')
    ax.legend()            
    plt.show()


"""
===============
Partie Physique
==============="""

"""     XPath: array[3,steps]
            coordonnées des points sur le chemin en 3 dimensions
        sPath: array[N]
            distance curvilinéaire des points
        TPath: array[3,N]
            vecteur tangent aux points (|T| = 1)
        CPath: array[3,N]
            vecteur de courbure aux points (|C| = courbure = 1/rayon)
    """    
def donnees_physique(steps):
    # déclaration de données

    #points de passage
    xyzPoints = np.loadtxt("looping_points.txt", unpack=True)

    # chemin et vecteurs
    xyzPath = path_points(xyzPoints, steps)
    sPath, TPath, CPath = path_vectors(xyzPath)

    Vs = 0 # vitesse initiale de la bille en m/s
    b = 0.012 # écartement des rails en m
    r = 0.010 # rayon de la bille en m
    e = 0.0004 # écartement de la bille en m/(m/s)
    g = 9.807 # force de gravité sur Terre
    current_time = 0.0
    track_time = 6
    dt = track_time/steps
    
    velocity_list = []
    acceleration_list = []
    time_list = []
    ep_list = []
    ek_list = []
    
    # """to delete"""
    # g = 9
    # for i in range(len(xyzPoints[0])):
    if steps == None:
        steps = len(xyzPath[0])
    for i in range(steps):
        print("\nNumber is :", i)
        # """test of the given case"""
        # CPath[0][0], CPath[1][0], CPath[2][0] = 2, -2, 0
        # TPath[0][0], TPath[1][0], TPath[2][0] = 2/3, 2/3, 1/3
        # if i == 0:
        #     Vs = 2
        # else : Vs = 0
        """to delete"""
        print("Tpath1 is : ", round(TPath[0][i], 2), round(TPath[1][i], 2), round(TPath[2][i], 2))
        """"""
        

        # print("Tangential vector : ", round(TPath[0][i], 3),round(TPath[1][i], 3),round(TPath[2][i], 3))
        
        # composantes de l'accélération de pesanteur : 
        #reminder : gn is g - gs*T for each array member
        gs = -g * TPath[2][i]
        """to delete"""
        print("gs is : ", round(gs, 2))
        """"""
        # accélération pesanteur "tangentielle" en m/(s**2)

        gn = [0 - gs * TPath[0][i], 0 - gs * TPath[1][i], -g - gs * TPath[2][i]]
        """to delete"""
        print("gn is : ", round(gn[0], 2),round(gn[1], 2), round(gn[2], 2))
        """"""
        # accélération centripète Vs**2 * CPath
        Vs_C = [CPath[0][i] * Vs**2, CPath[1][i] * Vs**2, CPath[2][i] * Vs**2]
        """to delete"""
        print("Vs_C is : ", Vs_C[0],Vs_C[1],Vs_C[2])
        """"""
        # Norme de l'accélération normale (m/(s**2))
        Gn = sqrt((Vs_C[0] - gn[0])**2 + (Vs_C[1] - gn[1])**2 + (Vs_C[2] - gn[2])**2)
        """to delete"""
        print("Gn is : ", round(Gn, 2))
        """"""
        # distance centre bille --> rails
        h = sqrt(r**2 - (b**2 / 4))

        # l'accélération enfin dieu merci m/(s**2)

        a = (gs - ((e*Vs/h)*Gn)) / (1 + (2 * r**2) / (5 * h**2))

        # velocity of the marble
        Vs += a * (track_time/steps)

        # append vs and a to their respective list in order to plot them
        velocity_list.append(Vs)
        acceleration_list.append(a)


        # time
        if i >= 1:
            current_time += dt
        else: 
            current_time = 0
        
        time_list.append(current_time)
        print("current time is : ", current_time)
        print(round(a, 2), 'm/(s**2)')
        print(round(velocity_list[i], 2), 'm/s')

        # append data to energy lists
        m = 0.016 # masse de la bille en kg
        ep_list.append(m * g * xyzPath[2][i])
        ek_list.append(0.5 * m * Vs ** 2 * 10)
        

    return velocity_list, acceleration_list, time_list, ep_list, ek_list


def xyz_graph():
    #give lists of respectively x, y and z points according to time
    # give_points = points.__str__().split('\n')
    # print(give_points)
    xyzPoints = np.loadtxt("looping_points.txt", unpack=True)

    plt.rcParams["figure.figsize"] = [6, 3.50]
    plt.rcParams["figure.autolayout"] = True
    xyzPath = path_points(xyzPoints, 60)
    x = xyzPath[0]
    y = xyzPath[1]
    z = xyzPath[2]
    

    list_of_t = []
    n = 1
    for i in range(len(x)):
        list_of_t.append(float(n))
        n += 1

    t = list_of_t

    plt.plot(t, x, 'b', label = "X axis")
    plt.plot(t, y, 'r', label = "Y axis")
    plt.plot(t, z, 'g', label = "Z axis")
    plt.axis([0, 80, -15, 10])

    plt.xlabel("Time (s/10)")
    plt.ylabel("Values of xyz according to time (dm)")
    plt.title("Point values")
    plt.legend()
    #for i, j in zip(t, x):
    #   plt.text(i, j+0.5, '({}, {})'.format(i, j))

    plt.show()

    # x_points, y_points, z_points = [], [], []
    # for i in range(len(give_points) - 1):
    #     x_points.append(float(give_points[i][3:10]))
    #     y_points.append(float(give_points[i][14:21]))
    #     z_points.append(float(give_points[i][25:32]))
    # print(f"x_points :{x_points}\n\n\n y points :{y_points}\n\n\n z points :{z_points}\n")

def affichage_graphiques(v, a, t, EpSim, EkSim):

    # affichage de la vitesse, et de l'accélération en fonction du temps
    # print("\n", v, "\n\n\n", a)
    energy_total_list = []
    for i in range(len(EpSim)):
        energy_total_list.append(EkSim[i] + EpSim[i])

    plt.figure()
    plt.plot(t, v, 'b-', label='Vs (m/s)')
    plt.plot(t, a, 'r-', label='a (m/s**2')
    # plt.plot(t, EkSim+EpSim, 'k-', label='E/m')
    plt.legend()
    plt.ylabel('Speed and acceleration')
    plt.xlabel('t [s]')
    plt.show()

    # plot énergies en fonction du temps
    plt.figure()
    plt.plot(t, EpSim, 'b-', label='Ep/m')
    plt.plot(t, EkSim, 'r-', label='Ek/m')
    plt.plot(t, energy_total_list, 'k-', label='E/m')
    plt.legend()
    plt.ylabel('Energy/mass [J/kg]')
    plt.xlabel('t [s]')
    plt.show()




    
    
if __name__ == "__main__":
    main()
    
"""Code created by Ralph Goffart Winkin in the context of his 1st year of Bachelor,
which is used with path3d (library from UCLouvain), numpy and matplotlib, in which none of the 3 libraries
does contain any work of my own. test_sim.py and make_simulation are the only files created solely
and exclusively by myself. 7/12/2021"""