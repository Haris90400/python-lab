import random

class NumberTooLarge(Exception):
    def __init__(self, msg):
        self.msg = msg
    
class NumberTooSmall(Exception):
    def __init__(self, msg):
        self.msg = msg

random_number = random.randint(1,100)
count = 0
print(random_number)
while True:
    count = count+1
    try:
        number = int(input("Enter a number: "))
        if number <random_number:
            raise NumberTooSmall("The number is too small!!")
        elif number>random_number:
            raise NumberTooLarge("The number is too large!!")
        else:
            break
    except NumberTooSmall as me:
        print(me)
    except NumberTooLarge as me:
        print(me)

print(f"You have correctly guessed the number :{random_number} in {count} guesses")






