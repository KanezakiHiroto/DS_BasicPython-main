text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

words = ''.join(map(lambda word: str(len(word.strip(',.'))),text.split()))
print(words)
