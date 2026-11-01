
#The break statement, like in C, breaks out of the smallest enclosing for or while loop.
def Prime(num=10):
    li=[1]
    for number in range(2, num):
        ulimit=int(number/2)
        for counter in range(2, ulimit):
            if number % counter == 0:
                print(number, 'equals',counter,  '*', number//counter)
                break
        else:
            li.append(number)
            print(number, 'is a prime number')
            
if("__main__"==__name__):
    num=int(input('Enter  Upper limit'))
    Prime(num)
