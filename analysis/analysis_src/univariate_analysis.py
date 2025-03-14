from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Abstract class for univariate analysis Statergy
class UnivariateAnalysisStratergy(ABC):
    @abstractmethod
    def analyze(self, data: pd.DataFrame, column: str):
        """ 
        Abstract method to analyze the data
        
        Parameters:
        data: pd.DataFrame
            The data to be analyzed
        column: str
            The column to be analyzed
                       
        Returns:None
        """
        pass

# Class to perform univariate analysis on numerical data
class NumericalUnivariateAnalysis(UnivariateAnalysisStratergy):
    def analyze(self, data: pd.DataFrame, column: str):
        """
        Method to perform univariate analysis on numerical data
        
        Parameters:
        data: pd.DataFrame
            The data to be analyzed
        column: str
            The column to be analyzed
                       
        Returns:None
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(data[column], kde=True, bins=30)
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.show()

# Class to perform univariate analysis on categorical data
class CategoricalUnivariateAnalysis(UnivariateAnalysisStratergy):
    def analyze(self, data: pd.DataFrame, column: str):
        """
        Method to perform univariate analysis on categorical data
        
        Parameters:
        data: pd.DataFrame
            The data to be analyzed
        column: str
            The column to be analyzed
                       
        Returns:None
        """
        plt.figure(figsize=(10, 6))
        sns.countplot(x=column, data=data, palette="muted")
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.show()

# Context class for univariate analysis
class UnivariateAnalysis:
    def __init__(self,  analysis_type: UnivariateAnalysisStratergy):
        """
        Method to perform univariate analysis on categorical data
        
        Parameters:
        data: pd.DataFrame
            The data to be analyzed
        column: str
            The column to be analyzed
        analysis_type: str
            The type of analysis to be performed
                       
        Returns:None
        """
        
        self.analysis_type = analysis_type

    def set_strategy(self, analysis_type: UnivariateAnalysisStratergy):
        """
        Method to set the analysis type
        
        Parameters:
        analysis_type: str
            The type of analysis to be performed
                       
        Returns:None
        """
        self.analysis_type = analysis_type

    def execute(self, data: pd.DataFrame, column: str):
        """
        Method to execute the analysis
        
        Parameters:
        data: pd.DataFrame
            The data to be analyzed
        column: str
            The column to be analyzed
                       
        Returns:None
        """
        self.analysis_type.analyze(data, column)


# Example
if __name__ == "__main__":
    pass

   
