class Node:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val


class LinkedList:
    def __init__(self, head):
        self.head = head

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev


def search_and_delete(list, key):
    if list.head is None:
        return list
    node = list.head
    while node is not None:
        if key == node.val:
            list.delete(node)
        node = node.next
    return list

node = Node(1)
node.next = Node(2)
node.next.prev = node
node.next.next = Node(1)
node.next.next.prev = node.next
list = LinkedList(node)
print("before:", node.val, "->", node.next.val, "->", node.next.next.val, "->", node.next.next.next)
node = search_and_delete(list, 1).head
print("after:", node.val, "->", node.next)
