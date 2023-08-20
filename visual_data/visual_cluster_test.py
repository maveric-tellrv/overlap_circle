import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

import math


from cluster_utils import reduce_clusters

def plot_circle(inputcircle):

    # tup_out = [(0.5, 0.5, 0.5), (0.7, 0.7, 0.4), (1.5, 1.5, 1.1),(4,4,0.7),(3,3,0.5),(3,2,0.5)]
    if (len(inputcircle)>=1):
        draw(inputcircle,'input')
        draw(reduce_clusters(inputcircle),'output')
    # Call the function to plot the circle
        plt.show()

    


def draw(tup,fig):
    plt.figure(fig)    
    theta = np.linspace(0, 2*np.pi, 100)
    for tup in tup:
        x = tup[0] + tup[2] * np.cos(theta)
        y = tup[1] + tup[2] * np.sin(theta)

        # x = center[0] + radius * np.cos(theta)
        # y = center[1] + radius * np.sin(theta)
        plt.plot(x, y,label=tup)
        plt.axis('equal')  # Ensure aspect ratio is maintained
        plt.title("Circle input")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid(True)
        plt.legend()



# ctuple = [(0.5, 0.5, 0.5),(0.7, 0.7, 0.4),(1,1,1),(1.5, 1.5, 1.1),(4,4,0.7),(2.9,3,1)]
# ctuple2 = [(0.5, 0.5, 0.5), (0.7, 0.7, 0.4),(1.5, 1.5, 1.1),(4,4,0.7)]
# ctuple3 = [(1.5, 1.5, 1.1),(4,4,0.7)]
# ctuple4 = [(1,3,0.7),(2,3,0.4),(3,3,0.9)]
# ctuple5 = [(0.5, 0.5, 0.5), (0.7, 0.7, 0.4), (1, 1, 1), (1.5, 1.5, 1.1),(2.9, 3, 1),(4, 4, 0.7),(5,5,0.5),(6,6,1),(7,7,1.5)]
# ctuple6 = [(0.5, 0.5, 0.5), (0.7, 0.7, 0.4), (1, 1, 1), (1.5, 1.5, 1.1),(2.9, 3, 1),(4, 4, 0.7),(5,5,0.5),(6,6,1),(7,7,1.5),(7.5,7.5,0.5)]
# ctuple7 = [(0.5, 0.5, 0.5), (0.7, 0.7, 0.4), (1, 1, 1), (1.5, 1.5, 1.1),(2.9, 3, 1),(4, 4, 0.7),(5,5,0.5),(6,6,1),(7,7,1.5),(7.5,7.5,0.5),(7.5,7.5,0.3),(6.3,6.3,0.6)]
# ctuple8 = [(1,1,0.5),(2,1,0.5)]
# ctuple8 = [(1,1,0.5),(1.25,1,0.25),(2,1,0.5)]

ctuple2 = [(0.5, 0.5, 0.5), (0.7, 0.7, 0.4),(1.5, 1.5, 1.1),(4,4,0.7)]
ctuple3 = [(1.5, 1.5, 1.1),(4,4,0.7)]
ctuple4 = [(1,3,0.7),(2,3,0.4),(3,3,0.9)]
ctuple5 = [(0.5, 0.5, 0.5),(0.7, 0.7, 0.4),(1,1,1),(1.5, 1.5, 1.1),(4,4,0.7),(2.9,3,1)]

test_data = [ctuple2,ctuple3,ctuple4,ctuple5]
for ctup in test_data:
    print(reduce_clusters(ctup))
    plot_circle(ctup)