def filter_by_length(words):
    return list(filter(lambda numLetters: len(numLetters)>= 4, words))

words = ['amor', 'sol', 'piedra', 'dia']   
response = filter_by_length (words)
print(response)