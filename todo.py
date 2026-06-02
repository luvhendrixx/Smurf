# import the libs
import random
import time
# forgot JSON again bro😭
import json

def main():
    # keep the questions coming
    while True:
        try:
            choice = input("What's today's task sir :)....\nA: Add a task?\n B: Search through tasks?\n C: Delete a task?\n D: Get a random task?\n E: Exit?\n: ")
        except TypeError:
            print("Hmm...check your options please :( ")
        
        # if they choose option A
        if choice.upper() == "A":
            # define the contents of the tasks
            name_task = input("What's the name of the task? ")
            try:
                timer_task = input("How long will the task take? ")
                time_task = input("At what time will the task take place? ")

            except TypeError:
                print("Hmm...Please check your time(s) :( ")

            note = input("Describe the task please: ")

            # print the confirmation of the task being added
            print(f"Your task {name_task} with a duration of {timer_task} scheduled at {time_task} with a note {note} has been added :) 🎉 ")
            # call the add_task function and pass in the arguments (CA)
            add_task(name_task, timer_task, time_task, note)


        # if they choose option B
        elif choice.upper() == "B":
            what_task = input("What task are you looking for :)? ")
            catch = search_tasks(what_task)
            
            # Case 1: An error message string was returned
            if isinstance(catch, str):
                print(catch)
                
            # Case 2: A single task dictionary was returned
            elif isinstance(catch, dict):
                print(f"\nFound it 🙂: ")
                print(f"Name:        {catch['Name']}")
                print(f"Duration:    {catch['Timer']}")
                print(f"Time:        {catch['Time']}")
                print(f"Description: {catch['Description']}\n")
                
            # Case 3: A list of multiple matching tasks was returned
            elif isinstance(catch, list):
                print(f"\n🔍 Found {len(catch)} matching tasks:")
                for task in catch:
                    print(f"- {task['Name']} ({task['Time']})")
                print()

        # if they choose option C
        elif choice.upper() == "C":
            # 1. Load the DB right here so we can show the user their tasks
            try:
                with open("DB.json", "r") as file:
                    my_sql = json.load(file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                my_sql = {}

            if not my_sql:
                print("You don't have any tasks to delete yet! 🤷‍♂️")
                continue # Skip back to the main menu

            # 2. Map numbers to the actual lowercase keys in a list
            # list(my_sql.keys()) gives us e.g. ["clean da office", "call mum"]
            task_keys_list = list(my_sql.keys()) 

            print("\n--- Here are your current tasks ---")
            for index, key in enumerate(task_keys_list, start=1):
                # Display the clean display name stored inside the task
                print(f"{index}: {my_sql[key]['Name']}") 
            print("----------------------------------")

            # 3. Get the user's choice as a number
            try:
                task_num = int(input("Enter the number of the task you'd like to delete: "))
                
                # Check if the number is valid (e.g. if they have 3 tasks, they can't pick 5)
                if task_num < 1 or task_num > len(task_keys_list):
                    print("That number isn't on the list, broski! ❌")
                    continue
            except ValueError:
                print("Please type an actual number! 🧐")
                continue

            # 4. Figure out exactly which key they picked using the index
            to_delete = task_keys_list[task_num - 1] # -1 because list indexing starts at 0

            # 5. Ask for final confirmation
            confirm_del = input(f"Are you sure you want to delete '{my_sql[to_delete]['Name']}'? (Yes/No): ")
            
            if confirm_del.capitalize() == "Yes":
                caught = del_task(to_delete) # Pass the exact key to our function
                print(f"Goodbye task 😔 ") 
            elif confirm_del.capitalize() == "No":
                print("Phew, thought you wanted me gone😅")
            else:
                print("That's not a valid choice, task safe! 😅")


        # if they choose option D (randomise a task in their tasks)
        elif choice.upper() == "D":
            print("Get readyy...bep..bop...beep...boop👀..ready?...👀")
            # add a short delay to create suspens.....
            time.sleep(1.5)
            # call the random function && catch it
            catch_random = random_task()
            # If it returned a string error message instead of a dictionary, print it
            if isinstance(catch_random, str):
                print(catch_random)
            else:
                # print the random task using the keys inside catch_random
                print(f"Here is your task: \n{catch_random['Name']} \n{catch_random['Timer']} \n{catch_random['Time']} \n{catch_random['Description']} 😎 ")

        # we tell the user goodbye && BREAK THE LOOP IF they want out
        elif choice.upper() == "E":
            print("Have a good time, see you soon🙂👋")
            break

        # else if the user keys in something not in the DB, TELL THEM
        else:
            print("That's not in the list, try again maybe😅")



def add_task(name_task, timer_task, time_task, note):
    # we create the empty DB so it actually exists(READ FIRST) && so python doesn't start crying
    try:
        with open("DB.json", "r") as file:
            my_sql = json.load(file) # load the contents of the empty DB
    except FileNotFoundError: # so python doesn't cry if it doesn't find the DB
        my_sql = {}
    except json.decoder.JSONDecodeError:
        my_sql = {} # same reason, python doesn't cry if it can't read the DB && creates the DB and loads the users contents

    # now we define the DB schema
    my_sql[name_task.lower()] = {
        "Name" : name_task,
        "Timer": timer_task,
        "Time" : time_task,
        "Description" : note
    }

    # add the contents INTO the DB THEN immediately SAVE the contents in the DB
    with open("DB.json", "w") as file:
        json.dump(my_sql, file) # load the contents of my_sql and then save them INTO the DB File

    # return the the results of my_sql back to main WHO called add_task (line 26)
    return my_sql


# now we search the DB && return the results IF found
def search_tasks(what_task):
    try: # TRY to open the DB as a file in read form and load it && the contents inside the DB
        with open("DB.json", "r") as file: 
            my_sql = json.load(file)
    except FileNotFoundError:
        my_sql = {}
    except json.decoder.JSONDecodeError:
        my_sql = {}

    search_key = what_task.lower() # Convert search query to lowercase && should be in lowercase

    # Create a blank list to hold any tasks we find
    found_tasks = []

    # loop through every key inside the DB
    for task_key in my_sql:
        # check if what the user typed is actually in the DB
        if search_key in task_key:
            # if it matches, add the found key to out empty list(found_tasks)
            found_tasks.append(my_sql[task_key])
    
    # If our list is empty, we found absolutely nothing
    if not found_tasks:
        return "Hmm... that task doesn't exist... maybe a typo? 🤔"

    # If we found exactly 1 task, return just that task dictionary
    if len(found_tasks) == 1:
        return found_tasks[0]

    # If the user typed in something broad like "car" and it matched return the whole list of matches!
    return found_tasks


# the DELETE a task function💀
def del_task(delete_key): # It's already the exact lowercase key!
    try: 
        with open("DB.json", "r") as file:
            my_sql = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        my_sql = {}

    # Check if it exists just to be perfectly safe before deleting
    if delete_key in my_sql:
        del my_sql[delete_key]
        with open("DB.json", "w") as file:
            json.dump(my_sql, file)
        return "It is done😔"
    else:
        return "Task not found, maybe...try again? 🤔"


    

def random_task():
    try: # try to open the DB THEN check if there's actual contents inside the DB, THEN IF there's contents, do the randomness then return the contents
        with open("DB.json", "r") as file:
            my_sql = json.load(file) # load the ENTIRE FILE ITSELF
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return "You have no tasks yet sadly 😔 "

    # NOW turn the DB values into a list THEN do the randomness
    catch_random = random.choice(list(my_sql.values()))
    # return it back to main
    return catch_random
        
    
if __name__ == "__main__":
    main()