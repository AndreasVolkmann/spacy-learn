import numpy


class Similarity:
    def __init__(self, nlp, labels, boost=5, threshold=0.7):
        self.labelDoc = nlp(labels)
        self.boost = boost
        self.threshold = threshold
        self.nlp = nlp

    def map_tokens(self, token):
        return [token.similarity(label) for label in self.labelDoc]

    def calculate(self, text):
        doc = self.nlp(text)
        res = [self.map_tokens(token) for token in doc]
        label_size = len(self.labelDoc)
        likeness = numpy.zeros(label_size)

        for ti in range(0, len(res)):
            for li in range(0, label_size):
                score = res[ti][li]
                if score == 1:
                    score += self.boost
                if score > self.threshold:
                    likeness[li] += score

        winner_index = numpy.argmax(likeness)
        return self.labelDoc[winner_index].text

    def detect_entities(self, text):
        doc = self.nlp(text)
        print(doc.ents[0], doc.ents[0].label_)
        # print(doc.ents[0])
