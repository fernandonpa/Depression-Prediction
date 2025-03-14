from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# Abstract class for multivariate analysis 
class MultivariateAnalysisTemplate(ABC):
    def analyze(self, data: pd.DataFrame):
        """ 
        Abstract method to analyze the data
        
        Parameters:
        data: pd.DataFrame
            The data to be analyzed
        columns: list
            The columns to be analyzed
                       
        Returns:None
        """
        self.generate_correlation_heatmap(data)
        self.generate_pairplot(data)

    @abstractmethod
    def generate_correlation_heatmap(self, data: pd.DataFrame):
        """ 
        Abstract method to generate correlation heatmap
        
        Parameters:
        data: pd.DataFrame
            The data to be analyzed
                       
        Returns:None
        """
        pass

    @abstractmethod
    def generate_pairplot(self, data: pd.DataFrame):
        """ 
        Abstract method to generate pairplot
        
        Parameters:
        data: pd.DataFrame
            The data to be analyzed
                       
        Returns:None
        """	
        pass

# Class to perform multivariate analysis
class SimpleMultivariateAnalysis(MultivariateAnalysisTemplate):
    def generate_correlation_heatmap(self, data: pd.DataFrame):
        """
        Method to generate correlation heatmap
        
        Parameters:
        data: pd.DataFrame
            The data to be analyzed
                       
        Returns:None
        """
        plt.figure(figsize=(12, 10))
        sns.heatmap(data.corr(), annot=True,fmt=".2f", cmap='coolwarm', linewidths=0.5)
        plt.title("Correlation Heatmap")
        plt.show()

    def generate_pairplot(self, data: pd.DataFrame):
        """
        Method to generate pairplot
        
        Parameters:
        data: pd.DataFrame
            The data to be analyzed
                       
        Returns:None
        """
        sns.pairplot(data)
        plt.suptitle("Pair Plot of Selected Features", y=1.02)
        plt.show()

if __name__ == "__main__":
    pass


