from dill import dump


class Model:
    def __init__(self):
        pass

    def get_score(self, user_input):
        return 0

with open("model.dill", "wb") as f:
    dump(Model(), f)
