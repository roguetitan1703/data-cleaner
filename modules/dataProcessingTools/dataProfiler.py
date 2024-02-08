import pandas as pd
import json

class DataProfiler:
    def __init__(self):
        pass

    def read_data_file(self, file_path):
        """
        Read data from file and return as a pandas DataFrame.
        
        Parameters:
        file_path (str): Path to the data file.
        
        Returns:
        DataFrame: Data read from file as a pandas DataFrame.
        """
        if file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            data = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format. Only CSV and Excel files are supported.")
        
        return data

    def basic_data_profiling(self, data):
        """
        Perform basic data profiling and return results in JSON format.
        
        Parameters:
        data (DataFrame): Input data as a pandas DataFrame.
        
        Returns:
        str: JSON string containing data profiling results.
        """
        # Calculate total null values
        total_null_values = int(data.isnull().sum().sum())
        
        # Number of rows and columns
        num_rows, num_cols = data.shape
        
        # Compile results into a dictionary
        profiling_results = {
            "num_rows": int(num_rows),
            "num_cols": int(num_cols),
            "total_null_values": total_null_values,
        }
        
        # Convert dictionary to JSON string
        json_result = json.dumps(profiling_results, indent=4)
        
        return json_result

    def unique_values_per_column(self, data):
        """
        Get the count of unique values per column in the DataFrame.

        Parameters:
        data (DataFrame): Input data as a pandas DataFrame.

        Returns:
        dict: Dictionary containing column names as keys and unique value counts as values.
        """
        unique_values_counts = data.nunique()
        return unique_values_counts.to_dict()

    def data_types_per_column(self, data):
        """
        Get the data types of each column in the DataFrame.

        Parameters:
        data (DataFrame): Input data as a pandas DataFrame.

        Returns:
        dict: Dictionary containing column names as keys and data types as values.
        """
        data_types = data.dtypes
        return data_types.to_dict()


if __name__ == '__main__':
    data_profiler = DataProfiler()
    data = data_profiler.read_data_file('../../data/sample/LaptopData.csv')

    # Basic Data Profiling
    basic_profiling_result = data_profiler.basic_data_profiling(data)
    print("Basic Data Profiling:")
    print(basic_profiling_result)

    # Additional Profiling: Unique Values per Column
    unique_values_result = data_profiler.unique_values_per_column(data)
    print("\nUnique Values per Column:")
    print(unique_values_result)

    # Additional Profiling: Data Types per Column
    data_types_result = data_profiler.data_types_per_column(data)
    print("\nData Types per Column:")
    print(data_types_result)
