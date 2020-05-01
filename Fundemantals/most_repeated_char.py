from pprint import pprint
sentence = "this is a common interview question"
char_frequency = {}
count = 0
for ch in sentence.rstrip():
    if ch in char_frequency:
        char_frequency[ch] += 1
    else:
        char_frequency[ch] = 1

items = sorted(char_frequency.items(),
               key=lambda kv: kv[1], reverse=True)
# items.sort(key=lambda item: item[1])

pprint(items[0])
