import node

class LinkedList:
  def __init__(self, value=None):
    self.head_node = node.Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = node.Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if self.head_node == value_to_remove:
      self.head_node = self.get_head_node().get_next_node()
    else:
      while current_node != None:
        if current_node.get_next_node().get_value() == value_to_remove:
          current_node.next_node = current_node.get_next_node().get_next_node()
          current_node = None
        else:
          current_node = current_node.get_next_node()