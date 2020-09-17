from type_assist.config import config

from abc import ABC, abstractmethod

import logging
import re
import os


class MetaModelPT(ABC):

    def fit_model(self, data, n_samples=-1, tr_batch_size=config['tr_batch_size'],
                  epochs=config['epochs'], val_split=config['val_split']):
        """

        :return:
        """

        input_data = data.input_data[:n_samples]
        output_data = data.output_data[:n_samples]
        target_data = data.target_data[:n_samples]

        return

    def save_model(self, models_dir=config['models_dir']):
        """

        :return:
        """

        model_path = f'{models_dir}/model_{self.model_num}'
        json_path = f'{model_path}.json'
        weights_path = f'{model_path}.h5'

        logging.info(f'Saving JSON model to {json_path}...')
        logging.info(f'Saving HDF5 weights to {weights_path}...')

        if os.path.exists(json_path) or os.path.exists(weights_path):
            raise BaseException('WARNING. Save path exists. Aborting.')

        with open(json_path, 'w') as f:
            model_json = self.model.to_json()
            f.write(model_json)

        self.model.save_weights(weights_path)

    def load_model(self):
        """

        :return:
        """

        pass

    @property
    def model_num(self):
        """ Calculates the current model number by adding 1 to the last number"""
        models_dir = config['models_dir']
        files = os.listdir(models_dir)
        matches = re.search('\d*s.json', files)
        # matches = order(matches)

        return matches[-1] + 1

    @abstractmethod
    def build_model(self):
        pass



class EncoderDecoderPT(MetaModelPT):


    def __init__(self):
        super().__init__()

        self.model = self.build_model()

    def __call__(self, *args, **kwargs):
        pass

    def _build_encoder(self):
        pass

    def _build_decoder(self):
        pass

    def build_model(self):
        pass
