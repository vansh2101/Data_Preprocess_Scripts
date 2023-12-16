import numpy as np
import pandas as pd

class OrdinalEncoder:
    def __init__(self):
        self.cats = {}

    def fit_transform(self, df, columns):
        self.df = df
        
        for column in columns:
            column_categories = self.df[column].astype('category')
            self.cats[column] = dict(enumerate(column_categories.cat.categories))

            self.df[column] = column_categories.cat.codes

        return self.df
    
    def transform(self, df, columns):
        self.some_other_df = df

        for column in columns:
            self.some_other_df[column] = self.some_other_df[column].map({v: k for k, v in self.cats[column].items()})

        return self.some_other_df

    def inverse_transform(self, df, columns):
        df_copy = df.copy()
        for column in columns:
            df_copy[column] = df_copy[column].map(self.cats[column])

        return df_copy
    

if __name__ == '__main__':
    df = pd.read_excel('sample.xlsx')

    encoder = OrdinalEncoder()

    df = encoder.fit_transform(df, ['col 2', 'col3'])
    df = encoder.inverse_transform(df, ['col 2', 'col3'])