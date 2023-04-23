import spacy
import pytextrank

# example text
text = "Billy always listens to his mother. He always does what she says. If his mother says, Brush your teeth, Billy brushes his teeth. If his mother says, Go to bed, Billy goes to bed. Billy is a very good boy. A good boy listens to his mother. His mother doesn't have to ask him again. She asks him to do something one time, and she doesn't ask again. Billy is a good boy. He does what his mother asks the first time. She doesn't have to ask again. She tells Billy, You are my best child. Of course Billy is her best child. Billy is her only child."

# load a spaCy model, depending on language, scale, etc.
nlp = spacy.load("en_core_web_sm")

# add PyTextRank to the spaCy pipeline
nlp.add_pipe("textrank")
doc = nlp(text)

# examine the top-ranked phrases in the document
for phrase in doc._.phrases:
    print(phrase.text)
    #print(phrase.rank, phrase.count)
    #print(phrase.chunks)
