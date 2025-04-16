import unittest
from graph import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge("A", "B", 100)
        self.graph.add_edge("B", "C", 200)

    def test_shortest_path(self):
        cost, path = self.graph.shortest_path("A", "C")
        self.assertEqual(cost, 300)
        self.assertEqual(path, ["A", "B", "C"])
