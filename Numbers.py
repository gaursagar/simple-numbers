# Common Number Operations Library

class Numbers:
    
    def is_even(self, x):
        return x%2 == 0

    def add(self, *args):
        sum = 0
        for arg in args:
            sum += float(arg)
        return sum