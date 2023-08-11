# import tkinter as tk
import customtkinter as ctk

# from tkinter import messagebox 
# or 
from CTkMessagebox import CTkMessagebox
import random

class CountdownApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown App")
        self.root.resizable(height=False, width=False)
        
        pad = 3
        self._geom = '200x200+0+0'
        root.geometry("{0}x{1}+0+0".format(
            root.winfo_screenwidth()-pad, root.winfo_screenheight()-pad))
        root.bind('<Escape>', self.toggle_geom)

        self.label = ctk.CTkLabel(self.root, text_color='red')
        self.label.pack(padx=20, pady=10, anchor='center')

        self.load_last_time()  # Load the last saved time
        self.start_countdown()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # Set the closing event handler

        # Create a Font instance with Roboto 15
        self.custom_font = ctk.CTkFont(family="Roboto", size=37)

        # Apply the custom font to the label
        self.label.configure(font=self.custom_font)

    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

    def start_countdown(self):
        try:
            years = random.randint(60, 70)
            total_seconds = years * 365 * 24 * 60 * 60
            if self.last_time is not None:  # Use the last saved time if available
                total_seconds = self.last_time
            self.remaining_seconds = total_seconds
            self.update_countdown()
        except ValueError:
            self.show_error("Invalid Input", "Please enter a valid number of years.")

    def update_countdown(self):
        if self.remaining_seconds > 0:
            remaining_years = self.remaining_seconds // (365 * 24 * 60 * 60)
            remaining_days = (self.remaining_seconds % (365 * 24 * 60 * 60)) // (24 * 60 * 60)
            remaining_hours = ((self.remaining_seconds % (365 * 24 * 60 * 60)) % (24 * 60 * 60)) // (60 * 60)
            remaining_minutes = (((self.remaining_seconds % (365 * 24 * 60 * 60)) % (24 * 60 * 60)) % (60 * 60)) // 60
            remaining_seconds = (((self.remaining_seconds % (365 * 24 * 60 * 60)) % (24 * 60 * 60)) % (60 * 60)) % 60

            # Place the numbers of years, days, hours, minutes, and seconds on top of each other
            self.label.configure(text=f"\n{remaining_years} yrs\n\n\n{remaining_days} day\n\n\n{remaining_hours:02} hrs\n\n\n{remaining_minutes:02} min\n\n\n{remaining_seconds:02} sec")
            self.remaining_seconds -= 1
            self.root.after(1000, self.update_countdown)
        else:
            self.show_info("Countdown Finished", "Countdown has finished!")
            self.e()
            self.last_time = None  # Reset the last saved time
            self.save_last_time()  # Save the last time after countdown finishes

    def e(self):
        exit()
