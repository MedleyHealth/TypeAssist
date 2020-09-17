from type_assist.config import config

import re


class DatasetGenerator:
    """

    :param df: A DataFrame containing type_assist free text column
    :param text_col: A string for the column name containing free text
    """

    def __init__(self, df, text_col):

        self.df = df
        self.text_col = text_col

        self._generate()

    def __len__(self):
        """

        :return:
        """

        return len(self.df)

    def __truediv__(self, num_pieces):
        """
        Splits the DatasetGenerator into (roughly) equally-sized pieces

        :param number_shares:
        :return: An unpacked list of equally-sized dataset chunks
        """

        num_samples = len(self.df)

        datasets = []

        for n in range(num_pieces):
            start_idx = int(n / num_pieces * num_samples) #TODO check logic of int
            end_idx = int((n + 1) / num_pieces * num_samples)

            df = self.df[start_idx: end_idx]
            ds = DatasetGenerator(df, self.text_col)

            datasets.append(ds)

        return datasets

    def _generate(self, filter_length=config['filter_length'],
                  max_length=config['max_length'],
                  filter_regex=config['filter_regex'],
                  regex_pattern=config['regex_pattern'],
                  split_newlines=config['split_newlines'],
                  convert_lowercase=config['convert_lowercase']):

        self.filter_length = filter_length
        self.filter_regex = filter_regex
        self.split_newlines = split_newlines
        self.convert_lowercase = convert_lowercase

        self.corpus = [text for text in self.df[self.text_col]]

        if filter_length:
            self.max_length = max_length
            self.corpus = self._filter_length(self.corpus)

        if filter_regex and regex_pattern:
            self.regex_pattern = regex_pattern
            self.corpus = self._filter_regex(self.corpus)

        if split_newlines:
            self.corpus = self._split_newlines(self.corpus)

        if convert_lowercase:
            self.corpus = self._convent_lowercase(self.corpus)

        self.data = self._generate_ngrams(self.corpus)

    def _filter_length(self, corpus, max_length=config['max_length']):
        """
        Drops any samples with text length greater than the max length

        :param corpus: A list of free text strings
        :param max_length: An integer for the maximum length free text
        :return: The updated corpus
        """

        corpus = [text for text in corpus if len(text) < max_length]

        return corpus

    def _filter_regex(self, corpus, regex_pattern=config['regex_pattern']):
        """
        Drops any samples that contain any substring which matches type_assist regex

        :param corpus: A list of free text strings
        :param regex: A string for type_assist regex pattern expression
        :return: The updated corpus
        """

        corpus = [text for text in corpus if re.search(regex_pattern, text) is None]

        return corpus

    def _split_newlines(self, corpus, min_length=config['min_length']):
        """
        Splits the corpus on newline characters \n

        :param corpus: A list of free text strings
        :param min_length: An integer for the minimum length of split notes
        :return: The updated corpus
        """

        corpus = [text.split('\n') for text in corpus]

        corpus = [split_text for text in corpus for split_text in text
                  if len(split_text) > min_length]

        return corpus

    def _convent_lowercase(self, corpus):
        """
        Converts the corpus to lower case letters.

        :param corpus: A list of free text strings
        :return: The updated corpus
        """

        corpus = [text.lower() for text in corpus]

        return corpus

    def _clean_special_chars(self, corpus, allowed_chars=config['allowed_chars']):
        """
        Removes all special characters from the corpus
    
        :param corpus: A list of free text strings
        :param special_chars: A string of special characters to remove
        :return: The updated corpus
        """

        text_chars = [set(text) for text in corpus]
        unique_chars = set([char_set for text in text_chars for char_set in text])

        self.special_chars = [char for char in unique_chars if char not in allowed_chars]

        corpus = [text.replace(sc, '') for text in corpus for sc in self.special_chars]

        return corpus

    def _generate_ngrams(self, corpus, start=config['ngram_start'],
                         end=config['ngram_end']):
        """

        :param corpus:
        :param start:
        :param end:
        :return:
        """

        data = []

        for text in corpus:
            for i in range(1, len(text)):
                x_ngram = start + text[:i+1] + end
                y_ngram = start + text[i+1:] + end
                data.append([x_ngram, y_ngram])

        return data


class LanguageIndex:
    """


    """

    def __init__(self, lang):

        self.lang = lang
        self.word2idx = {}
        self.idx2word = {}
        self.vocab = set()

        self.create_index()

        self.max_length = self._max_length(self.data)

    def _create_index(self):
        """

        :return:
        """

        for phrase in self.lang:
            self.vocab.update(phrase.split(' '))
        self.vocab = sorted(self.vocab)
        self.word2idx["<pad>"] = 0
        self.idx2word[0] = "<pad>"
        for i,word in enumerate(self.vocab):
            self.word2idx[word] = i + 1
            self.idx2word[i+1] = word

    def _max_length(data):
        return max(len(sequence) for sequence in data)


def generate_train():
    pass