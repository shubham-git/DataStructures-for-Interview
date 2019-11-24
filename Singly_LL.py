class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_first(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_last(self, new_data):
        new_node = Node(new_data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_position(self, position, new_data):
        temp = self.head
        new_node = Node(new_data)
        for _ in range(position-2):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def delete_a_position(self, position):
        temp = self.head
        for _ in range(position-1):
            temp = temp.next
        next = temp.next.next
        temp.next = None
        temp.next = next

    def delete_a_number(self, number):
        temp = self.head
        while temp is not None:
            if temp.data == number:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next
        temp = None

    def length_of_list(self):
        temp = self.head
        length = 0
        while temp is not None:
            length = length+1
            temp = temp.next
        print(length)

    def search_a_number(self, number):
        temp = self.head
        while temp is not None:
            if temp.data == number:
                return True
                break
        return False

    def detect_a_loop(self):
        s = set()
        temp = self.head
        while temp:
            if temp in s:
                return True
        s.add(temp)
        temp = temp.next
        return False

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':

    l_list = LinkedList()
    n = int(input("Enter the size of linked list"))

    for i in range(n):
        if i == 0:
            l_list.head = Node(int(input()))
        else:
            l_list.insert_at_last(int(input()))

    # l_list.insert_at_position(2, 30000)
    # l_list.delete_a_position(5)
    # l_list.delete_a_number(3)
    l_list.length_of_list()
    l_list.print_list()
