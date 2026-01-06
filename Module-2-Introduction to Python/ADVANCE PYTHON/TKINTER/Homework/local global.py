x=10
def add():
    global x
    x=5      # this is defined as global so x will be 5 and x will not be 10
add()
print(x)

x=10
def sub():
    x=5
sub()
print(x)