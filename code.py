from spellchecker import SpellChecker

spell = SpellChecker()

# find those words that may be misspelled
# I write all wrong word and add some correct words in the
# list they recommend me for correct word as you can see
wrong_spelling=spell.unknown(['checkr','wrng','pythn','gret','backspac','something', 'is', 'here',"grammr",'livng'])

for word in wrong_spelling:
    # Get the one `most likely` answer
    print(spell.correction(word))

    # Get a list of `likely` options
    print(spell.candidates(word))
    print("_______________________________________")
