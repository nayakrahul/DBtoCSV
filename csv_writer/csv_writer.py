import pandas as pd


class CSV:
    def __init__(self, file):
        self.file = file

    def write(self, rows, columns):
        df = pd.DataFrame(rows, columns=columns)
        df.to_csv(self.file, sep=',', index=False)
