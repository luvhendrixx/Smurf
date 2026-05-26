import random

def main():
    while True:
        try:
            user = int(input("Guess a number from 1-10 :) "))
        except ValueError:
            print("That's not a number :( ")
            continue # <--- restart the loop on bad input

        # call the machine(guess) and catch it
        catch = guess(user)
        
        # print the catch
        print(catch)
        
        # the loop only breaks on the correct guess 
        if catch == "Bingo :) ":
            break
        
    
# -----------------make the machine(guess)---------------
def guess(user):
    random_number = random.randint(1, 10)
    
    if user > random_number:
        return "Too high"
    elif user < random_number:
        return "Too low"
    else:
        return "Bingo :) "
        

# call main so the programme actually runs
if __name__ =="__main__":
    main()
