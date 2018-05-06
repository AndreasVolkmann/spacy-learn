import csv

from misinterpretation import Misinterpretation
from similarity import Similarity
from collections import defaultdict

correctLabels = []
textRows = []

with open('data.psv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter='|')
    next(reader, None)
    for row in reader:
        correctLabels.append(row[0])
        textRows.append(row[1])

labels = sorted(set(correctLabels))
labelString = ' '.join(labels)

sim = Similarity(labelString, boost=5, threshold=0.7)
maxRecords = 100
size = min(len(correctLabels), maxRecords)
correctGuesses = 0
misinterpretations = []

for i in range(0, size):
    actual = correctLabels[i]
    text = textRows[i]
    prediction = sim.calculate(text)
    if prediction == actual:
        correctGuesses += 1
    else:
        mis = Misinterpretation(i, prediction, actual)
        # print(mis)
        misinterpretations.append(mis)

print("Correct Guesses", correctGuesses, correctGuesses / size * 100)

misDict = defaultdict(lambda: [])
for m in misinterpretations:
    key = m.get_key()
    misDict[key].append(m)

print("Misinterpretations (predicted vs actual):")
for key in misDict:
    name = key.split('|')
    items = misDict[key]
    print(name, len(items))

