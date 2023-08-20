from cluster_utils import reduce_clusters

import pytest

# Define the parameters and expected results
@pytest.mark.parametrize("ctuple, expected", [
    ([(0.5, 0.5, 0.5), (0.7, 0.7, 0.4),(1.5, 1.5, 1.1),(4,4,0.7)],[(4, 4, 0.7), (1.5, 1.5, 1.1)]),
    ([(1.5, 1.5, 1.1),(4,4,0.7)],[(1.5, 1.5, 1.1), (4, 4, 0.7)]),
    ([(1,3,0.7),(2,3,0.4),(3,3,0.9)],[(3, 3, 0.9)]),
    ([(0.5, 0.5, 0.5),(0.7, 0.7, 0.4),(1,1,1),(1.5, 1.5, 1.1),(4,4,0.7),(2.9,3,1)],[(1.5,1.5,1.1)])
])
def test_reduce_cluster(ctuple, expected):
    
    print("INPUT\n",ctuple)
    result = reduce_clusters(ctuple)
    print("EXPECTED\n",expected)
    assert result == expected
