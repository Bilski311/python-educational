import collections
import re

WORD_RE = re.compile(r'\w+')

index = {}
default_index = collections.defaultdict(list)
with open('zen_of_python', encoding='utf-8') as fp:
    for line_number, line in enumerate(fp):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_number = match.start() + 1
            location = (line_number, column_number)
            index.setdefault(word, []).append(location)
            default_index[word].append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])
    print(word, default_index[word])