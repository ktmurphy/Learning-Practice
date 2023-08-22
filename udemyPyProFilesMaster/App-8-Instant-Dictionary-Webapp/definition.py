
import pandas

class Definition:

    def __init__(self, term):
        self.term = term

    def get(self):
        df = pandas.read_csv('data.csv')
        # the df returns a word dataframe, which we get the term out of, and then convert to tuple
        return tuple(df.loc[df['word'] == self.term]['definition'])
