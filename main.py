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
