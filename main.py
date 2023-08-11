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
