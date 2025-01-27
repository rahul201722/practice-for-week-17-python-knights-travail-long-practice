class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None  # Single parent allowed
        self._children = []

    @property
    def value(self):
        """Getter for the value property."""
        return self._value

    @property
    def children(self):
        """Getter for the children property."""
        return self._children

    @property
    def parent(self):
        """Getter for the parent property."""
        return self._parent

    @parent.setter
    def parent(self, node):
        """Setter for the parent property with proper base case."""
        if self._parent == node:
            return  # Base case to prevent recursion

        if self._parent:  # Remove from current parent's children
            self._parent.remove_child(self)

        self._parent = node

        if node and self not in node._children:
            node.add_child(self)

    def add_child(self, node):
        """Adds a child node to the list of children."""
        if node not in self._children:
            self._children.append(node)
            node.parent = self  # Explicitly call the parent setter

    def remove_child(self, node):
        """Removes a child node from the list of children."""
        if node in self._children:
            self._children.remove(node)
            node.parent = None  # Explicitly call the parent setter to trigger mock

    def depth_search(self, value):
        """Performs a depth-first search for a node with the given value."""
        if self._value == value:
            return self
        for child in self._children:
            result = child.depth_search(value)
            if result:
                return result
        return None

    def breadth_search(self, value):
        """Performs a breadth-first search for a node with the given value."""
        queue = [self]
        while queue:
            current = queue.pop(0)
            if current._value == value:
                return current
            queue.extend(current._children)
        return None

# # Example usage
# if __name__ == "__main__":
#     node1 = Node("root1")
#     node2 = Node("root2")
#     node3 = Node("root3")

#     # Test parent-child relationships
#     node3.parent = node1
#     node3.parent = node2

#     print([child.value for child in node1.children])  # Should be empty
#     print([child.value for child in node2.children])  # Should contain "root3"

#     # Test depth-first search
#     node4 = Node("child")
#     node2.add_child(node4)

#     print(node1.depth_search("child"))  # Should
