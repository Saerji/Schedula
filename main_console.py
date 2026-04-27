'''
This is an integrated academic schedule and room retrieval system that takes the user inputs and allow them to sisplay, update, and delete them.

This code will start by displaying the main menu that displays the possible vhoices the user can mak. It will then directs the user to the right function
in order to add new schedule or manipulate existing ones. This system can be used by students to university personalities such as professors or instructors
in order to easily identify schedules, rooms, and / or what course they would take ot attend to.

Author: Sergie Alexis S. Maldonado
'''
import json
import os

def load_schedules():
    if os.path.exists("schedules.json"):
        with open("schedules.json", "r") as file:
            return json.load(file)
    return {}

def save_schedules():
    with open("schedules.json", "w") as file:
        json.dump(schedules, file, indent = 4)
    print("Schedules saved!")
    
def display_menu():
    print("=====================")
    print("      Main Menu      ")
    print("=====================")
    print("1. Add Schedule")
    print("2. Search Schedule")
    print("3. Display All Schedule/s")
    print("4. Update Existing Schedule")
    print("5. Delete Existing Schedule")
    print("6. Exit Program")

def add_schedule(schedules):
    course_code = input("Enter course code: ").upper()
    course_title = input("Input course title: ")
    schedule_day = input("Enter date: (Sunday - Saturday): ")
    
    while True:  
        schedule_hour = input("Enter time in hours (24-hour format): ")
        if schedule_hour.isdigit() and int(schedule_hour) >= 0 and int(schedule_hour) <= 23:
            break
        print("Invalid time input! Please enter numbers between 00-23 only.")
        
    while True: 
        schedule_minutes = input("Enter time in minutes: ")
        if schedule_minutes.isdigit() and int(schedule_minutes) >= 0 and int(schedule_minutes) <= 59:
            break
        print("Invalid time input! Please enter numbers between 00-59 only.")
    
    schedule_time = f"{schedule_hour.zfill(2)}:{schedule_minutes.zfill(2)}"
    schedule_room = input("Enter designated room: ")
    
    entry = {
        "Title" : course_title,
        "Day" : schedule_day,
        "Time" : schedule_time,
        "Room" : schedule_room
    }
    
    if course_code in schedules:
        schedules[course_code].append(entry)
    else:
        schedules[course_code] = [entry]
    
    print(f"Schedule for {course_title} is added successfully.")

def search_schedule(schedules):
    print("Choose which category you would want to search")
    print("1. By course code")
    print("2. By time")
    print("3. By room")
    
    search_choice = input("Enter choice: ")
    
    #-----------------------------------SEARCH BY COURSE CODE-------------------------------------------
    if search_choice == "1":                                                                                                                                                                                                                                                                                                                                                                                            
        search_code = input("Enter course code: ").upper()
        if search_code in schedules:
            print()
            print("Schedule found!")
            print("=====================")
            for i, entry in enumerate(schedules[search_code], start = 1):
                print(f"Schedule No. {i}")
                print(f"Course title: {entry['Title']}")
                print(f"Day: Every {entry['Day']}")
                print(f"Time: {entry['Time']}")
                print(f"Room: {entry['Room']}")
                print("\n")
            print("=====================")    
        else:
            print("Schedule associated with that course code doesn't exist.")
    
    #------------------------------------SEARCH BY TIME-------------------------------------------------
    elif search_choice == "2":
        while True:  
            hour_choice = input("Enter the hour of the course you would want to search: ")
            if hour_choice.isdigit() and int(hour_choice) >= 0 and int(hour_choice) <= 23:
                break
            print("Invalid time input! Please enter numbers between 00-23 only.")
        while True:
            minute_choice = input("Enter the minute of the course you would want to search: ")
            if minute_choice.isdigit() and int(minute_choice) >= 0 and int(minute_choice) <= 59:
                break
            print("Invalid time input! Please enter numbers between 00-59 only.")
        time_found = False
        search_time = f"{hour_choice.zfill(2)}:{minute_choice.zfill(2)}"
        print(f"Schedule/s at {search_time}:")
        
        for key, value in schedules.items():
            for i, entry in enumerate(schedules[key], start = 1):
                if search_time in entry["Time"]:
                    print()
                    print("Schedule found!")
                    print("=====================")
                    print(f"Schedule No. {i}")
                    print(f"Course Title: {entry['Title']}")
                    print(f"Day: Every {entry['Day']}")
                    print(f"Time: {entry['Time']}")
                    print(f"Room: {entry['Room']}")
                    time_found = True
                    print("=====================")
        if time_found == False:
            print("Schedule associated with that timeframe does not exist.")
                    
    
    #--------------------------------------SEARCH BY ROOM------------------------------------------------
    elif search_choice == "3":
        room_found = False
        search_room = input("Enter the room of the schedule you would want to search: ").upper()
        for key, value in schedules.items():
            for i, entry in enumerate(schedules[key], start = 1):
                if search_room in entry["Room"].upper():
                    print()
                    print("Schedule found!")
                    print("=====================")
                    print(f"Schedule No. {i}")
                    print(f"Course Title: {entry['Title']}")
                    print(f"Day: Every {entry['Day']}")
                    print(f"Time: {entry['Time']}")
                    print(f"Room: {entry['Room']}")
                    room_found = True
                    print("=====================")                    
        if room_found == False:
            print("Schedule associated with that room does not exist.")

def display_schedule(schedules):
    if not schedules:
        print("There is no existing schedules found. Please add schedules in the Add Schedules menu.")
    else:
        print("All existing schedules:")
        for key1, value1 in schedules.items():
            print("============================================")
            print(f"Schedule/s for {key1}:\n")
            for key2, value2 in enumerate(value1, start = 1):
                print(f"Schedule #{key2}:")
                print(f"Course Title: {value2['Title']}")
                print(f"Day: Every {value2['Day']}")
                print(f"Time: starts at {value2['Time']}")
                print(f"Room: {value2['Room']}")
                if key2 > 1:
                    print("\n")
            print("===========================================")

def update_schedule(schedules):
    while True:
        print("To update the specific schedule, you need to take a look at the schedules first. Do you want to display all schedules?")
        print("1. Yes")
        print("2. No (Proceed to updating)")
        print("3. Back to main menu")
        display_choice1 = input("Enter choice: ")
        if display_choice1 == "1":
            display_schedule(schedules)
        elif display_choice1 == "2":
            update_code = input("Enter the course code of the schedule to be updated: ").upper()
            if update_code not in schedules:
                print("The course code you're looking for does not exist.")
                return
            else:
                for key, value in enumerate(schedules[update_code], start = 1):
                    print(f"Schedule #{key}:")
                    print(f"Course Title: {value['Title']}")
                    print(f"Day: Every {value['Day']}")
                    print(f"Time: starts at {value['Time']}")
                    print(f"Room: {value['Room']}")
                    
                
                updated_schedule = input("Enter the # of schedule to be updated: ")
                if not updated_schedule.isdigit():
                    print("Invalid. Please input a valid number!")
                    return
                schedule_num = int(updated_schedule)
                if schedule_num < 1 or schedule_num > len(schedules[update_code]):
                    print(f"Invalid. Please input number ranging from 1 to {len(schedules[update_code])}!")
                    return
                else:
                    target_schedule = schedules[update_code][schedule_num - 1]
                    
                    print(f"Update Schedule #{updated_schedule}:")
                    target_schedule["Title"] = input("Enter new course title: ")
                    target_schedule["Day"] = input("Enter new day: ")
                    
                    while True:  
                        update_hour = input("Enter new time in hours (24-hour format): ")
                        if update_hour.isdigit() and int(update_hour) >= 0 and int(update_hour) <= 23:
                            break
                        print("Invalid time input! Please enter numbers between 00-23 only.")
            
                    while True: 
                        update_minutes = input("Enter new time in minutes: ")
                        if update_minutes.isdigit() and int(update_minutes) >= 0 and int(update_minutes) <= 59:
                            break
                        print("Invalid time input! Please enter numbers between 00-59 only.")
                
                    target_schedule["Time"] = f"{update_hour.zfill(2)}:{update_minutes.zfill(2)}"
                    target_schedule["Room"] = input("Enter the newly designated room: ")
                    
                    print("The specified schedule is updated successfully.")
                    
        elif display_choice1 == "3":
            print("Going back to main menu.")
            return
        else:
            print("Invalid input! Please try again.")

       
def delete_schedule(schedules):
    while True:
        print("To delete the specific schedule, you need to take a look at the schedules first. Do you want to display all schedules?")
        print("1. Yes")
        print("2. No (Proceed to deleting)")
        print("3. Back to main menu")
        display_choice2 = input("Enter choice: ")
        if display_choice2 == "1":
            display_schedule(schedules)
        elif display_choice2 == "2":
            delete_code = input("Enter the course code of the schedule you want to delete: ").upper()
            if delete_code not in schedules:
                print("The course code of the schedule you want to delete does not exist.")
                return
            else:
                for i, entry in enumerate(schedules[delete_code], start = 1):
                    print(f"Schedule #{i}:")
                    print(f"Course Title: {entry['Title']}")
                    print(f"Day: Every {entry['Day']}")
                    print(f"Time: {entry['Time']}")
                    print(f"Room: {entry['Room']}")
                    
                deleted_schedule = input("Enter the # of schedule to be deleted: ")
                if not deleted_schedule.isdigit():
                    print("Invalid input. Please input a valid number!")
                    return
                scheduled_num = int(deleted_schedule)
                if scheduled_num < 1 or scheduled_num > len(schedules[delete_code]):
                    print(f"Invalid input! Please input numbers between 1 to {len(schedules[delete_code])}")
                    return
                else:
                    del schedules[delete_code][scheduled_num - 1]
                    if len(schedules[delete_code]) == 0:
                        del schedules[delete_code]
                        print(f"All schedules for the code {delete_code} are deleted successfully")
                    else:
                        print("The schedule is deleted successfully")
        elif display_choice2 == "3":
            print("Going back to main menu.")
            return
        else:
            print("Invalid input! Please try again.")
               
                       
                           
if __name__ == "__main__":
    schedules = load_schedules()
    while True:
        display_menu()
        choice = int(input("Enter choice: "))
        match choice:
            case 1:
                add_schedule(schedules)
                save_schedules()
            case 2:
                search_schedule(schedules)
            case 3:
                display_schedule(schedules)
            case 4:
                update_schedule(schedules)
                save_schedules()
            case 5:
                delete_schedule(schedules)
                save_schedules()
            case 6:
                print("Exiting Program...")
                break
            case _:
                print("Invalid input! Please try again.")
