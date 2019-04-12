
class Element:

    def __init__(self, value, previous_element=None, next_element=None):
        self.value = value
        self.next_element = next_element
        self.previous_element = previous_element


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        elements = []
        _next = self.head

        while _next is not None:
            elements.append(_next.value)
            _next = _next.next_element

        return str(elements)

    def enqueue(self, value):
        element = Element(value, self.tail)

        if self.size == 0:
            self.head = element
        else:
            self.tail.next_element = element
        self.tail = element
        self.size += 1

    def deque(self):

        if self.size == 0:
            raise Exception('Empty queue')

        first_element = self.head.value
        second_element = self.head.next_element
        self.head = second_element
        second_element.previous_element = None
        self.size -= 1

        return first_element

    def is_empty(self):
        return self.size == 0
