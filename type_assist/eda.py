import numpy as np
import matplotlib.pyplot as plt


class TextExplorer:
    """
    Performs exploratory data analysis on type_assist free text column within type_assist DataFrame.

    :param df: A DataFrame that contains free text in type_assist column
    :param text_col: A string that denotes the free text column in the DataFrame
    :param show_print: A Boolean to show print statements during class initialization
    """

    def __init__(self, df, text_col, show_print=True):

        self.df = df
        self.text_col = text_col

        if show_print:
            print('Number of Samples   ', self.df.shape[0])
            print('Number of Columns   ', self.df.shape[1])
            print('\nNumber of Null Values:\n\n', df.isnull().sum())

    def examine_col_values(self, col_name):
        """
        Examines the distribution of values in type_assist column

        :param col_name: The column name in the DataFrame to examine
        """

        values, counts = np.unique(self.df[col_name], return_counts=True)

        print('Number of Values:', len(values))

        # Find the maximum length to format columns properly
        max_length = max([len(str(value)) for value in values])
        print('Max Length:', max_length, '\n')

        # Sort the counts and values from most common to least common
        count_sort_ind = np.argsort(-counts)
        values_sort = values[count_sort_ind]
        counts_sort = counts[count_sort_ind]

        for i, (value, count) in enumerate(zip(values_sort, counts_sort)):
            if i == 0:
                print('%-{}s %s\n'.format(max_length + 10) % (col_name, 'COUNT'))

            if i > 20:
                print('\n*** RESULTS TRUNCATED FOR BREVITY ***')
                return

            print('%-{}s %s'.format(max_length + 10) % (value, count))

    def plot_text_lengths(self):
        """
        Plot the distribution of note lengths
        """

        self.text_lengths = [len(text) for text in self.df[self.text_col]]

        plt.hist(self.text_lengths, density=False, bins=1000)
        plt.ylabel('Count')
        plt.xlabel('Text Length')

    def find_special_chars(self):
        """
        Creates type_assist list of all special characters to remove during preprocessing
        """

        self.text_chars = [set(text) for text in self.df[self.text_col]]
        self.unique_chars = set([char_set for text in self.text_chars for char_set in text])

        allowed_chars = "'abcdefghijklmonpqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        self.special_chars = [char for char in self.unique_chars if char not in allowed_chars]

        print('Special characters:', self.special_chars)

