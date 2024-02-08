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

        # Create a scrollable frame
        scrollable_frame = ctk.CTkScrollableFrame(self, width=200, height=200)
        scrollable_frame.grid(row=0, column=0, padx=20, pady=10, sticky="nw")

        # Create a frame for number of rows, columns, and null values
        data_frame_1 = ctk.CTkFrame(scrollable_frame, corner_radius=5)
        data_frame_1.pack(fill="x", padx=10, pady=(10, 5))
        
        # Display number of rows, columns, and null values
        num_rows_label = ctk.CTkLabel(data_frame_1, text=f"Number of Rows: {profiling_data['num_rows']}")
        num_rows_label.pack(anchor="w")

        num_cols_label = ctk.CTkLabel(data_frame_1, text=f"Number of Columns: {profiling_data['num_cols']}")
        num_cols_label.pack(anchor="w")

        total_null_values_label = ctk.CTkLabel(data_frame_1, text=f"Total Null Values: {profiling_data['total_null_values']}")
        total_null_values_label.pack(anchor="w")

        # Create a frame for unique values per column
        data_frame_2 = ctk.CTkFrame(scrollable_frame, corner_radius=5)
        data_frame_2.pack(fill="x", padx=10, pady=5)

        # Display unique values per column
        unique_values_label = ctk.CTkLabel(data_frame_2, text="Unique Values per Column:")