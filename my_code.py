# Collaborators (including web sites where you got help: (enter none if you didn't need help) none


def find_gcf(x,y):   # Do not change function name!
    # User code goes here
    number=1
    while number<=x and number <=y:
        if x%number==0 and y%number==0:
            gcf=number
            number=number+1
        else:
            number=number+1
    return(gcf)

if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
    print(find_gcf(6,9))

    # After you are satisfied with your results, use input() to prompt the user for two values:
    #x = int(input("Enter a number: "))
    #y = int(input("Enter another number: "))

