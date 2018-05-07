from collections import defaultdict

from data_reader import read
from similarity import Similarity
from similarity_trainer import SimilarityTrainer

# path = 'data.psv'
path = 'D:\Dev\Java\clinical-trials\\trials_combined_text.psv'
maxRecords = 100

correctLabels, textRows = read(path, '|')

labels = sorted(set(correctLabels))
labelString = ' '.join(labels)

sim = Similarity(labelString, boost=5, threshold=0.7, model_name='en_core_web_lg')
size = min(len(correctLabels), maxRecords)
trainer = SimilarityTrainer(correctLabels, textRows, sim, size)
misinterpretations, correctGuesses = trainer.train()

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
