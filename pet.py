class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting with moderate hunger
        self.energy = 5   # Starting with moderate energy
        self.happiness = 5  # Starting with moderate happiness
        self.tricks = []  # For storing learned tricks
        
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating... 🍖")
        
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping... 💤")
        
    def play(self):
        if self.energy >= 2:  # Can only play if has enough energy
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} is playing... 🎾")
        else:
            print(f"{self.name} is too tired to play! Needs sleep.")
            
    def train(self, trick):
        if self.energy >= 1:  # Training requires energy
            self.tricks.append(trick)
            self.energy = max(0, self.energy - 1)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} learned a new trick: {trick}! 🎪")
        else:
            print(f"{self.name} is too tired to learn new tricks.")
            
    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks:")
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
            
    def get_status(self):
        print(f"\n{self.name}'s current status:")
        print(f"Hunger: {self.hunger}/10 ({'★' * self.hunger}{'☆' * (10 - self.hunger)})")
        print(f"Energy: {self.energy}/10 ({'★' * self.energy}{'☆' * (10 - self.energy)})")
        print(f"Happiness: {self.happiness}/10 ({'★' * self.happiness}{'☆' * (10 - self.happiness)})")
        if self.tricks:
            print(f"Tricks: {self.tricks}")