class Misinterpretation:

    def __init__(self, index, prediction, actual):
        self.index = index
        self.prediction = prediction
        self.actual = actual

    def __str__(self):
        return str(self.index) + ' ' + self.prediction + ' ' + self.actual

    def get_key(self):
        return self.prediction + '|' + self.actual
