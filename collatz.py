
def collatz():
    global number
    value = int(10)
    while value != 1:
        if  number%2 == 0:
            value = number//2
            print(value)
        else:
            value = 3*number+1
            print(value)
        
        number = value



try:
    number=int(input())
except ValueError:
    print("Error: enter an integer")
number=int(input())
collatz()
