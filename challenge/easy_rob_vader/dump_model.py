from joblib import dump
from test_user import Model

m = Model
dump(m, 'model.joblib')
