import customtkinter as ctk
from tkinter import messagebox
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
    ("Search Schedule/s", "search"),
    ("View Schedules", "view"),
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
                  width=300,
                  height=45,
                  corner_radius=6,
                  command=submit).pack(anchor="w", padx=20, pady=20)

def show_search_schedule():
    ctk.CTkLabel(content_frame,
                 text="Search",
                 font=("Arial", 20, "bold")
                 ).pack()

def show_view_schedules():
    ctk.CTkLabel(content_frame,
                 text="View",
                 font=("Arial", 20, "bold")
                 ).pack()

def show_update_schedule():
    ctk.CTkLabel(content_frame,
                 text="update Sched",
                 font=("Arial", 20, "bold")
                 ).pack()
    
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
    elif view_name == "search":
        show_search_schedule()
    elif view_name == "view":
        show_view_schedules()
    elif view_name == "update":
        show_update_schedule()
    elif view_name == "delete":
        show_delete_schedule()
        
        
root.mainloop()
    