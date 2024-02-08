import customtkinter as ctk
import tkinter.messagebox
from tkinter import filedialog
from tabulate import tabulate

import pandas as pd
import numpy as np
import json
from pprint import pprint

class HomeFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = ctk.CTkLabel(self, text="Home Frame", font=("Arial", 24))
        self.label.pack(expand=True)

class ImportFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create import button and place it in the center of the frame
        self.import_button = ctk.CTkButton(self, text="Import File", command=self.import_file)
        self.import_button.grid(row=0, column=0, pady=10)

    def import_file(self):
        # Open file dialog to select a file
        file_path = filedialog.askopenfilename()

        if file_path:
            # Display message box with file details
            filename = file_path.split("/")[-1]
            answer = tkinter.messagebox.askquestion("Import File", f"Do you want to import {filename}?", icon="question")

            if answer == "yes":
                # Perform import action
                self.import_button.configure(state="disabled")
                # Implement your import logic here
                print(f"File '{filename}' imported successfully!")

                # Clear the import frame
                self.clear_import_frame()

                # Display data exploration components
                self.dataset = file_path
                self.display_data_profiling()

    def clear_import_frame(self):
        # Destroy all widgets in the import frame
        for widget in self.winfo_children():
            widget.destroy()

    def display_data_profiling(self):
        # Sample data profiling results (replace with actual data)
        profiling_data = {
            "num_rows": 1303,
            "num_cols": 12,
            "total_null_values": 360,
            "unique_values_per_column": {
                'Unnamed: 0': 1273,
                'Company': 19,
                'TypeName': 6,
                'Inches': 25,
                'ScreenResolution': 40,
                'Cpu': 118,
                'Ram': 9,
                'Memory': 40,
                'Gpu': 110,
                'OpSys': 9,
                'Weight': 189,
                'Price': 777
            },
            "data_types_per_column": {
                'Unnamed: 0': 'float64',
                'Company': 'object',
                'TypeName': 'object',
                'Inches': 'object',
                'ScreenResolution': 'object',
                'Cpu': 'object',
                'Ram': 'object',
                'Memory': 'object',
                'Gpu': 'object',
                'OpSys': 'object',
                'Weight': 'object',
                'Price': 'float64'
            }
        }

        # Create labels to display data profiling results
        num_rows_label = ctk.CTkLabel(self, text=f"Number of Rows: {profiling_data['num_rows']}")
        num_rows_label.grid(row=1, column=0, sticky="w")

        num_cols_label = ctk.CTkLabel(self, text=f"Number of Columns: {profiling_data['num_cols']}")
        num_cols_label.grid(row=2, column=0, sticky="w")

        total_null_values_label = ctk.CTkLabel(self, text=f"Total Null Values: {profiling_data['total_null_values']}")
        total_null_values_label.grid(row=3, column=0, sticky="w")

        unique_values_frame = ctk.CTkFrame(self)
        unique_values_frame.grid(row=4, column=0, sticky="w")
        unique_values_label = ctk.CTkLabel(unique_values_frame, text="Unique Values per Column:")
        unique_values_label.pack()
        for i, (column, value) in enumerate(profiling_data["unique_values_per_column"].items()):
            label_text = f"{column}: {value}"
            label = ctk.CTkLabel(unique_values_frame, text=label_text)
            label.grid(row=i+1, column=0, sticky="w")

        data_types_frame = ctk.CTkFrame(self)
        data_types_frame.grid(row=1, column=1, sticky="w")
        data_types_label = ctk.CTkLabel(data_types_frame, text="Data Types per Column:")
        data_types_label.pack()
        for i, (column, dtype) in enumerate(profiling_data["data_types_per_column"].items()):
            label_text = f"{column}: {dtype}"
            label = ctk.CTkLabel(data_types_frame, text=label_text)
            label.grid(row=i+1, column=0, sticky="w")

class ActionFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = ctk.CTkLabel(self, text="Action Frame", font=("Arial", 24))
        self.label.pack(expand=True)

class ExportFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = ctk.CTkLabel(self, text="Export Frame", font=("Arial", 24))
        self.label.pack(expand=True)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pre Processor")
        self.geometry(f"{1100}x{580}")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        # Create sidebar frame
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="ns")

        # Create sidebar buttons
        self.sidebar_button_home = ctk.CTkButton(self.sidebar_frame, text="Home", command=self.show_home_frame)
        self.sidebar_button_home.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        self.sidebar_button_import = ctk.CTkButton(self.sidebar_frame, text="Import", command=self.show_import_frame)
        self.sidebar_button_import.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.sidebar_button_action = ctk.CTkButton(self.sidebar_frame, text="Action", command=self.show_action_frame)
        self.sidebar_button_action.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.sidebar_button_export = ctk.CTkButton(self.sidebar_frame, text="Export", command=self.show_export_frame)
        self.sidebar_button_export.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        
        self.sidebar_buttons = [self.sidebar_button_home, self.sidebar_button_import, self.sidebar_button_action, self.sidebar_button_export]

        # Create main frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, sticky="nsew")

        # Initially show the home frame
        self.show_home_frame()

    def show_home_frame(self):
        self.clear_main_frame()
        self.home_frame = HomeFrame(self.main_frame)
        self.home_frame.pack(fill="both", expand=True)
        self.set_button_state(self.sidebar_button_home)  # Set the button state to disabled

    def show_import_frame(self):
        self.clear_main_frame()
        self.import_frame = ImportFrame(self.main_frame)
        self.import_frame.pack(fill="both", expand=True)
        self.set_button_state(self.sidebar_button_import)  # Set the button state to disabled
        
    def show_action_frame(self):
        self.clear_main_frame()
        self.action_frame = ActionFrame(self.main_frame)
        self.action_frame.pack(fill="both", expand=True)
        self.set_button_state(self.sidebar_button_action)  # Set the button state to disabled

    def show_export_frame(self):
        self.clear_main_frame()
        self.export_frame = ExportFrame(self.main_frame)
        self.export_frame.pack(fill="both", expand=True)
        self.set_button_state(self.sidebar_button_export)  # Set the button state to disabled

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def set_button_state(self, clicked_button):
        for button in self.sidebar_buttons:
            if button == clicked_button:
                button.configure(state="disabled", fg_color=("#fff"), text_color_disabled="#000")
            else:
                button.configure(state="normal", fg_color=("#3a7ebf"))

if __name__ == "__main__":
    app = App()
    app.mainloop()
