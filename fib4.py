#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

# Requests a variable (n) from the user, and prints the fibonacci sequence 
# for n iterations. Only prints 4 iterations per line

class Fib :
    def __init__(self, max_iterations) :
        self.current = 0
        self.next = 1
        self.num_iterations = 0
        if max_iterations < 1 :
            raise ValueError
        self.max_iterations = max_iterations

    def __iter__(self) :
        return self
    
    def __next__(self) :
        output = self.current
        self.current, self.next = self.next, self.current + self.next
        self.num_iterations += 1
        if self.num_iterations > self.max_iterations :
            raise StopIteration
        return output

outstring = ""

try :
    n = int(input("Please enter a positive integer: "))
    for i in Fib(n) :
        outstring += str(i) + " "
        if outstring.split("\n")[-1].count(" ") > 3 :
            outstring += "\n"
    print("Output:")
    print(outstring)

except ValueError :
    print("Input is not a valid positive integer")
