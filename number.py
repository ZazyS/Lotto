import random

class Number:
    def generate(self):
        return random.sample(range(1,  49), 6)

n = Number()
print(n.generate())