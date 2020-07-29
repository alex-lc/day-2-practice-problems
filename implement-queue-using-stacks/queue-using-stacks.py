# UNDERSTAND
# We have a Queue class with methods that we need to implement using stacks

# PLAN
# A regular Python list is an example of a stack
# We can do a first pass solution using built in list methods

# EXECUTE
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []  # init with an empty list
        self.size = 0  # init size / length to 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)  # append passed in value to end of stack
        self.size += 1  # increase size / length by 1

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.size -= 1  # decrease size / length by 1
        return self.stack.pop(0)  # remove and return first item in stack

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[0]  # return first item in stack

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        # check if our stack is empty
        if self.size > 0:
            return False  # return False if stack is not empty
        # if it is, return True
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
