from customtkinter import (
    CTk,
    CTkButton,
    CTkEntry,
    CTkFont,
    CTkImage,
    CTkLabel,
    CTkOptionMenu,
    CTkScrollableFrame,
    CTkToplevel,
    filedialog,
    set_appearance_mode,    
    set_default_color_theme,
)
import customtkinter
import os

timeString = ""
timeList = []

def add_time():
    try:
        timeInputValue = timeInput.get()
        int(timeInputValue)
        global timeString
        global timeList
        timeString += timeInputValue + " minute(s) per mile\n"
        timeList.append(int(timeInputValue))
        timeInput.delete(0, len(timeInput.get()))
        addtimeErrorLabel.configure(text="Time added successfully.", text_color="Green")
        timeDisplayLabel.configure(text=timeString)
        
        # Calculate fastest, slowest, average.
        fastestTime = fastest_time()
        slowestTime = slowest_time()
        averageTime = average_time()
        slowestTimeLabel.configure(text="Slowest Time: " + str(slowestTime) + " minute(s) per mile")
        fastestTimeLabel.configure(text="Fastest Time: " + str(fastestTime) + " minute(s) per mile")
        averageTimeLabel.configure(text="Average Time: " + str(round(averageTime,2)) + " minute(s) per mile")

    except:
        addtimeErrorLabel.configure(text="An error occurred. Make sure your input is a number. Please try again.", text_color="Red")

    
def average_time():
    global timeList
    totaltime = 0
    for time in timeList:
        totaltime += time
    return totaltime / len(timeList)
def slowest_time():
    global timeList
    slowestTime = timeList[0]
    for time in timeList:
        if time < slowestTime:
            slowestTime = time
    return slowestTime

def fastest_time():
    global timeList
    fastestTime = timeList[0]
    for time in timeList:
        if time > fastestTime:
            fastestTime = time
    return fastestTime

app = customtkinter.CTk()
app.title("time Tracker")
app.geometry("400x400")
app.grid_columnconfigure(0, weight=1)
customtkinter.set_appearance_mode("dark")
big = CTkFont(size=70, family="Segoe UI", weight="bold")
instruction = CTkFont(size=20, family="Segoe UI")
error = CTkFont(size=20, family="Segoe UI", weight="bold")
time = CTkFont(size=12, family="Segoe UI", weight="bold")


titleLabel = customtkinter.CTkLabel(app, text="Time Tracker", fg_color="transparent", font=big)
titleLabel.grid(row=0, column=0, padx=20, pady=20)

instructionLabel = customtkinter.CTkLabel(app, text="Enter time per mile in minutes", fg_color="transparent", font=instruction)
instructionLabel.grid(row=1, column=0, padx=20, pady=20)

timeDisplayFrame = customtkinter.CTkScrollableFrame(app, orientation="vertical",width=600)
timeDisplayFrame.grid(row=2, column=0, padx=0, pady=30)

timeDisplayLabel = customtkinter.CTkLabel(timeDisplayFrame, text="", font=time)
timeDisplayLabel.grid(row=0, column=0, padx=20, pady=20)


timeInput = customtkinter.CTkEntry(app, width=400)
timeInput.grid(row=3, column=0, padx=20, pady=0)

addtimeButton = customtkinter.CTkButton(app, text="Add Time", command=add_time)
addtimeButton.grid(row=4, column=0, padx=20, pady=10)

addtimeErrorLabel = customtkinter.CTkLabel(app, text="", fg_color="transparent", font=error, text_color="Red")
addtimeErrorLabel.grid(row=5, column=0, padx=0, pady=0)

slowestTimeLabel = customtkinter.CTkLabel(app, text="Slowest Time:", fg_color="transparent", font=error)
slowestTimeLabel.grid(row=6, column=0, padx=0, pady=10)
averageTimeLabel = customtkinter.CTkLabel(app, text="Average Time:", fg_color="transparent", font=error)
averageTimeLabel.grid(row=7, column=0, padx=0, pady=10)
fastestTimeLabel = customtkinter.CTkLabel(app, text="Fastest Time:", fg_color="transparent", font=error)
fastestTimeLabel.grid(row=8, column=0, padx=0, pady=10)

app.mainloop()
