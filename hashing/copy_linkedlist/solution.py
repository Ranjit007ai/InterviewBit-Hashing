#Given a linked list ,where each node to connected to next node ,and each node consist of nextpointer and randompointer .
# Create a duplicate linked list.
class node:
    def __init__(self,data):
        self.data = data
        self.next = None 
        self.random = None 

node1 = node(1)
node2 = node(2)
node3 = node(3)

node1.next = node2
node2.next = node3

node1.random = node3
node2.random = node1
node3.random = node1

def copyrandomlist(head):
    hash_map = {}
    cur_node = head
    while cur_node != None :
        hash_map[cur_node] = node(cur_node.data)
        cur_node = cur_node.next
    cur_node = head
    while cur_node != None :
        hash_map[cur_node].next = hash_map.get(cur_node.next)
        hash_map[cur_node].random = hash_map.get(cur_node.random)
        cur_node = cur_node.next
    return hash_map.get(head)


# test case
new_head = copyrandomlist(node1)
while new_head != None :
    print(new_head.data)
    new_head = new_head.next