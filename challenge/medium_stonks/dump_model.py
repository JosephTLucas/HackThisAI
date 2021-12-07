from joblib import dump
from example_model import Model

m = Model
dump(m, 'model.joblib')
