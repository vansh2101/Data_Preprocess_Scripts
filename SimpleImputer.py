import numpy as np
import pandas as pd

class SimpleImputer:
    def __init__(self, strategy='mean', missing_values=np.nan):
        strategy_list = ['mean', 'median', 'mode', 'constant']

        if strategy not in strategy_list:
            raise Exception('Invalid strategy')
        
        self.strategy = strategy
        self.missing_values = missing_values

    def impute(self, df, columns):
        self.df = df

        for col in columns:
            if self.strategy == 'mean':
                self.df[col] = self.df[col].fillna(self.df[col].mean())

            elif self.strategy == 'median':
                self.df[col] = self.df[col].fillna(self.df[col].median())

            elif self.strategy == 'mode':
                self.df[col] = self.df[col].fillna(self.df[col].mode()[0])

            elif self.strategy == 'constant':
                self.df[col] = self.df[col].fillna(self.missing_values)

        return self.df


if __name__ == '__main__':
    df = pd.read_excel('sample2.xlsx')

    imputer = SimpleImputer(strategy='constant', missing_values=0)

    df = imputer.impute(df, ['col 1'])
    print(df)