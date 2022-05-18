import tensorflow as tf
import numpy as np
import json
import os

DATA_PATH = os.path.join('MP_Data')

actions = np.array(['hello', 'thanks', 'iloveyou']) #np.array(json.load("labels/actions.json", "r"))

no_sequences = 30

sequence_length = 30

