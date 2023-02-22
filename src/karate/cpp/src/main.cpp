#include <omp.h>
#include <iostream>
#include <string>
#include <vector>
#include <utility>

#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/graph_traits.hpp>
#include <boost/graph/dijkstra_shortest_paths.hpp>


typedef boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS> Graph;
typedef Graph::vertex_descriptor Vertex;


int main() {
  Graph model;

  // Vertice names
  std::vector<std::string> vertices = {"N", "H", "W", "P", "O"};

  // Add vertices to the graph, a id is assigned to each vertex
  std::unordered_map<std::string, Vertex> vertex_map;
  for (auto v : vertices) {
    vertex_map[v] = boost::add_vertex(model);
  }

  // Print the vertices and their ids
  for (auto v : vertices) {
    std::cout << "Vertex " << v << " " << vertex_map[v] << std::endl;
  }

  // Define edges
  std::vector<std::pair<std::string, std::string>> edges = {
    {"N", "H"},
    {"W", "H"},
    {"H", "P"},
    {"W", "O"}
  };

  // Add edges to the graph
  std::vector<std::pair<Graph::edge_descriptor, bool>> graph_edges;
  for (auto e : edges) {
    auto graph_edge = boost::add_edge(vertex_map[e.first], vertex_map[e.second], model);
    graph_edges.push_back(graph_edge);
  }

  // Print the edges
  for (auto e : graph_edges) {
    std::cout << "Edge " << e.first << " " << e.second << std::endl;
  }


  return 0;
}