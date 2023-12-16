import numpy as np
import pandas as pd

class OneHotEncoder:
    def fit_transform(self, df, columns):
        self.df = df
        
        for column in columns:
            column_categories = self.df[column].astype('category').cat.categories

            for cat in column_categories:
                self.df[cat] = (self.df[column] == cat).astype(int)

        return self.df
    

if __name__ == '__main__':
    df = pd.read_excel('sample.xlsx')

    encoder = OneHotEncoder()

    df = encoder.fit_transform(df, ['col 2', 'col3'])
    print(df)