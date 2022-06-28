import pickle
import logging
import os
from dotenv import load_dotenv
#import sklearn
import numpy as np

def load_env_vars():
    #load the environment variables (in prod) and load the variables from .env file(in development)
    load_dotenv()
    global BEST_MODEL_FOR_TEMPERATURE_PREDICTION
    BEST_MODEL_FOR_TEMPERATURE_PREDICTION=os.getenv('BEST_MODEL_FOR_TEMPERATURE_PREDICTION')
    global BEST_MODEL_FOR_CLASS_PREDICTION
    BEST_MODEL_FOR_CLASS_PREDICTION=os.getenv('BEST_MODEL_FOR_CLASS_PREDICTION')


def predictClasses(payload):
    """makes the prediction of classes based on the model_selected in load_model()

    Args:
        payload (list): list of independent features to be used for making predictions
    Output:
        result(int): prediction output sent to the calling function
    """
    # Model to be loaded is stored in BEST_MODEL_FOR_CLASS_PREDICTION env variable. Load the env variable
    load_env_vars()
    logging.info(f'Class prediction: Env variables loaded. Model: {BEST_MODEL_FOR_CLASS_PREDICTION} will be used.')

    # Predict Class
    #load the model
    model=pickle.load(open(f'./SavedModels/{str(BEST_MODEL_FOR_CLASS_PREDICTION)[:-2]}_model.pkl','rb'))
    logging.info('Class prediction: Model loaded for making prediciton')
    
    #make prediction
    try:
        result = model.predict([payload])
    except Exception as e:
        logging.exception("Exception occured while making predictions: predictClasses(payload): "+str(e))

    return result

def predictTemp(payload):
    """makes the prediction based on the model selected in load_model()

    Args:
        payload (list): list of indipendent features to be used for making the predictions
    Output:
        result (float): prediction output sent to the calling function
    """
    # Model to be loaded is stored in BEST_MODEL_FOR_TEMPERATURE_PREDICTION env variable. Load the env valrible
    load_env_vars()
    logging.info(f'Temp prediciton: Env variables loaded. Model : {BEST_MODEL_FOR_TEMPERATURE_PREDICTION} will be used')

    # Predict temperature
    #load the model
    model=pickle.load(open(f'./SavedModels/{str(BEST_MODEL_FOR_TEMPERATURE_PREDICTION)[:-2]}_model.pkl','rb'))
    logging.info('Temperature prediction: Model loaded for making prediciton')

    #make prediction
    try:
        result = model.predict([payload])
    except Exception as e:
        logging.exception("Exception occured while making predictions: predictTemp(payload): "+str(e))

    return result
