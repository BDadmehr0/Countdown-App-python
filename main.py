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
