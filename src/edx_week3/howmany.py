animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

values = animals.values()
returnVal = []
for val in values:
    returnVal += val
i = len(returnVal)
print(i)
