import math

def reduce_clusters(ctuple_list):
    """
    Takes in an unordered list of ctuples. Identifies clusters of ctuples by overlapping area.
    Then returns a list of ctuples where each item in the list corresponds to one ctuple per
    cluster of the highest area.
    The length of the returned list should equal the number of clusters formed from the original
    ctuple list
    :param ctuple_list: A list of ctuple definitions in the form [(x, y, r), (x, y, r), ... ]
    :return: A list of ctuple definitions in the form [(x, y, r), (x, y, r), ... ]
    """

    dataset = unique_data(ctuple_list)
    # print(find_clusters_sets(dataset))
    total_cluster_formed = merge_sets_with_intersection(find_clusters_sets(dataset))
    final_cluster = only_keep_largest_circle_in_cluster(total_cluster_formed)
    
    # print(final_cluster)

    return final_cluster
    


def find_clusters_sets(circle):
    '''
    This functions returns the list of all possible combinations 
    for overlapping circle
    :params accept the ctuple
        [(0.5, 0.5, 0.5), (0.7, 0.7, 0.4),(1.5, 1.5, 1.1),(4,4,0.7)]
    returns: A list of compbination of overlapping clusters
        [[(4, 4, 0.7)], [(1.5, 1.5, 1.1), (0.5, 0.5, 0.5), (0.7, 0.7, 0.4)], [(0.7, 0.7, 0.4), (0.5, 0.5, 0.5)], [(0.7, 0.7, 0.4)]]
    '''
    
    listCluster = []
    for idx,c in enumerate(circle):
        clus = []
        if (idx < len(circle)):
            listofc = circle[idx+1:]
   
        if (len(listofc)>0):
            for elem in listofc:
                if checkOverlap(c,elem):
                   
                    clus.append(elem)
                    clus.append(c)
                else:
                    clus.append(c)
    
           
            clus = unique_data(clus)

        else:
            clus.append(c)
        if(len(clus)>0):
            listCluster.append(unique_data(clus))

    return listCluster



def merge_sets_with_intersection(sets):
    '''
    find the intesection of two circle set and  merge it
    :param accept the list of list of overlap circle and merge it 
        [[(3, 3, 0.9), (2, 3, 0.4)], [(1, 3, 0.7), (2, 3, 0.4)], [(2, 3, 0.4)]] 
    :returns list of merge set circle cluster 
        [{(3, 3, 0.9), (1, 3, 0.7), (2, 3, 0.4)}]
    '''
    
    # Convert the list of list of tuples to list of sets of tuples
   
    lenght_initial = len(sets)

    if (type(sets[0]) == type([])):
        
        list_of_sets = []

        for sublist in sets:
            new_set = set()
            for tuple_item in sublist:
                new_set.add(tuple_item)
            list_of_sets.append(new_set)
    
    # list of sets of tuples
        sets = list_of_sets
      
    merged_sets = []
    
    for current_set in sets:
        merged = False
        
        # Try to merge with existing sets
        for merged_set in merged_sets:
            if current_set.intersection(merged_set):
                merged_set.update(current_set)
                merged = True
                break
        
        # If not merged, add as a new set
        if not merged:
            merged_sets.append(current_set)

    
    if (len(merged_sets) > 1 and lenght_initial != len(merged_sets)) :
        
        lenght_initial = len(merged_sets)
        return merge_sets_with_intersection(merged_sets)
    
    else:
        return merged_sets


def checkOverlap(c1,c2):
    '''
    Return true if two tuple with c1 (x,y,r) & C2
    match the overlapping criteria r1-r2 <= distance <= r1 + r2
    :param: tuple (x1,y1,r1), (x2,y2,r2)
    :return: True|False
    '''

    if(len(c1) & len(c2) == 3):
        x1, y1, r1 = c1
        x2, y2, r2 = c2
    
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
        # if ( r1-r2 <= distance <= r1+r2):
        if ( distance <= r1+r2):
            return True
        else:
            return False


def unique_data(tup):
    '''
    This function accepts the list of tuple
    removes invalid and duplicate value
    :param: accepts ctuple 
    :retruns: list of valid dataset and removes duplicate
    '''

    # Creata a empty set 
    circle_data = set()
    for item in tup:
        if(len(item) == 3):
            circle_data.add(item)
        else:
            print("INVALID dataset Excluded",item)
    
    #Convert the set to list 
    circle_data_list = list(circle_data)

    # validate duplicates in dataset 
    # if (len(tup) != len(circle_data_list)):
    #     print("removing duplicate")

    return circle_data_list


def only_keep_largest_circle_in_cluster(clusterVal):
    '''
    This function accept the circle cluster set and return
    the list of largest.
    :param: list of set tuples 
            [{(3, 3, 0.9), (1, 3, 0.7), (2, 3, 0.4)}]
    :return: list of large circle
         [(3, 3, 0.9)]
    '''

    #list to hold the single largert circle in cluster

    listOfCircle = []

    for cluster in clusterVal:
    
        if (len(cluster)):
            #largest area
            la = 0
            #largest circle
            lc = None

            for circle in cluster:
                x,y,r = circle
                area = math.pi* r**2

                if area > la:
                    la = area
                    lc = circle
            listOfCircle.append(lc)
        else:
            listOfCircle.append(cluster)
    
    return listOfCircle

