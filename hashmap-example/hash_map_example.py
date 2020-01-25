from linked_list import LinkedList, Node
from blossom_lib import flower_definitions

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(size)]
    
  def hash(self, key):
    key_bytes = key.encode()
    key_sum = sum(key_bytes)
    return key_sum
  
  def compress(self, hash_code):
    return hash_code % self.array_size
  
  def assign(self, key, value):
    hash_value = self.hash(key)
    array_index = self.compress(hash_value)
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for item in list_at_array:
      if item[0] == key:
        item[1] = value
        return
    list_at_array.insert(payload)
    
  def retrieve(self, key):
    hash_value = self.hash(key)
    array_index = self.compress(hash_value)
    list_at_index = self.array[array_index]
    for item in list_at_index:
      if item[0] == key:
        return item[1]
    return None
  
blossom = HashMap(len(flower_definitions))
for item in flower_definitions:
  blossom.assign(item[0], item[1])

print(blossom.retrieve('daisy'))
blossom.assign('lilac', 'fun')
print(blossom.retrieve('lilac'))