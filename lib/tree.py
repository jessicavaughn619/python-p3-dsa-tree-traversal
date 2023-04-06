class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_visit = [self.root]

    while len(nodes_to_visit) > 0:
      node = nodes_to_visit.pop(0)
      if node['id'] == id:
        return node
      
      nodes_to_visit = nodes_to_visit + node['children']
    return None

# # Breadth first traversal 
#   def breadth_first_traversal(node):
#     result = []
#     nodes_to_visit = [node]

#     while len(nodes_to_visit) > 0:
#       node = nodes_to_visit.pop(0)
#       result.append(node['value'])
#       nodes_to_visit = nodes_to_visit + node['children']

#     return result
  
#   child_1 = {
#     'value': 2,
#     'children': []
#   }

#   child_2 = {
#     'value': 3,
#     'children': []
#   }

#   child_3 = {
#     'value': 4,
#     'children': []
#   }

#   root = {
#     'value': 1,
#     'children': [child_1, child_2, child_3]
#   }

#   print(breadth_first_traversal(root))

# # Depth first traversal (preorder traversal)
#   def depth_first_traversal(node):
#     result = []
#     nodes_to_visit = [node]

#     while len(nodes_to_visit) > 0:
#       node = nodes_to_visit.pop(0)
#       result.append(node['value'])
#       nodes_to_visit = node['children'] + nodes_to_visit
    
#     return result
  
#   def depth_first_traversal(node, result = []):
#     result.append(node['value'])
#     for child in node['children']:
#       depth_first_traversal(child, result)

#     return result