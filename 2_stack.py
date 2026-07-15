class Stack:

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


def check_brackets(expression):

    stack = Stack()

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in expression:

        if ch in "([{":
            stack.push(ch)

        elif ch in ")]}":

            if stack.is_empty():
                return "Not Balanced"

            top = stack.pop()

            if top != pairs[ch]:
                return "Not Balanced"

    if stack.is_empty():
        return "Balanced"

    return "Not Balanced"


# Stack demonstration
stack = Stack()

stack.push("A")
stack.push("B")
stack.push("C")

print("Top:", stack.peek())
print("Removed:", stack.pop())
print("Top after pop:", stack.peek())

print()

# Balanced Brackets Checker
exp1 = "{[()]}"
exp2 = "{[(])}"

print(exp1, "->", check_brackets(exp1))
print(exp2, "->", check_brackets(exp2))

# Time Complexity
# Push - O(1)
# Pop - O(1)
# Peek - O(1)
# Bracket Checker - O(n)