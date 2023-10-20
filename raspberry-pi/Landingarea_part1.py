
def check(test):
    try:
        print(test)
        return True
    except:
        print("Incorract syntax, please re-enter")
        return False
def area(x,y,z):

while True:
    print("Enter the first coordinate x,y:")
    x = float(input().split())
    while(check(x)):
        print("Enter the second coordinate x,y:")
        y = float(input().split())
        while(check(y)):
            print("Enter the third coordinate x,y:")
            z = float(input().split())
                if(check(z)):
                    print(area(x,y,z))

