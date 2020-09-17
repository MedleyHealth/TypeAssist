from type_assist.config import Configure
from type_assist.data_prep import Formatter, Preprocess




import torch
import logging


class PythonPredictor:

    configure = Configure()
    formatter = Formatter()
    preprocess = Preprocess()

    def __init__(self):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        logging.info(f'Using device: {self.device}...')

        self.model_path = None
        self.model = self.load_model(self.model_path)
        self.model = self.model.to(self.device)

    def predict(self, payload):
        """
        Makes predictions

        :param payload: A dictionary of request parameters
        :return prediction: A string
        :return confidence: A float from 0 to 1 with highest confidence at 1
        """

        text = payload['text']
        data = self.formatter(text)
        data = self.preprocessor(data)
        prediction, confidence = self.model.inference(data)

        return prediction, confidence

    def load_model(self, model_path):
        model = ...
        return model