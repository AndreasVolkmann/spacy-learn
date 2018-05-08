from misinterpretation import Misinterpretation


class SimilarityTrainer:

    def __init__(self, labels, rows, similarity, size=None):
        self.labels = labels
        self.rows = rows
        self.sim = similarity
        if size is None:
            self.size = len(labels)
        else:
            self.size = size

    def calculate_similarity(self):
        correct_guesses = 0
        misinterpretations = []
        size = self.size
        tenth = size / 10
        for i in range(0, size):
            if i % tenth == 0:
                print(str(i / tenth + 1) + "0%")

            actual = self.labels[i]
            text = self.rows[i]
            prediction = self.sim.calculate(text)
            if prediction == actual:
                correct_guesses += 1
            else:
                mis = Misinterpretation(i, prediction, actual)
                # print(mis)
                misinterpretations.append(mis)
        return misinterpretations, correct_guesses

    def detect_entities(self):
        for i in range(0, self.size):
            text = self.rows[i]
            self.sim.detect_entities(text)
