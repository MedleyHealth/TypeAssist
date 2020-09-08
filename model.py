from config import config

import tensorflow as tf

import os

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, Dense, CuDNNLSTM, Embedding, Flatten, TimeDistributed, Dropout, LSTMCell, RNN, Bidirectional, Concatenate, Layer
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.python.keras.utils import tf_utils
from tensorflow.keras import backend as K
from tensorflow.keras.models import model_from_json
from tensorflow.keras.models import load_model


class EncoderDecoderTF:
    """

    :param data: A LanguageIndex object
    :return:

    """

    def __init__(self, data, load_path=config['load_path']):

        self.embedding_dim = config['embedding_dim']
        self.use_birectional = config['use_bidirectional']
        self.loss = config['loss']
        self.metrics = config['metrics']

        self.max_length = data.max_length
        self.vocab_size = data.vocab_size

        self.histories = []

        if load_path:
            pass

        else:
            self.encoder = self._build_encoder()
            self.decoder = self._build_decoder()
            self.model = self._build_model()


    def _build_encoder(self):
        """

        :return:
        """

        self.encoder_inputs = Input(shape=(self.max_length,))

        encoder_emb = Embedding(input_dim=self.vocab_size,
                                output_dim=self.embedding_dim)

        if self.use_birectional:

            encoder_lstm = Bidirectional(CuDNNLSTM(units=self.units,
                                                   return_sequences=True,
                                                   return_state=True))

            encoder_out, fstate_h, fstate_c, bstate_h, bstate_c = encoder_lstm(encoder_emb(self.encoder_inputs))
            state_h = Concatenate()([fstate_h, bstate_h])
            state_c = Concatenate()([bstate_h, bstate_c])

        else:
            encoder_lstm = CuDNNLSTM(units=self.units,
                                     return_sequences=True,
                                     return_state=True)

            encoder_out, state_h, state_c = encoder_lstm(encoder_emb(self.encoder_inputs))

        self.encoder_states = [state_h, state_c]

        encoder_model = Model(self.encoder_inputs,
                              [encoder_out, state_h, state_c])

        return encoder_model

    def _build_decoder(self, encoder_states):
        """

        :return:
        """

        self.decoder_inputs = Input(shape=(None,))

        decoder_emb = Embedding(input_dim=self.vocab_size,
                                output_dim=self.embedding_dim)

        decoder_lstm = CuDNNLSTM(units=self.units * 2,
                                 return_sequences=True,
                                 return_state=True)

        decoder_lstm_out, _, _ = decoder_lstm(decoder_emb(self.decoder_inputs),
                                              initial_state=encoder_states)

        decoder_d1 = Dense(self.units, activation='relu')
        decoder_d2 = Dense(self.vocab_size, activation='softmax')

        self.decoder_out = decoder_d2(Dropout(rate=.2)(decoder_d1(Dropout(rate=.2)(decoder_lstm_out))))

        decoder_model =

    def _build_model(self):
        """

        :return:
        """

        model = Model(inputs=[self.encoder_inputs, self.decoder_inputs],
                      outputs=self.decoder_out)

        opt = tf.train.AdamOptimizer()

        model.compile(optimizer=opt, loss=self.loss, metrics=self.metrics)

        return model

    def fit_model(self, data, n_samples=-1, tr_batch_size=config['tr_batch_size'],
                  epochs=config['epochs'], val_split=config['val_split']):
        """

        :return:
        """

        input_data = data.input_data[:n_samples]
        output_data = data.output_data[:n_samples]
        target_data = data.target_data[:n_samples]

        history = self.model.fit([input_data, output_data], target_data,
                            batch_size=tr_batch_size,
                            epochs=epochs,
                            validation_split=val_split)

        self.histories.append(history)

        return history

    def save_model(self, model_dir=config['model_dir']):
        """

        :return:
        """

        save_path = '/content/drive/My Drive/3 Reference/TypeAssist/model_1'

        if os.path.exists('{}.json'.format(save_path)):
            raise BaseException('WARNING. Save path exists. Please increment the model number.')

        model_json = self.model.to_json()

        with open('{}.json'.format(save_path), 'w') as f:
            f.write(model_json)

        # serialize weights to HDF5
        inf_model.save_weights('{}.h5'.format(save_path))




