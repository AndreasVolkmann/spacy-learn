import spacy


def initialize_model(model_name='en', disable=None, blank=False):
    """
    Pass an empty array as disable to not disable anything
    """
    if disable is None:
        disable = ["parser", "ner", "tagger"]

    print("Loading model...")
    if blank:
        nlp = spacy.blank(model_name, disable=disable)
    else:
        nlp = spacy.load(model_name, disable=disable)
    print("Model loaded!", nlp.pipe_names)
    return nlp


def initialize_textcat(nlp):
    # add the text classifier to the pipeline if it doesn't exist
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'textcat' not in nlp.pipe_names:
        textcat = nlp.create_pipe('textcat')
        nlp.add_pipe(textcat, last=True)
    # otherwise, get it, so we can add labels to it
    else:
        textcat = nlp.get_pipe('textcat')

    return textcat
