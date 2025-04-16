# I start by importing unittest, which is a built-in Python module for writing and running tests
import unittest
# Then I import the Graph class from the graph module
from graph import Graph

# I created the TestGraph class, which inherits from the unittest.TestCase class; This is a standard way to create test cases in Python 
class TestGraph(unittest.TestCase):
    # I defined the setUp method, which is called before each test case
    def setUp(self):
        # I created an instance of the Graph class
        self.graph = Graph()
        # I added some edges to the graph for testing purposes
        # These edges represent the flight routes and their costs
        self.graph.add_edge("A", "B", 100)
        # I then added another edge from B to C with a cost of 200 the reason for this is to create a path from A to C
        self.graph.add_edge("B", "C", 200)
    # I defined the test_shortest_path method, which is a test case for the shortest_path method of the Graph class
    # This method tests the shortest path from airport A to airport C
    def test_shortest_path(self):
        # On this line cost is set to the result of calling the shortest_path method on the graph instance; path is set to the path returned by the method 
        cost, path = self.graph.shortest_path("A", "C")
        # self.assertEqual is a method provided by unittest.TestCase that checks if the first argument is equal to the second argument
        # If they are not equal, the test will fail
        # In this case, I am checking if the cost of the shortest path from A to C is 300
        self.assertEqual(cost, 300)
        # here I am checking if the path from A to C is ["A", "B", "C"]
        # This means that the shortest path from A to C goes through B
        self.assertEqual(path, ["A", "B", "C"])
