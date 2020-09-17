from

class ModelSelector:
    """
    Automatically loads the model based on the config
    """

    valid_names = {
        'encoderdecoderpt': EncoderDecoderPT,
        'encdoerdecodertf': EncoderDecoderTF,
    }

    def __init__(self, model_name=config['model_name'],
                 framework=config['framework']):

        self.model_name = ValidateName
        self.framework = framework

    def __call__(self, *args, **kwargs):
        return _model

    def select_model(self):

        model = (self.valid_names[self.model_name])()

    @property
    def model(self):
        return self._model