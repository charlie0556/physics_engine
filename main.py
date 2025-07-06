#Imports are listed here 

import tkinter as tk
from tkinter import ttk

#Global variables are listed here




#The root is created here

physics_engine = tk.Tk()
physics_engine.title("Physics Engine")
physics_engine.geometry("800x600")
physics_engine.resizable(False, False)

#Frames are created here
WelcomeFrame = tk.Frame(physics_engine, width=800, height=600, bg="lightblue")
WelcomeFrame.grid(row=0, column=0, sticky="nsew")
WelcomeFrame.grid_propagate(False)

New_simulationFrame = tk.Frame(physics_engine, width=800, height=600, bg="lightgreen")
New_simulationFrame.grid(row=0, column=0, sticky="nsew")
New_simulationFrame.grid_propagate(False)
New_simulationFrame.grid_remove()

Load_simulationFrame = tk.Frame(physics_engine, width=800, height=600, bg="lightyellow")
Load_simulationFrame.grid(row=0, column=0, sticky="nsew")
Load_simulationFrame.grid_propagate(False)
Load_simulationFrame.grid_remove()

tutorialFrame = tk.Frame(physics_engine, width=800, height=600, bg="lightgrey")
tutorialFrame.grid(row=0, column=0, sticky="nsew")
tutorialFrame.grid_propagate(False)
tutorialFrame.grid_remove()

Learn_about_spaceFrame = tk.Frame(physics_engine, width=800, height=600, bg="lightcoral")
Learn_about_spaceFrame.grid(row=0, column=0, sticky="nsew")
Learn_about_spaceFrame.grid_propagate(False)
Learn_about_spaceFrame.grid_remove()

DonateFrame = tk.Frame(physics_engine, width=800, height=600, bg="lightpink")
DonateFrame.grid(row=0, column=0, sticky="nsew")
DonateFrame.grid_propagate(False)
DonateFrame.grid_remove()
#Functions are defined here

def exit_program():
    physics_engine.quit()
    physics_engine.destroy()


def start_new_simulation():
    WelcomeFrame.grid_remove()
    New_simulationFrame.grid()

def load_simulation():
    WelcomeFrame.grid_remove()
    Load_simulationFrame.grid()
    
def settings_option():
    selected_option = selected_setting.get()
    if selected_option == "Tutorial":
        WelcomeFrame.grid_remove()
        tutorialFrame.grid()
    elif selected_option == "Learn About Space":
        WelcomeFrame.grid_remove()
        Learn_about_spaceFrame.grid()
    elif selected_option == "Donate":
        WelcomeFrame.grid_remove()
        DonateFrame.grid()
    else:
        pass


        # Add code to open donation page

#Front end is created here

welcome = tk.Label(WelcomeFrame, text="Welcome to Solar Physics Calculator ", font=("Arial", 24), bg="lightblue")
welcome.grid(row=0, column=0, padx=20, pady=20)

exit_button = tk.Button(WelcomeFrame, text="Exit", command=exit_program, font=("Arial", 16), bg="red", fg="white")
exit_button.place(x=20, y=550) 

information_on_what_engine_is = '''This is a physics engine that allows you to explore the physics of the solar system.'''

info_label = tk.Label(WelcomeFrame, text=information_on_what_engine_is, font=("Arial", 16), bg="lightblue", wraplength=600)
info_label.place(x=20, y=100)  

start_new_simulation_button = tk.Button(WelcomeFrame, text="Start New Simulation", command=start_new_simulation, font=("Arial", 16), bg="lightgreen", fg="black")
start_new_simulation_button.place(x=20, y=200) 

load_simulation_button = tk.Button(WelcomeFrame, text="Load Simulation", command=load_simulation, font=("Arial", 16), bg="lightyellow", fg="black")
load_simulation_button.place(x=20, y=300)

selected_setting = tk.StringVar()
selected_setting.set("Settings")

settings_selector = ttk.Combobox(WelcomeFrame, values=["Tutorial", "Learn About Space", "Donate"], font=("Arial", 16), state="readonly", textvariable=selected_setting)
settings_selector.set("Settings")
settings_selector.place(x=20, y=400)
settings_selector.bind("<<ComboboxSelected>>", lambda event: settings_option())


version_label = tk.Label(WelcomeFrame, text="Version 1.0", font=("Arial", 12), bg="lightblue")
version_label.place(x=700, y=570) 




















#The loop ends here
physics_engine.mainloop()






