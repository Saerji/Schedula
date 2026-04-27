import json
import os

def load_schedules():
    if os.path.exists("schedules.json"):
        with open("schedules.json", "r") as file:
            return json.load(file)
    return {}

def save_schedules(schedules):
    with open("schedules.json", "w") as file:
        json.dump(schedules, file, indent = 4)
    
def add_schedule(schedules, course_title, schedule_day, schedule_time, schedule_room, course_code):   
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
    save_schedules(schedules)

    #-----------------------------------SEARCH BY COURSE CODE-------------------------------------------
def search_code(schedules, search_code): 
    if search_code in schedules:
        return schedules[search_code]
    return None
            
    
    #------------------------------------SEARCH BY TIME-------------------------------------------------
def search_time (schedules, search_time): 
    results = []
    for code, entries in schedules.items():
        for entry in entries:
            if search_time == entry["Time"]:
                results.append({"code" : code, **entry})
    return results        
    #--------------------------------------SEARCH BY ROOM------------------------------------------------
def search_room (schedules, search_room): 
    results = []
    for code, entries in schedules.items():
        for entry in entries:
            if search_room == entry["Room"].upper():
                results.append({"code" : code, **entry})
    return results        

def display_schedule(schedules):
    if not schedules:
        return None
    return schedules

def update_schedule(schedules, code, num, title, day, time, room):
    target = schedules[code][num - 1]

    if title: target["Title"] = title
    if day:   target["Day"]   = day
    if time:  target["Time"]  = time
    if room:  target["Room"]  = room

    save_schedules(schedules)

       

def delete_schedule(schedules, code, num):
    del schedules[code][num - 1]

    if len(schedules[code]) == 0:
        del schedules[code]
        save_schedules(schedules)
        return "all_deleted"    # ✅ tells GUI all schedules for that code are gone

    save_schedules(schedules)
    return "deleted" 


schedules = load_schedules()