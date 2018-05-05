import numpy
import spacy

nlp = spacy.load('en')


class Similarity:

    def __init__(self, labels):

        self.labelDoc = nlp(labels)

    def map_tokens(self, token):
        return [token.similarity(label) for label in self.labelDoc]

    def calculate(self, text):
        doc = nlp(text)
        res = [self.map_tokens(token) for token in doc]
        label_size = len(self.labelDoc)
        likeness = numpy.zeros(label_size)

        for ti in range(0, len(res)):
            for li in range(0, label_size):
                score = res[ti][li]
                if score == 1:
                    score += 5
                likeness[li] += score

        winner_index = numpy.argmax(likeness)
        return self.labelDoc[winner_index].text
