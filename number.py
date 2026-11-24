import random

class Number:
    def generate(self):
        return random.randint(1, 49)

n = Number()
print(n.generate())