# overlap_circle


# python version used: 
  Python 3.6.8

# How to include  reduce_cluster in module
  from cluster_utils import reduce_clusters

# Sample test run file 
 sample data used:
 ```
  ctuple2 = [(0.5, 0.5, 0.5), (0.7, 0.7, 0.4),(1.5, 1.5, 1.1),(4,4,0.7)]
  ctuple3 = [(1.5, 1.5, 1.1),(4,4,0.7)]
  ctuple4 = [(1,3,0.7),(2,3,0.4),(3,3,0.9)]
```
```
  pip install -r requirement.txt
  python3 test.py 
[(4, 4, 0.7), (1.5, 1.5, 1.1)]
[(1.5, 1.5, 1.1), (4, 4, 0.7)]
[(3, 3, 0.9)]
```


