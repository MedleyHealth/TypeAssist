# TypeAssist
Predictive text based on conditional fields

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MedleyHealth/TypeAssist)

# Type Assist
Type Assist is an industry-agnostic, embeddable element for text completion. That is it offers text suggestions as users type. The user hits the tab key to accept the suggestion. It requires use of a GPU for acceptable inference times. The two major objectives of this library are to fine tune pre-trained language models and to serve predictions from those models via a medium such as a broswer. 

We plan to extend the library to use federated learning during the model training process. Doing so will maintain the privacy of users while creating a better collective model.

![Demo](https://medralabs.com/wp-content/uploads/2020/07/Demo-v2.gif)

## Getting Started

1. Gather a dataset with free text
2. Preprocess the free text into the expected format
3. Fine tune a pre-trained language model
4. Host the fine tuned model in a RESTful API
5. Send requests to the API from a browser

## Google Colab

Google Colab offers free GPU use with notebooks, which is necessary to train models in a reasonable amount of time. It integrates nicely with Google Drive too if you want to store your dataset there. 

See all the notebooks for the Medley Labs organization [here](https://colab.research.google.com/github/MedleyLabs/TypeAssist/).
