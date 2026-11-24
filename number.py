import random

class Number:
    def generate(self):
        return random.sample(range(1, 50), 6)

class Ticket:
    def __init__(self):
        self.numbers = []

    def read_numbers(self):
        while len(self.numbers) < 6:
            n = int(input(f"Number {len(self.numbers) + 1}: "))
            if n < 1 or n > 49:
                print("Must be between 1 and 49!")
            elif n in self.numbers:
                print("You already picked that one!")
            else:
                self.numbers.append(n)

    def check(self, draw):
        matches = set(self.numbers) & set(draw)
        print(f"Draw: {sorted(draw)}")
        print(f"Your ticket: {sorted(self.numbers)}")
        if len(matches) == 6:
            print("JACKPOT!")
        else:
            print(f"Not this time. You guessed {len(matches)}: {sorted(matches)}")


draw = Number().generate()
t = Ticket()
t.read_numbers()
t.check(draw)