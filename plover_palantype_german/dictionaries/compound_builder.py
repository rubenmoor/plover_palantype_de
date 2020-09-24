LONGEST_KEY = 22

from plover.oslayer.config import CONFIG_DIR

import json

directories_home = CONFIG_DIR + "/"

dictionary = json.load(open(directories_home + "palantype_de.json", encoding="u8"))
words = [word.strip() for word in open(directories_home + "german.dic", encoding="u8").readlines()]
case_reverse = {word.lower(): word for word in words}

# assumes that the result is unique

def lookup(strokes):
    table = [("",)]
    for i in range(len(strokes)):
        next_element = set()
        for j in range(len(table)):
            try:
                part = dictionary["/".join(strokes[j:i+1])].lower()
            except KeyError:
                continue

            for previous_parts in table[j]:
                next_element.add(previous_parts + part)

        table.append(next_element)

    candidates = []
    for word in table[-1]:
        if word in case_reverse:
            candidates.append(case_reverse[word])

    if candidates:
        if len(candidates) >= 2:
            print("More than one candidates:", "/".join(candidates))
            # note: prints to stdout, the log should be redirected somewhere else readable

        return candidates[0]
    else:
        return None
