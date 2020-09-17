from type_assist.config import config
from type_assist.data_validate import ValidateName
from type_assist.model_pt import EncoderDecoderPT
from type_assist.model_tf import EncoderDecoderTF

class ModelLoader:
    """
    Automatically loads the model based on the config

    >> ldr = ModelLoader()
    >> model = ldr()
    """

    valid_names = {
        'encoderdecoderpt': EncoderDecoderPT,
        'encdoerdecodertf': EncoderDecoderTF,
    }

    def __init__(self, model_name=config['model_name'],
                 framework=config['framework']):

        self.model_name = ValidateName()
        self.framework = framework

        self.model = self.load_model()

    def __call__(self, *args, **kwargs):
        return self._model

    def load_model(self, model_name):
        """ Initializes"""

        meta_model =

        return (self.valid_names[model_name])()

    @property
    def model(self):
        if self._model
        return self._model

    @model.setter
    def model(self):
