import pandas as pd

class fileCleaner():
    '''This class cleans up the inputs provided'''

    def __init__(self, df):
        self.df = df

    def prntdf(self):
        print('*'*30)
        print(self.df)

    def roundoff(self):
        print('*' * 30)
        print('round off all numbers ')
        print(round(self.df))

    def removeNANs(self):
        print('*' * 30)
        print('drop all nans')
        print(self.df.dropna())
print(fileCleaner.__doc__)
df = pd.read_excel('sampleFile.xlsx')
fc = fileCleaner(df)
fc.prntdf()
fc.roundoff()
fc.removeNANs()
