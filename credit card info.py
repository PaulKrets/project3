import pandas as pd
import requests
import matplotlib.pyplot as plt
class DataLoader:
    def __init__(self):
        self.data = None

    def load_csv(self, file_path):
        self.data = pd.read_csv(file_path)

    def load_json(self, file_path):
        self.data = pd.read_json(file_path)

    def load_api(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            self.data = pd.DataFrame(response.json())
        else:
            raise Exception(f"API request failed with status code {response.status_code}")

    def add_histogram(self, column):
        if column in self.data.columns:
            plt.hist(self.data[column].dropna())
            plt.title(f'Histogram of {column}')
            plt.show()
        else:
            print(f'Column {column} does not exist.')

    def add_line_plot(self, x_column, y_column):
        if x_column in self.data.columns and y_column in self.data.columns:
            plt.plot(self.data[x_column], self.data[y_column])
            plt.title(f'Line Plot of {y_column} vs {x_column}')
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.show()
        else:
            print(f'One or both columns do not exist.')

    def add_scatter_plot(self, x_column, y_column):
        if x_column in self.data.columns and y_column in self.data.columns:
            plt.scatter(self.data[x_column], self.data[y_column])
            plt.title(f'Scatter Plot of {y_column} vs {x_column}')
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.show()
        else:
            print(f'One or both columns do not exist.')

    def count_missing_values(self):
        return self.data.isnull().sum()

    def report_missing_values(self):
        report = self.data.isnull().sum()
        print("Missing Values Report:")
        print(report[report > 0])

    def fill_missing_values(self, column, method='mean'):
        if column in self.datacolumns:
            if method == 'mean':
                self.data[column].fillna(self.data[column].mean(), inplace=True)
            elif method == 'median':
                self.data[column].fillna(self.data[column].median(), inplace=True)
            elif method == 'mode':
                self.data[column].fillna(self.data[column].mode()[0], inplace=True)
            else:
                print("Method not recognized. Use 'mean', 'median', or 'mode'.")
        else:
            print(f'Column {column} does not exist.')

data_loader = DataLoader()
data_loader.load_csv('"C:\Users\user\PycharmProjects\pythonProject2\.venv\Dev_data_to_be_shared.csv"')