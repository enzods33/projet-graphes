# Fichier généré automatiquement pour déclarer les graphes disponibles

from graphes.delaunay_triangulation_graph.canvas_delaunay_triangulation_graph import open_delaunay_triangulation_graph_canvas as ouvrir_delaunay_triangulation_graph
from graphes.gabriel_graph.canvas_gabriel_graph import open_gabriel_graph_canvas as ouvrir_gabriel_graph
from graphes.integer_graph.canvas_integer_graph import open_integer_graph_canvas as ouvrir_integer_graph
from graphes.k_closest_neighbors_graph.canvas_k_closest_neighbors_graph import open_k_closest_neighbors_graph_canvas as ouvrir_k_closest_neighbors_graph
from graphes.minimum_spanning_tree_graph.canvas_minimum_spanning_tree_graph import open_minimum_spanning_tree_graph_canvas as ouvrir_minimum_spanning_tree_graph
from graphes.nearest_neighbor_graph.canvas_nearest_neighbor_graph import open_nearest_neighbor_graph_canvas as ouvrir_nearest_neighbor_graph
from graphes.relative_neighborhood_graph.canvas_relative_neighborhood_graph import open_relative_neighborhood_graph_canvas as ouvrir_relative_neighborhood_graph
from graphes.theta_graph.canvas_theta_graph import open_theta_graph_canvas as ouvrir_theta_graph
from graphes.unit_disk_graph.canvas_unit_disk_graph import open_unit_disk_graph_canvas as ouvrir_unit_disk_graph

graphes_disponibles = {
    "Delaunay triangulation graph": ouvrir_delaunay_triangulation_graph,
    "Gabriel graph": ouvrir_gabriel_graph,
    "Integer graph": ouvrir_integer_graph,
    "K closest neighbors graph": ouvrir_k_closest_neighbors_graph,
    "Minimum spanning tree graph": ouvrir_minimum_spanning_tree_graph,
    "Nearest neighbor graph": ouvrir_nearest_neighbor_graph,
    "Relative neighborhood graph": ouvrir_relative_neighborhood_graph,
    "Theta graph": ouvrir_theta_graph,
    "Unit disk graph": ouvrir_unit_disk_graph
}
