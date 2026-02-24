string1 = 'cecilia'
frequencies = {}

for i in string1:
    if i not in frequencies:
        n = 1
        frequencies[i] = n
    else:
        frequencies[i] += n

print('Frequencies for', string1, ':', frequencies)

