import re

sentences = ('I am looking for Jane.', 'Jane was walking along the river.',
             'Kate and Jane are close friends.')

pattern = re.compile(r'^Jane')

for sentence in sentences:

    if re.search(pattern, sentence):  # == if pattern.search(sentence):
        # print(sentence)
        result = re.compile(r'^Jane').search(sentence).group()
        print(result)
