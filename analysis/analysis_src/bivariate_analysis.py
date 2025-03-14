from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# Abstract class for bivariate analysis Statergy
class BivariateAnalysisStratergy(ABC):
    @abstractmethod
    def analyze(self, data: pd.DataFrame, column1: str, column2: str):
        """ 
        Abstract method to analyze the data
        
        Parameters:
        data: pd.DataFrame
            The data to be analyzed
        column1: str
            The first column to be analyzed
        column2: str
            The second column to be analyzed
                       
        Returns:None
        """
        pass

# Concreate Strategy for NUmerical vs Numerical Bivariate Analysis
class NumericalNumericalBivariateAnalysis(BivariateAnalysisStratergy):
    def analyze(self, data: pd.DataFrame, column1: str, column2: str):
        """
        Method to perform bivariate analysis on numerical data
        
        Parameters:
        data: pd.DataFrame
            The data to be analyzed
        column1: str
            The first column to be analyzed
        column2: str
            The second column to be analyzed
                       
        Returns:None
        """
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=column1, y=column2, data=data)
        plt.title(f"{column1} vs {column2}")
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.show()


# Concreate Strategy for Categorical vs Numerical Bivariate Analysis
class CategoricalNumericalBivariateAnalysis(BivariateAnalysisStratergy):
    def analyze(self, data: pd.DataFrame, column1: str, column2: str):
        """
        Method to perform bivariate analysis on categorical and numerical data
        
        Parameters:
        data: pd.DataFrame
            The data to be analyzed
        column1: str
            The first column to be analyzed
        column2: str
            The second column to be analyzed
                       
        Returns:None
        """
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=column1, y=column2, data=data)
        plt.title(f"{column1} vs {column2}")
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.xticks(rotation=45)
        plt.show()

# Concreate Strategy for Categorical vs Categorical Bivariate Analysis  
class CategoricalCategoricalBivariateAnalysis(BivariateAnalysisStratergy):
    def analyze(self, data: pd.DataFrame, column1: str, column2: str):
        """
        Method to perform bivariate analysis on categorical data
        
        Parameters:
        data: pd.DataFrame
            The data to be analyzed
        column1: str
            The first column to be analyzed
        column2: str
            The second column to be analyzed
                       
        Returns:None
        """
        plt.figure(figsize=(10, 6))
        sns.countplot(x=column1, hue=column2, data=data)
        plt.title(f"{column1} vs {column2}")
        plt.xlabel(column1)
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.show()

# Context class for bivariate analysis
class BivariateAnalysis:
    def __init__(self,  analysis_type: BivariateAnalysisStratergy):
        """
        Method to perform bivariate analysis on categorical data
        
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

    def set_strategy(self, analysis_type: BivariateAnalysisStratergy):
        """
        Method to set the analysis type
        
        Parameters:
        analysis_type: str
            The type of analysis to be performed
                       
        Returns:None
        """
        self.analysis_type = analysis_type

    def execute(self, data: pd.DataFrame, column1: str, column2: str):
        """
        Method to execute the analysis
        
        Parameters:
        data: pd.DataFrame
            The data to be analyzed
        column: str
            The column to be analyzed
        """
        self.analysis_type.analyze(data, column1, column2)

# Example Usage
if __name__ == "__main__":
    pass