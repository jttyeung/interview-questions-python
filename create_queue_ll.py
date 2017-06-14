class Queue(object):
    """ Creates a queue. """

    def __init__(self):
        self.head = self
        self.next = None
        self.tail = None

    def __repr__(self):
        if not self.length():
            return '<Queue (empty)>'
        else:
            return '<Queue %s>' % self.head

    def length(self):
        count = 0

        if self.is_empty():
            return 0

        current = self.head

        while self.next is not None:
            current = self.next
            count += 1
        return count


    def dequeue(self):
        # Could also use import collections
        # Use collections.deque() to pop() or popleft()
        while not self.is_empty():
            current = self.head
            new_head = self.head.next
            self.head = new_head

            return current

        return 'this queue is empty. nothing to dequeue.'


    def enqueue(self, item):
        """Add item to end of queue::

            >>> q = Queue()
            >>> q.enqueue("buy flight")
            >>> q.enqueue("pack")
            >>> q.enqueue("enjoy vacation")

            >>> q
            <Queue ['buy flight', 'pack', 'enjoy vacation']>

            >>> q.length()
            3
        """
        # # If I kept track of 'tail'
        # self.tail.next = item
        # self.tail = item

        # If I didn't keep track of 'tail'
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = item


    def is_empty(self):
        return self.head == None


    def peek(self):
        """Return but don't remove the first item in the queue.

            >>> q = Queue()
            >>> q.enqueue("buy flight")
            >>> q.enqueue("pack")
            >>> q.enqueue("enjoy vacation")

            >>> q.peek()
            'buy flight'

            >>> q
            <Queue ['buy flight', 'pack', 'enjoy vacation']>
        """
        return self.head


if __name__ == '__main__':
    import doctest
    results = doctest.testmod()

    if not results.failed:
        print "ALL TESTS PASSED!"

