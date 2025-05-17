from graphes.delaunay import open_delaunay_triangulation_graph
from graphes.gabriel import open_gabriel_graph
from graphes.integer import open_integer_graph
from graphes.k_closest_neighbors import open_k_closest_neighbors_graph
from graphes.minimum_spanning_tree import open_minimum_spanning_tree_graph
from graphes.nearest_neighbor import open_nearest_neighbor_graph
from graphes.relative_neighborhood import open_relative_neighborhood_graph
from graphes.unit_disk import open_unit_disk_graph
from graphes.yao import open_yao_graph


graphes_disponibles = {
    "Delaunay triangulation graph": open_delaunay_triangulation_graph,
    "Gabriel graph": open_gabriel_graph,
    "Integer graph": open_integer_graph,
    "K closest neighbors graph": open_k_closest_neighbors_graph,
    "Minimum spanning tree graph": open_minimum_spanning_tree_graph,
    "Nearest neighbor graph": open_nearest_neighbor_graph,
    "Relative neighborhood graph": open_relative_neighborhood_graph,
    "Unit disk graph": open_unit_disk_graph,
    "Yao graph": open_yao_graph

}