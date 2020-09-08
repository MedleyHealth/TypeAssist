from config import config

import re


class DataGenerator:
    """

    :param df: A DataFrame containing a free text column
    :param text_col: A string for the column name containing free text
    """

    def __init__(self, df, text_col):

        self.df = df
        self.text_col = text_col

        self.corpus = [text for text in df[text_col]]

        if config['filter_length']:
            self.length_limit = config['length_limit']
            self.corpus = self._filter_length(self.corpus)

        if config['filter_regex']:
            self.regex = config['regex']
            self.corpus = self._filter_regex(self.corpus)

        if config['split_newlines']:
            self.split_new_lines = config['split_newlines']
            self.corpus = self._split_new_lines(self.corpus)

        if config['convert_lowercase']:
            self.convent_lowercase = config['convert_lowercase']
            self.corpus = self._convent_lowercase(self.corpus)

        self.data = self.generate_ngrams(self.corpus)

    def _filter_length(self, corpus, max_length=config['max_length']):
        """
        Drops any samples with text length greater than the max length

        :param corpus: A list of free text strings
        :param max_length: An integer for the maximum length free text
        :return: The updated corpus
        """

        corpus = [text for text in corpus if len(text) < max_length]

        return corpus

    def _filter_regex(self, corpus, regex=config['regex']):
        """
        Drops any samples that contain any substring which matches a regex

        :param corpus: A list of free text strings
        :param regex: A string for a regex expression
        :return: The updated corpus
        """

        corpus = [text for text in corpus if re.search(regex, text) is None]

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

    def _clean_special_chars(self, corpus, special_chars=config['special_chars']):
        """
        Removes all special characters from the corpus
    
        :param corpus: A list of free text strings
        :param special_chars: A string of special characters to remove
        :return: The updated corpus
        """

        corpus = [text.replace(sc, '') for text in corpus for sc in special_chars]

        return corpus

    def _generate_ngrams(self, corpus, start=config['start'], end=config['end']):
        """

        :param corpus:
        :return:
        """

        data = []

        for text in corpus:
            for i in range(1, len(text)):
                x_ngram = start + text[:i + 1] + end
                y_ngram = start + text[i + 1:] + end
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