import pandas as pd

class DataAnalyzer:
    def __init__(self, data,save):
        self.data = data
        self.save = save
    
    def analyze(self):
        #Alapvető statisztikai elemzést végez és kerekíti az eredményeket
        analysis = self.data.describe().round(2)  # Kerekítés két tizedesjegyre
        if not self.save:
            print("\nStatisztikai elemzés:")
            print(analysis)
        analysis = analysis.reset_index().rename(columns={'index':'Elemzés'})
        return analysis
    
    
    #The describe() method returns description of the data in the DataFrame.
    
    #If the DataFrame contains numerical data, the description contains these information for each column:
    
    #count - The number of not-empty values.
    #mean - The average (mean) value.
    #std - The standard deviation.
    #min - the minimum value.
    #25% - The 25% percentile*.
    #50% - The 50% percentile*.
    #75% - The 75% percentile*.
    #max - the maximum value.
    
    #*Percentile meaning: how many of the values are less than the given percentile.