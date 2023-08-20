from cluster_utils import reduce_clusters



ctuple2 = [(0.5, 0.5, 0.5), (0.7, 0.7, 0.4),(1.5, 1.5, 1.1),(4,4,0.7)]
ctuple3 = [(1.5, 1.5, 1.1),(4,4,0.7)]
ctuple4 = [(1,3,0.7),(2,3,0.4),(3,3,0.9)]
ctuple5 = [(0.5, 0.5, 0.5),(0.7, 0.7, 0.4),(1,1,1),(1.5, 1.5, 1.1),(4,4,0.7),(2.9,3,1)]

test_data = [ctuple2,ctuple3,ctuple4,ctuple5]
for ctup in test_data:
    print("INPUT DATAPOINTS \n",ctup)
    print("OUTPUT CLUSTER\n",reduce_clusters(ctup))
