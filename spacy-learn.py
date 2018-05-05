import csv

from similarity import Similarity

correctLabels = []
textRows = []

with open('data.psv') as csvfile:
    reader = csv.reader(csvfile, delimiter='|')
    for row in reader:
        correctLabels.append(row[0])
        textRows.append(row[1])

labels = "Cancer HIV Obesity Depression Pharmacokinetics"

sim = Similarity(labels)

size = len(correctLabels)
correctGuesses = 0

for i in range(0, size):
    correctLabel = correctLabels[i]
    text = textRows[i]
    winner = sim.calculate(text)
    print(winner, correctLabel)
    if winner == correctLabel:
        correctGuesses += 1


print("Correct Guesses", correctGuesses, correctGuesses / size * 100)
