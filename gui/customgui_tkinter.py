import customtkinter as ctk
import tkinter as tk
import webview, os, sys, time, threading
from pprint import pprint

project_root = os.getcwd()
sys.path.append(project_root)

data_path = f'{project_root}/data/'
# Import local modules
from modules.dataProcessingTools import dataProfiler


class HomeFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = ctk.CTkLabel(self, text="Home Frame", font=("Arial", 24))
        self.label.pack(expand=True)


class ImportFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create import button and place it in the center of the frame
        self.import_button = ctk.CTkButton(self, text="Import File", command=self.import_file, font=("Arial", 16))
        self.import_button.place(relx=0.5, rely=0.5, anchor="center")

    def import_file(self):
        # Open file dialog to select a file
        file_path = tk.filedialog.askopenfilename(filetypes=[
            ("CSV Files", "*.csv"),
            ("Excel Files", "*.xlsx")])

        if file_path:
            # Display message box with file details
            self.filename = file_path.split("/")[-1]
            answer = tk.messagebox.askquestion("Import File", f"Do you want to import {self.filename}?", icon="question")

            if answer == "yes":
                # Perform import action
                print(f"File '{self.filename}' imported successfully!")

                # Display data exploration components
                self.dataset = dataProfiler.DataProfiler.read_data_file(file_path)
                
                self.display_data_profiling()

    def clear_import_frame(self):
        # Destroy all widgets in the import frame
        for widget in self.winfo_children():
            widget.destroy()

    def generate_data_profiling_report(self):
        file_name = f"{self.filename[:len(self.filename)-self.filename[::-1].find('.')-1]}.html"
        self.profiling_report_html = f"{project_root}/gui/assets/{file_name}"
        
        # Create the report
        dataProfiler.DataProfiler.pandas_profiling_report(self.dataset, self.profiling_report_html, file_format='html')
        
        self.after(1, self.render_data_profiling_report)
        
    def render_data_profiling_report(self):
        self.progress_bar.stop()
        self.progress_bar.destroy()
        self.wait_label.destroy()
        # Display data profiling report
        webview.create_window("Data Profiling Report", self.profiling_report_html, width=800, height=600)
        webview.start()
    
    def generate_complex_report(self):
        # Create a progress bar
        for widget in self.frame_4.winfo_children():
            widget.destroy()
            
        self.more_complex_button.destroy()
        self.more_complex_label.destroy()
        # Label indicating report generation
        self.wait_label = ctk.CTkLabel(self.frame_4, text="Wait while we generate the report")
        self.wait_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(self.frame_4, orientation="horizontal")
        self.progress_bar.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.progress_bar.start()
        
        # Create a thread for running the rendering function
        threading.Thread(target=self.generate_data_profiling_report).start()
      
    def display_data_profiling(self):
        # Sample data profiling results (replace with actual data)
        self.profiling_data = dataProfiler.DataProfiler.all_data_profiling(self.dataset)
        # pprint(profiling_data)
        
        # Create a scrollable frame for basic per column
        self.scrollable_frame_1 = ctk.CTkScrollableFrame(self, width=200, height=200)
        self.scrollable_frame_1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.data_frame_1 = ctk.CTkFrame(self.scrollable_frame_1, corner_radius=5)
        self.data_frame_1.pack(fill="x", padx=10, pady=5)

        # Display number of rows, columns, and null values
        self.num_rows_label = ctk.CTkLabel(self.data_frame_1, text=f"Number of Rows: {self.profiling_data['num_rows']}")
        self.num_rows_label.grid(row=0, column=0, sticky="w")

        self.num_cols_label = ctk.CTkLabel(self.data_frame_1, text=f"Number of Columns: {self.profiling_data['num_cols']}")
        self.num_cols_label.grid(row=1, column=0, sticky="w")

        self.total_null_values_label = ctk.CTkLabel(self.data_frame_1, text=f"Total Null Values: {self.profiling_data['total_null_values']}")
        self.total_null_values_label.grid(row=2, column=0, sticky="w")

        # Create a scrollable frame for unique values per column
        self.scrollable_frame_2 = ctk.CTkScrollableFrame(self, width=200, height=200)
        self.scrollable_frame_2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.data_frame_2 = ctk.CTkFrame(self.scrollable_frame_2, corner_radius=5)
        self.data_frame_2.pack(fill="x", padx=10, pady=5)

        # Display unique values per column
        self.unique_values_label = ctk.CTkLabel(self.data_frame_2, text="Unique Values per Column:")
        self.unique_values_label.pack(anchor="w")
        for i, (column, value) in enumerate(self.profiling_data["unique_values_per_column"].items()):
            label_text = f"{column}: {value}"
            label = ctk.CTkLabel(self.data_frame_2, text=label_text)
            label.pack(anchor="w")

        # Create a scrollable frame for data types per column
        self.scrollable_frame_3 = ctk.CTkScrollableFrame(self, width=200, height=200)
        self.scrollable_frame_3.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        self.data_frame_3 = ctk.CTkFrame(self.scrollable_frame_3, corner_radius=5)
        self.data_frame_3.pack(fill="x", padx=10, pady=(5, 10))

        # Display data types per column
        self.data_types_label = ctk.CTkLabel(self.data_frame_3, text="Data Types per Column:")
        self.data_types_label.pack(anchor="w")
        for i, (column, dtype) in enumerate(self.profiling_data["data_types_per_column"].items()):
            label_text = f"{column}: {dtype}"
            label = ctk.CTkLabel(self.data_frame_3, text=label_text)
            label.pack(anchor="w")
            
        
        self.frame_4 = ctk.CTkFrame(self, width=200, height=200, corner_radius=5)
        self.frame_4.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

        # Add a label and button asking the user if they want to generate more complex data profiling
        self.more_complex_label = ctk.CTkLabel(self.frame_4, text="Do you want to generate a more complex data profiling report?")
        self.more_complex_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        

        self.more_complex_button = ctk.CTkButton(self.frame_4, text="Generate Complex Report", command=self.generate_complex_report)
        self.more_complex_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
  


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
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Set the size of the GUI to the screen width and height
        self.geometry(f"{screen_width}x{screen_height}-8+0")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        
        # Create tab view with increased padding
        self.tab_view = ctk.CTkTabview(master=self)
        self.tab_view.pack(fill="both", expand=True)

        # Add tabs
        self.tab_home = self.tab_view.add("Home")
        self.tab_import = self.tab_view.add("Import")
        self.tab_action = self.tab_view.add("Action")
        self.tab_export = self.tab_view.add("Export")

        # Display frames in respective tabs
        self.home_frame = HomeFrame(self.tab_home)
        self.home_frame.pack(fill="both", expand=True)

        self.import_frame = ImportFrame(self.tab_import)
        self.import_frame.pack(fill="both", expand=True)

        self.action_frame = ActionFrame(self.tab_action)
        self.action_frame.pack(fill="both", expand=True)

        self.export_frame = ExportFrame(self.tab_export)
        self.export_frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()
