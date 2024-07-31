# Inheritance in python
class Animal:
    def __init__(self) -> None:
        self.num_of_eyes = 2
        
    
    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()
        
    def swim(self):
        print("swim in water.")
        
    def breathe(self):
        super().breathe()
        print("doing this underwater")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(f"Number of eyes: {nemo.num_of_eyes}")