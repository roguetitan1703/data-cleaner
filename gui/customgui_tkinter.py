import customtkinter as ctk
import tkinter.messagebox
from tkinter import filedialog, ttk
import tkinter as tk
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
        self.import_button.place(relx=0.5, rely=0.5, anchor="center")

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

        # Create a scrollable frame for basic  per column
        scrollable_frame_1 = ctk.CTkScrollableFrame(self, width=200, height=200)
        scrollable_frame_1.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

        data_frame_1 = ctk.CTkFrame(scrollable_frame_1, corner_radius=5)
        data_frame_1.pack(fill="x", padx=10, pady=5)

        # Display number of rows, columns, and null values
        num_rows_label = ctk.CTkLabel(data_frame_1, text=f"Number of Rows: {profiling_data['num_rows']}")
        num_rows_label.grid(row=0, column=0, sticky="w")

        num_cols_label = ctk.CTkLabel(data_frame_1, text=f"Number of Columns: {profiling_data['num_cols']}")
        num_cols_label.grid(row=1, column=0, sticky="w")

        total_null_values_label = ctk.CTkLabel(data_frame_1, text=f"Total Null Values: {profiling_data['total_null_values']}")
        total_null_values_label.grid(row=2, column=0, sticky="w")

        # Create a scrollable frame for unique values per column
        scrollable_frame_2 = ctk.CTkScrollableFrame(self, width=200, height=200)
        scrollable_frame_2.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")

        data_frame_2 = ctk.CTkFrame(scrollable_frame_2, corner_radius=5)
        data_frame_2.pack(fill="x", padx=10, pady=5)

        # Display unique values per column
        unique_values_label = ctk.CTkLabel(data_frame_2, text="Unique Values per Column:")
        unique_values_label.pack(anchor="w")
        for i, (column, value) in enumerate(profiling_data["unique_values_per_column"].items()):
            label_text = f"{column}: {value}"
            label = ctk.CTkLabel(data_frame_2, text=label_text)
            label.pack(anchor="w")

        # Create a scrollable frame for data types per column
        scrollable_frame_3 = ctk.CTkScrollableFrame(self, width=200, height=200)
        scrollable_frame_3.grid(row=0, column=2, padx=20, pady=10, sticky="nsew")

        data_frame_3 = ctk.CTkFrame(scrollable_frame_3, corner_radius=5)
        data_frame_3.pack(fill="x", padx=10, pady=(5, 10))

        # Display data types per column
        data_types_label = ctk.CTkLabel(data_frame_3, text="Data Types per Column:")
        data_types_label.pack(anchor="w")
        for i, (column, dtype) in enumerate(profiling_data["data_types_per_column"].items()):
            label_text = f"{column}: {dtype}"
            label = ctk.CTkLabel(data_frame_3, text=label_text)
            label.pack(anchor="w")



    def display_data_profiling_frame(self, scrollable_frame, data, is_unique_values=False, is_data_types=False):
        # Create a frame for the data
        data_frame = ctk.CTkFrame(scrollable_frame, corner_radius=5)
        data_frame.pack(fill="both", padx=10, pady=10)

        # Display data profiling results based on the type
        if is_unique_values:
            label_text = "Unique Values per Column:"
            data_dict = data
        elif is_data_types:
            label_text = "Data Types per Column:"
            data_dict = data
        else:
            label_text = "Number of Rows, Columns, and Total Null Values:"
            data_dict = data

        # Display label
        label = ctk.CTkLabel(data_frame, text=label_text, font=("Arial", 12, "bold"))
        label.pack(anchor="w", padx=10, pady=5)

        # Display data
        for key, value in data_dict.items():
            text = f"{key}: {value}"
            label = ctk.CTkLabel(data_frame, text=text)
            label.pack(anchor="w", padx=10, pady=2)



        
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
