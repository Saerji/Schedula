import customtkinter as ctk
from tkinter import messagebox
from CTkTable import CTkTable
import logic_package

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("1100x600")
root.configure(fg_color = "#F8F4EC")

sidebar = ctk.CTkFrame(root, fg_color="#A8B89A", width=220)
sidebar.pack(side="left", fill="y")
sidebar.propagate(False)

main_area = ctk.CTkFrame(root, fg_color="#F8F4EC", corner_radius=0)
main_area.pack(side="left", fill="both", expand=True)

logo_frame = ctk.CTkFrame(sidebar, fg_color="#6F8F62", corner_radius=0, height=100)
logo_frame.pack(fill="x")
logo_frame.pack_propagate(False)

ctk.CTkLabel(logo_frame, text="🎓  BSU",
             font=ctk.CTkFont("Georgia", 20, "bold"),
             text_color="#F8F4EC").pack(expand=True)

ctk.CTkLabel(sidebar, text="Welcome!", font=("Arial",20,"bold")).pack(pady=10)
ctk.CTkFrame(sidebar, fg_color="#7A8B76", height=1).pack(fill="x", padx=15, pady=8) #divider

sidebar_nav = [
    ("Add Schedule", "add"),
    ("View Schedules", "view"),
    ("Search Schedule/s", "search"),
    ("Update Schedule", "update"),
    ("Delete Schedule", "delete")
]

for i, view in sidebar_nav:
    btn = ctk.CTkButton (sidebar,
                         text = f"{i}",
                         font = ("Georgia", 17, "bold"),
                         fg_color="transparent",
                         text_color="#F4F1E8",
                         hover_color="#2F4F3E",
                         corner_radius=3,
                         height=55,
                         command=lambda v=view : switch_view(v))
    btn.pack(fill="x", pady=10, padx=0)
    
exit_btn = ctk.CTkButton (sidebar,
                          text="Exit",
                          font = ("Georgia", 15, "bold"),
                          fg_color="transparent",
                          text_color="#F4F1E8",
                          hover_color="#2F4F3E",
                          command=None)
exit_btn.pack(pady=21, fill='x')

title_bar = ctk.CTkFrame (main_area,
                          fg_color="transparent", 
                          width=220, 
                          height=100,
                          corner_radius=0)
title_bar.propagate(False)
title_bar.pack(fill="x",side="top")

title = ctk.CTkLabel(title_bar,
                     text="INTEGRATED ACADEMIC SCHEDULE\nAND CLASSROOM RETRIEVAL SYSTEM",
                     font=("Georgia", 28, "bold"),
                     text_color="#2F4F3E",
                     justify="left",
                     anchor="w")
title.pack(padx=5,pady=0, side="left")

content_frame = ctk.CTkFrame(main_area, fg_color="#F8F4EC", corner_radius=0)
content_frame.pack(fill="both", expand=True, padx=20, pady=20)



def show_add_schedule():
    LABEL_WIDTH = 150
    PADY = 5
    ctk.CTkLabel(content_frame,
                 text="Add Schedule",
                 font=("Georgia", 24, "bold"),
                 text_color="#344E41").pack(padx=20, pady=20)
    ctk.CTkFrame(content_frame, fg_color="#7A8B76", height=1).pack(fill="x", padx=15, pady=10) #divider
    code_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
    code_frame.pack(anchor="w", padx=20, pady=5)
    ctk.CTkLabel(code_frame,
                 text="Enter course code:",
                 font=("Georgia", 14),
                 justify="left",
                 width=LABEL_WIDTH,
                 text_color="#344E41").pack(side="left", padx=(0, 10), pady=PADY)
    code_entry = ctk.CTkEntry(code_frame,
                 placeholder_text="e.g. CS 102",
                 font=("Georgia", 15),
                 width=350,
                 height=50)
    code_entry.pack(side="left")
    
    course_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
    course_frame.pack(anchor="w", padx=20, pady=PADY)
    ctk.CTkLabel(course_frame,
                 text="Enter course title:",
                 font=("Georgia", 14),
                 justify="left",
                 width=LABEL_WIDTH,
                 text_color="#344E41").pack(side="left", padx=(0, 10), pady=5)
    course_entry = ctk.CTkEntry(course_frame,
                 placeholder_text="e.g. Advanced Computer Programming",
                 font=("Georgia", 15),
                 width=350,
                 height=50)
    course_entry.pack(side="left")
    
    day_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
    day_frame.pack(anchor="w", pady=PADY, padx=20)
    ctk.CTkLabel(day_frame,
                 text="Choose day:",
                 font=("Georgia", 14),
                 justify="left",
                 width=LABEL_WIDTH,
                 text_color="#344E41").pack(side="left", padx=(0, 10), pady=5)
    selected_day = ctk.StringVar(value="Monday")
    day_entry = ctk.CTkOptionMenu(day_frame,
                      values=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
                              "Friday", "Saturday"],
                      variable=selected_day,
                      width=350,
                      height=50,
                      fg_color="#A8B89A",
                      button_color="#6F8F62",
                      button_hover_color="#4E7A57",
                      text_color="#244032",
                      dropdown_fg_color="#F8F5F0",
                      dropdown_text_color="#244032",
                      dropdown_hover_color="#DDE5D8")
    day_entry.pack(side="left")
    time_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
    time_frame.pack(anchor="w", pady=PADY, padx=20)
    ctk.CTkLabel(time_frame,
                 text="Enter Time:",
                 font=("Georgia", 14),
                 justify="left",
                 width=LABEL_WIDTH,
                 text_color="#344E41").pack(side="left", padx=(0, 10), pady=5)
    hour_values = [f"{h:02d}" for h in range(1, 24)]
    default_hour = ctk.StringVar(value="01")
    hour_entry = ctk.CTkOptionMenu(time_frame,
                      values=hour_values,
                      variable=default_hour,
                      width=100,
                      height=50,
                      fg_color="#A8B89A",
                      button_color="#6F8F62",
                      button_hover_color="#4E7A57",
                      text_color="#244032",
                      dropdown_fg_color="#F8F5F0",
                      dropdown_text_color="#244032",
                      dropdown_hover_color="#DDE5D8")
    hour_entry.pack(side="left")
    ctk.CTkLabel(time_frame,
                 text=":",
                 font=("Georgia", 14),
                 justify="left",
                 width=50,
                 text_color="#344E41").pack(side="left", padx=(0, 5), pady=5)
    minute_values = [f"{m:02d}" for m in range(60)]
    default_minute = ctk.StringVar(value="00")
    minute_entry = ctk.CTkOptionMenu(time_frame,
                      values=minute_values,
                      variable=default_minute,
                      width=100,
                      height=50,
                      fg_color="#A8B89A",
                      button_color="#6F8F62",
                      button_hover_color="#4E7A57",
                      text_color="#244032",
                      dropdown_fg_color="#F8F5F0",
                      dropdown_text_color="#244032",
                      dropdown_hover_color="#DDE5D8")
    minute_entry.pack(side="left")
    room_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
    room_frame.pack(anchor="w", padx=20, pady=PADY)
    ctk.CTkLabel(room_frame,
                 text="Enter room designation:",
                 font=("Georgia", 14),
                 justify="left",
                 width=LABEL_WIDTH,
                 text_color="#344E41").pack(side="left", padx=(0, 10), pady=8)
    room_entry = ctk.CTkEntry(room_frame,
                 placeholder_text="LAB3",
                 font=("Georgia", 15),
                 width=350,
                 height=50)
    room_entry.pack(side="left")
    
    def submit():
        course_code = code_entry.get().strip().upper()
        course_title = course_entry.get().strip()
        day = day_entry.get()
        time = f"{hour_entry.get()} : {minute_entry.get()}"
        room = room_entry.get()
        
        if not course_code or not course_title or not room:
            messagebox.showerror("Error", "Please fill in all fields!", parent=root)
            return
        
        logic_package.add_schedule(logic_package.schedules,
                                   course_code,
                                   course_title,
                                   day,
                                   time,
                                   room)
        messagebox.showinfo("Success" , f"The schedule for the couse {course_code} is addedd successfully.", parent=root)
        code_entry.delete(0, "end")
        course_entry.delete(0, "end")
        room_entry.delete(0, "end")
        selected_day.set("Monday")
        default_hour.set("00")
        default_minute.set("00")
    ctk.CTkButton(content_frame,
                  text="Add Schedule",
                  font=("Georgia", 15, "bold"),
                  fg_color="#6F8F62",
                  hover_color="#4E7A57",
                  text_color="#F8F4EC",
                  width=3000,
                  height=50,
                  corner_radius=6,
                  command=submit).pack(anchor="w", padx=20, pady=20)

def show_view_schedules():
    LABEL_WIDTH = 150
    PADY = 5
    ctk.CTkLabel(content_frame,
                 text="View Schedules",
                 font=("Georgia", 24, "bold"),
                 text_color="#344E41").pack(padx=20, pady=20)
    ctk.CTkFrame(content_frame, fg_color="#7A8B76", height=1).pack(fill="x", padx=15, pady=10) #divider
    
    data = logic_package.display_schedule(logic_package.schedules)
    
    if not data:
        ctk.CTkLabel(content_frame,
                 text='No schedules found. Add one in the "Add Schedules" section. :) ',
                 font=("Georgia", 24, "bold"),
                 text_color="#344E41").pack(padx=20, pady=20)
        
        return
    
    table_data = [["Course Code", "Course Title", "Day", "Time", "Room"]]
    
    for code, entries in data.items():
        first = True
        for entry in entries:
            if first:
                table_data.append([
                    code,
                    entry["Title"],
                    entry["Day"],
                    entry["Time"],
                    entry["Room"]
                ])
                first = False
                
            else:
                table_data.append([
                "",
                entry["Title"],
                entry["Day"],
                entry["Time"],
                entry["Room"]
            ])
            
    schedules_table = CTkTable(content_frame,
                               row=len(table_data),
                               column=5,
                               values=table_data,
                               header_color="#6B8F5E",
                               colors=["#A8B89A", "#A8B89A"],
                               hover_color="#EEF2EA",
                               font = ("Georgia", 13)
                              )
    schedules_table.pack(fill="both", expand=True, padx=20, pady=10)
    
def show_search_schedule():
    LABEL_WIDTH = 180
    PADY = 5
    ctk.CTkLabel(content_frame,
                 text="Search Schedules",
                 font=("Georgia", 24, "bold"),
                 text_color="#344E41").pack(padx=20, pady=20)
    ctk.CTkFrame(content_frame, fg_color="#7A8B76", height=1).pack(fill="x", padx=15, pady=10) #divider
    
    cat_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
    cat_frame.pack(anchor="w", padx=(15,10), pady=PADY)
    ctk.CTkLabel(cat_frame,
                 text="Choose search category:",
                 font=("Georgia", 14),
                 justify="left",
                 width=LABEL_WIDTH,
                 text_color="#344E41").pack(side="left", padx=(0, 10), pady=5)
    search_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
    search_frame.pack(anchor="w", padx=(15,10), fill="x")
    
    results_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
    results_frame.pack(fill="both", expand=True, padx=15, pady=10)
    
    def show_all():
        all_results = []
        for code, entries in logic_package.schedules.items():
            for entry in entries:
                all_results.append({"code": code, **entry})
        show_results(all_results)
    
    def show_results (data):
        for widget in results_frame.winfo_children():
            widget.destroy()
            
        if not data:
            ctk.CTkLabel(results_frame,
                 text='No schedule/s found with the indicated search. :) ',
                 font=("Georgia", 24, "bold"),
                 text_color="#344E41").pack(padx=20, pady=20)
            return
        
        table_data = [["Course Code", "Course Title", "Day", "Time", "Room"]]
    
        for entry in data:
            table_data.append([
                entry["code"],
                entry["Title"],
                entry["Day"],
                entry["Time"],
                entry["Room"]
            ])
            
        search_table = CTkTable(results_frame,
                            row=len(table_data),
                            column=5,
                            values=table_data,
                            header_color="#6B8F5E",
                            colors=["#A8B89A", "#A8B89A"],
                            hover_color="#EEF2EA",
                            font = ("Georgia", 13)
                            )
        search_table.pack(fill="both", expand=True, padx=20, pady=10)
        
    def change_searchbox(choice):
            for widget in search_frame.winfo_children():
                widget.destroy()
            
            show_all()
            
            if choice == "By Course Code":
                search_var = ctk.StringVar()
                search_var.trace("w", lambda *args: show_results(
                    logic_package.search_code(logic_package.schedules, search_var.get().strip().upper()) or []
                ))
                ctk.CTkEntry(search_frame,
                                        textvariable=search_var,
                                        placeholder_text="  🔍︎Search Course Code",
                                        font=("Georgia", 15),
                                        width=500,
                                        height=50).pack(side="left",pady = 5, fill="x", expand=True)
            elif choice == "By Course Title":
                search_var = ctk.StringVar()
                search_var.trace("w", lambda *args: show_results(
                    logic_package.search_title(logic_package.schedules, search_var.get().strip().upper()) or []
                ))
                ctk.CTkEntry(search_frame,
                                        placeholder_text="  🔍︎Search Course Title",
                                        textvariable=search_var,
                                        font=("Georgia", 15),
                                        width=500,
                                        height=50).pack(side="left",pady = 5, fill="x", expand=True)
            elif choice == "By Day":
                ctk.CTkLabel(search_frame,
                    text="Choose day:",
                    font=("Georgia", 14),
                    justify="left",
                    width=LABEL_WIDTH,
                    text_color="#344E41").pack(side="left", padx=(0, 10), pady=5)
                selected_day = ctk.StringVar(value="Monday")
                selected_day.trace("w", lambda *args: show_results(
                    logic_package.search_day(logic_package.schedules, selected_day.get()) or []
                ))
                ctk.CTkOptionMenu(search_frame,
                        values=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
                                "Friday", "Saturday"],
                        variable=selected_day,
                        width=350,
                        height=40,
                        fg_color="#A8B89A",
                        button_color="#6F8F62",
                        button_hover_color="#4E7A57",
                        text_color="#244032",
                        dropdown_fg_color="#F8F5F0",
                        dropdown_text_color="#244032",
                        dropdown_hover_color="#DDE5D8").pack(side="left")
                
            elif choice == "By Time":
                default_hour = ctk.StringVar(value="01")
                default_minute = ctk.StringVar(value="00")
                def update_time_search(*args):
                    time = f"{default_hour.get()} : {default_minute.get()}"
                    show_results(logic_package.search_time(logic_package.schedules, time) or [])
                default_hour.trace("w", update_time_search)
                default_minute.trace("w", update_time_search)
                
                ctk.CTkLabel(search_frame,
                    text="Enter Time:",
                    font=("Georgia", 14),
                    justify="left",
                    width=LABEL_WIDTH,
                    text_color="#344E41").pack(side="left", padx=(0, 10), pady=5)
                hour_values = [f"{h:02d}" for h in range(1, 24)]
                hour_entry = ctk.CTkOptionMenu(search_frame,
                        values=hour_values,
                        variable=default_hour,
                        width=100,
                        height=40,
                        fg_color="#A8B89A",
                        button_color="#6F8F62",
                        button_hover_color="#4E7A57",
                        text_color="#244032",
                        dropdown_fg_color="#F8F5F0",
                        dropdown_text_color="#244032",
                        dropdown_hover_color="#DDE5D8")
                hour_entry.pack(side="left")
                ctk.CTkLabel(search_frame,
                    text=":",
                    font=("Georgia", 14),
                    justify="left",
                    width=50,
                    text_color="#344E41").pack(side="left", padx=(0, 5), pady=5)
                minute_values = [f"{m:02d}" for m in range(60)]
                minute_entry = ctk.CTkOptionMenu(search_frame,
                        values=minute_values,
                        variable=default_minute,
                        width=100,
                        height=40,
                        fg_color="#A8B89A",
                        button_color="#6F8F62",
                        button_hover_color="#4E7A57",
                        text_color="#244032",
                        dropdown_fg_color="#F8F5F0",
                        dropdown_text_color="#244032",
                        dropdown_hover_color="#DDE5D8")
                minute_entry.pack(side="left")
            elif choice == "By Room":
                search_var = ctk.StringVar()
                search_var.trace("w", lambda *args: show_results(
                    logic_package.search_room(logic_package.schedules, search_var.get().strip().lower()) or []
                ))
                search_code = ctk.CTkEntry(search_frame,
                                        placeholder_text="  🔍︎Search Room",
                                        font=("Georgia", 15),
                                        textvariable=search_var,
                                        width=500,
                                        height=50)
                search_code.pack(side="left",pady = 5, fill="x", expand=True)
            
    cat_entry = ctk.CTkOptionMenu(cat_frame,
                                values=["By Course Code", "By Course Title", "By Day", "By Time", "By Room"],
                                command=change_searchbox,
                                width=350,
                                height=40,
                                fg_color="#A8B89A",
                                button_color="#6F8F62",
                                button_hover_color="#4E7A57",
                                text_color="#244032",
                                dropdown_fg_color="#F8F5F0",
                                dropdown_text_color="#244032",
                                dropdown_hover_color="#DDE5D8")
    cat_entry.pack(side="left")
    change_searchbox(cat_entry.get())
    
def show_update_schedule():
    LABEL_WIDTH = 180
    PADY = 5
    ctk.CTkLabel(content_frame,
                 text="Update Schedule",
                 font=("Georgia", 24, "bold"),
                 text_color="#344E41").pack(padx=20, pady=20)
    ctk.CTkFrame(content_frame, fg_color="#7A8B76", height=1).pack(fill="x", padx=15, pady=10) #divider
    ctk.CTkLabel(content_frame,
                 text="Click the schedule you would want to update:",
                 font=("Georgia", 14, "bold"),
                 text_color="#344E41").pack(anchor="w", padx=20, pady=10)
    
    def on_click(cell):
        if cell["row"] == 0:
            messagebox.showwarning("Warning", "Header cannot be edited!", parent=root)
            return
        if cell["column"] == 0:
            messagebox.showwarning("Warning", "Course code cannot be edited here!", parent=root)
            return
        
        popup = ctk.CTkToplevel(root)
        popup.title("Edit Cell")
        popup.geometry("400x200")
        popup.grab_set()
        
        column_names = ["Course Code", "Course Title", "Day", "Time", "Room"]
        clicked_column = column_names[cell["column"]]
        ctk.CTkLabel(popup,
                    text=f"Editing: {clicked_column}",
                    font=("Georgia", 14, "bold"),
                    text_color="#344E41").pack(padx=20, pady=(20, 5))
        ctk.CTkFrame(popup, fg_color="#7A8B76", height=1).pack(fill="x", padx=15, pady=10) #divider

        if clicked_column == "Course Title" or clicked_column == "Room":
            edit_var = ctk.StringVar(value=cell["value"])
            ctk.CTkEntry(popup,
                        textvariable=edit_var,
                        font=("Georgia", 13),
                        width=300,
                        height=40).pack(padx=20, pady=10)
        elif clicked_column == "Day":
            edit_var = ctk.StringVar(value=cell["value"])
            ctk.CTkOptionMenu(popup,
                            values=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
                                    "Friday", "Saturday"],
                            variable=edit_var,
                            width=350,
                            height=50,
                            fg_color="#A8B89A",
                            button_color="#6F8F62",
                            button_hover_color="#4E7A57",
                            text_color="#244032",
                            dropdown_fg_color="#F8F5F0",
                            dropdown_text_color="#244032",
                            dropdown_hover_color="#DDE5D8").pack()
        else:
            timeupdate_frame = ctk.CTkFrame(popup, fg_color="transparent")
            timeupdate_frame.pack()
            hour_values = [f"{h:02d}" for h in range(1, 24)]
            edit_var_hour = ctk.StringVar(value=cell["value"][:-5])
            edit_var_min = ctk.StringVar(value=cell["value"][5:])
            ctk.CTkOptionMenu(timeupdate_frame,
                            values=hour_values,
                            variable=edit_var_hour,
                            width=100,
                            height=50,
                            fg_color="#A8B89A",
                            button_color="#6F8F62",
                            button_hover_color="#4E7A57",
                            text_color="#244032",
                            dropdown_fg_color="#F8F5F0",
                            dropdown_text_color="#244032",
                            dropdown_hover_color="#DDE5D8").pack(side="left")
            ctk.CTkLabel(timeupdate_frame,
                        text=":",
                        font=("Georgia", 14),
                        justify="left",
                        width=50,
                        text_color="#344E41").pack(side="left", padx=(0, 5), pady=5)
            minute_values = [f"{m:02d}" for m in range(60)]
            ctk.CTkOptionMenu(timeupdate_frame,
                            values=minute_values,
                            variable=edit_var_min,
                            width=100,
                            height=50,
                            fg_color="#A8B89A",
                            button_color="#6F8F62",
                            button_hover_color="#4E7A57",
                            text_color="#244032",
                            dropdown_fg_color="#F8F5F0",
                            dropdown_text_color="#244032",
                            dropdown_hover_color="#DDE5D8").pack(side="left")
            
        def confirm():
            if clicked_column == "Time":
                new_value = f"{edit_var_hour.get()} : {edit_var_min.get()}"
            else:
                new_value = edit_var.get().strip()
            
            if not new_value:
                messagebox.showwarning("Error", "Field can not be empty!", parent=popup)
                return
            
            row_data = table_data[cell["row"]]
            code = row_data[0]
            num = None
            for i, entry in enumerate(logic_package.schedules[code]):
                if (entry["Title"] == row_data[1] and
                    entry["Day"]   == row_data[2] and
                    entry["Time"]  == row_data[3] and
                    entry["Room"]  == row_data[4]):
                    num = i + 1
                    break
                
            if num is None:
                messagebox.showerror("Error", "Schedule not found!", parent=popup)
                return
            
            title = new_value if clicked_column == "Course Title" else row_data[1]
            day   = new_value if clicked_column == "Day"          else row_data[2]
            time  = new_value if clicked_column == "Time"         else row_data[3]
            room  = new_value if clicked_column == "Room"         else row_data[4]
        
            logic_package.update_schedule(logic_package.schedules, code, num, title, day, time, room)
            
            messagebox.showinfo("Success", "Schedule updated successfully!", parent=popup)
            popup.destroy()

            switch_view("update")
            
        #----------------------Button---------------------------------------
        btn_frame = ctk.CTkFrame(popup, fg_color = "transparent")
        btn_frame.pack(pady=15) 
        
        ctk.CTkButton(btn_frame,
                text="Confirm",
                font=("Georgia", 15, "bold"),
                fg_color="#6F8F62",
                hover_color="#4E7A57",
                text_color="#F8F4EC",
                width=30,
                height=50,
                corner_radius=6,
                command=confirm).pack(side="left")
        
        ctk.CTkButton(btn_frame,
                text="Cancel",
                font=("Georgia", 15, "bold"),
                fg_color="#6F8F62",
                hover_color="#4E7A57",
                text_color="#F8F4EC",
                width=30,
                height=50,
                corner_radius=6,
                command=popup.destroy).pack(side="left", padx=10)
            
            
    update_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
    update_frame.pack(fill="both", expand=True, padx=15, pady=10)
    
    data = logic_package.display_schedule(logic_package.schedules)
    table_data = [["Course Code", "Course Title", "Day", "Time", "Room"]]
    for code, entries in data.items():
        for entry in entries:
            table_data.append([code,
                               entry["Title"],
                               entry["Day"],
                               entry["Time"],
                               entry["Room"]])
    CTkTable(update_frame,
             row=len(table_data),
             values=table_data,
             header_color="#6B8F5E",
            colors=["#A8B89A", "#A8B89A"],
            hover_color="#EEF2EA",
            font = ("Georgia", 13),
            command=on_click).pack(fill="both", expand=True, padx=20, pady=10)    
                    
def show_delete_schedule():
    ctk.CTkLabel(content_frame,
                 text="delete sched",
                 font=("Arial", 20, "bold")
                 ).pack()
    
def switch_view(view_name):
    for widget in content_frame.winfo_children():
        widget.destroy()    
        
    if view_name == "add":
        show_add_schedule()
    elif view_name == "view":
        show_view_schedules()
    elif view_name == "search":
        show_search_schedule()
    elif view_name == "update":
        show_update_schedule()
    elif view_name == "delete":
        show_delete_schedule()
        
root.mainloop()