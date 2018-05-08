import nlp_model as nm
import data_reader

nlp = nm.initialize_model('en', blank=True)
nm.initialize_textcat(nlp)

data_reader.read()
optimizer = nlp.begin_training()
print("Training model...")
