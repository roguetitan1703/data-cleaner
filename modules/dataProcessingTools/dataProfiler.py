import pandas as pd
from ydata_profiling import ProfileReport
import json

class DataProfiler:
    @staticmethod
    def read_data_file(file_path):
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

    @staticmethod
    def basic_data_profiling(data):
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

    @staticmethod
    def unique_values_per_column(data):
        """
        Get the count of unique values per column in the DataFrame.

        Parameters:
        data (DataFrame): Input data as a pandas DataFrame.

        Returns:
        dict: Dictionary containing column names as keys and unique value counts as values.
        """
        unique_values_counts = data.nunique()
        return unique_values_counts.to_dict()

    @staticmethod
    def data_types_per_column(data):
        """
        Get the data types of each column in the DataFrame.

        Parameters:
        data (DataFrame): Input data as a pandas DataFrame.

        Returns:
        dict: Dictionary containing column names as keys and data types as values.
        """
        data_types = data.dtypes
        return data_types.to_dict()
    
    @classmethod
    def all_data_profiling(cls, data):
        """
        Perform all data profiling tasks and return results in a dictionary.

        Parameters:
        data (DataFrame): Input data as a pandas DataFrame.

        Returns:
        dict: Dictionary containing all data profiling results.
        """
        profiling_results = {}

        # Basic Data Profiling
        basic_profiling_result = cls.basic_data_profiling(data)
        profiling_results = json.loads(basic_profiling_result)

        # Unique Values per Column
        unique_values_result = cls.unique_values_per_column(data)
        profiling_results["unique_values_per_column"] = unique_values_result

        # Data Types per Column
        data_types_result = cls.data_types_per_column(data)
        profiling_results["data_types_per_column"] = data_types_result

        return profiling_results
    
    @staticmethod
    def pandas_profiling_report(data, output_file, file_format='html'):
        """
        Generate a pandas-profiling report for the input data and save it to the specified file.

        Parameters:
        data (DataFrame): Input data as a pandas DataFrame.
        output_file (str): Output file path where the report will be saved.
        file_format (str, optional): File format for the output report ('html' or 'json'). Defaults to 'html'.
        """
        if file_format == 'html':
            profile = ProfileReport(data)
            profile.to_file(output_file)
            return output_file
        
        elif file_format == 'json':
            profile = ProfileReport(data)
            profile.to_file(output_file)
            return output_file
        
        else:
            raise ValueError("Unsupported file format. Only 'html' and 'json' are supported.")
        

if __name__ == '__main__':
    file_path = '../../data/sample/food_coded.csv'
    data = DataProfiler.read_data_file(file_path)
    
    # Generate and save pandas-profiling report as HTML
    DataProfiler.pandas_profiling_report(data, 'output_report.html', file_format='html')
    
    # Generate and save pandas-profiling report as JSON
    DataProfiler.pandas_profiling_report(data, 'output_report.json', file_format='json')
