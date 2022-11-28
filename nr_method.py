class NewtonRaphson:

    def __init__(self, x, epsilon):
        self.x = x 
        self.epsilon = epsilon
        
    @classmethod
    def from_input(cls):
        return cls(
                float(input("Target: ")),
                float(input("Epsilon: "))
        )


    def first_derv(self):
        guess = self.x/2
        while abs(guess**2 - self.x) >= self.epsilon:
            guess = guess - (((guess**2) -self.x)/(2*guess))
        print('Square root of', self.x, 'is about', guess)

#solver = NewtonRaphson(25, 0.1)
solver = NewtonRaphson.from_input()
solver.first_derv()
