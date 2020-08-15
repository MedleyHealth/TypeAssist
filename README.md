[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MedleyHealth/TypeAssist)

# Type Assist
Type Assist is an application that offers text suggestions as users type. The user hits the tab key to accept the suggestion. The two major objectives of this library are to fine tune language models and to serve those models via many mediums such as a broswer. It can be optionally extended to use federated learning during the model training process. Doing so maintains the privacy of users while creating a better collective model.

![Demo](https://medralabs.com/wp-content/uploads/2020/07/Demo-v2.gif)

## Getting Started

1. [Apply for access](https://mimic.physionet.org/gettingstarted/access/) to the MIMIC dataset.
2. Download the dataset once access is approved.
3. Save the dataset to Google Drive.
4. Start with the EDA notebook to see what the data is like.

## Google Colab

Google Colab offers free GPU use with notebooks. It integrates nicely with Google Drive too. 

See all the notebooks for the Medley Health organization [here](https://colab.research.google.com/github/MedleyHealth/TypeAssist/).

It's important to make sure no output from the code cells in the notebook is saved to Github or any other public location. To make sure Colab doesn't save this output:

1. Go to Edit > Notebook Settings
2. Make sure the checkbox is ticked for "Omit code cell output when saving this notebook"
