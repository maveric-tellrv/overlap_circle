# Overlap_circle
Solutions: 

Based on my understanding an overlap circle :
1.  Cirlce which intersects and or can be travered from another circle is in a coverlapping cluster cluster
   Considtion used : (distance <= r1+r2)

2.  Assumption : If a circle is sompletely engulf another circle considering it an overlapping circle.
    (based on the problem statmeent it is not clear if a concerntric circle should be considered as overlapping circle or not
    this can be handeled with the setting if condition  ( abs(r1-r2) < distance <= r1+r2)
    adding two version of output3
    
# Python version used: 
  Python 3.6.8

# How to include  reduce_cluster in module
  from cluster_utils import reduce_clusters

# Sample test run file 
 sample data used:
 ```
ctuple2 = [(0.5, 0.5, 0.5), (0.7, 0.7, 0.4),(1.5, 1.5, 1.1),(4,4,0.7)]
ctuple3 = [(1.5, 1.5, 1.1),(4,4,0.7)]
ctuple4 = [(1,3,0.7),(2,3,0.4),(3,3,0.9)]
ctuple5 = [(0.5, 0.5, 0.5),(0.7, 0.7, 0.4),(1,1,1),(1.5, 1.5, 1.1),(4,4,0.7),(2.9,3,1)]
```
```
  pip install -r requirement.txt
  python3 test.py 
[(4, 4, 0.7), (1.5, 1.5, 1.1)]
[(1.5, 1.5, 1.1), (4, 4, 0.7)]
[(3, 3, 0.9)]
```

# To plot the input and putput 
execute visual_cluster_test.py which is inse visual_data folder 
```
visual_data]$ python3 visual_cluster_test.py
```

# Solution 1
![screenshot](https://github.com/maveric-tellrv/overlap_circle/blob/main/images/gitoverlap/solution1.png)

# Solution 2
![screenshot](https://github.com/maveric-tellrv/overlap_circle/blob/main/images/gitoverlap/solution2.png)

# Solution 3
![screenshot](https://github.com/maveric-tellrv/overlap_circle/blob/main/images/gitoverlap/solution3.png)

# Sample data Set
![screenshot](https://github.com/maveric-tellrv/overlap_circle/blob/main/images/gitoverlap/dataset_sample_4.png)
# Input1
![screenshot](https://github.com/maveric-tellrv/overlap_circle/blob/main/images/gitoverlap/Screenshot%20from%202023-08-20%2014-07-36.png)

# Input1
![screenshot](https://github.com/maveric-tellrv/overlap_circle/blob/main/images/gitoverlap/Screenshot%20from%202023-08-20%2014-07-36.png)

# Output1
![screenshot](https://github.com/maveric-tellrv/overlap_circle/blob/main/images/gitoverlap/Screenshot%20from%202023-08-20%2014-07-35.png)

# Input 2
![screenshot](https://github.com/maveric-tellrv/overlap_circle/blob/main/images/gitoverlap/Screenshot%20from%202023-08-20%2014-07-58.png)

# Output 2
![screenshot](https://github.com/maveric-tellrv/overlap_circle/blob/main/images/gitoverlap/Screenshot%20from%202023-08-20%2014-07-56.png)

# Input 3
![screenshot](https://github.com/maveric-tellrv/overlap_circle/blob/main/images/gitoverlap/Screenshot%20from%202023-08-20%2014-05-09.png)

# Output 3-1
![screenshot](https://github.com/maveric-tellrv/overlap_circle/blob/main/images/gitoverlap/output3.png)
# Output 3-2 Concentric circle
Well ths  is corner case which needs clarification if based on the above problem concentric circle should be considered as overlapping cluster
![screenshot](https://github.com/maveric-tellrv/overlap_circle/blob/main/images/gitoverlap/Screenshot%20from%202023-08-20%2014-05-12.png)

# Test Run
```
[overlap_circle]$ pytest test.py -v -s
============================================ test session starts ============================================
platform linux -- Python 3.6.8, pytest-7.0.1, pluggy-1.0.0 -- /home/rovyas/Documents/javascript-objects-prototypes-classes/python/venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/rovyas/Documents/javascript-objects-prototypes-classes/pulltest/overlap_circle
collected 4 items                                                                                           

test.py::test_addition[ctuple0-expected0] INPUT
 [(0.5, 0.5, 0.5), (0.7, 0.7, 0.4), (1.5, 1.5, 1.1), (4, 4, 0.7)]
EXPECTED
 [(4, 4, 0.7), (1.5, 1.5, 1.1)]
PASSED
test.py::test_addition[ctuple1-expected1] INPUT
 [(1.5, 1.5, 1.1), (4, 4, 0.7)]
EXPECTED
 [(1.5, 1.5, 1.1), (4, 4, 0.7)]
PASSED
test.py::test_addition[ctuple2-expected2] INPUT
 [(1, 3, 0.7), (2, 3, 0.4), (3, 3, 0.9)]
EXPECTED
 [(3, 3, 0.9)]
PASSED
test.py::test_addition[ctuple3-expected3] INPUT
 [(0.5, 0.5, 0.5), (0.7, 0.7, 0.4), (1, 1, 1), (1.5, 1.5, 1.1), (4, 4, 0.7), (2.9, 3, 1)]
EXPECTED
```
