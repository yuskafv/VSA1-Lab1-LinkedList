# Bağlı siyahı (Linked List) reallaşdırılması


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def display(self):
        if self.head is None:
            print("Siyahı boşdur")
            return
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

    def delete_node(self, key):
        current = self.head

        # birinci element silinirsə
        if current is not None and current.data == key:
            self.head = current.next
            return True

        previous = None
        while current is not None and current.data != key:
            previous = current
            current = current.next

        if current is None:
            return False  # tapılmadı

        previous.next = current.next
        return True

    def search(self, key):
        current = self.head
        position = 0
        while current is not None:
            if current.data == key:
                return position
            current = current.next
            position += 1
        return -1
