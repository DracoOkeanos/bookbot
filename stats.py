def count_words(text):
    text.split(sep=None, maxsplit=-1)
    num_words = len(text.split())
    return num_words

def count_characters(text):
    counts = {}
    for ch in text:
        lower_ch = ch.lower()
        if lower_ch in counts:
            counts[lower_ch] += 1
        else:
            counts[lower_ch] = 1
    return counts

def sort_on(item):
    return item["num"]

def sort_characters(char_counts):
    # make an empty list
    result = []
    # loop over char_counts
    for char, num in char_counts.items():
    # append {"char": ..., "num": ...} to the list
        result.append({"char": char, "num": num})
    # Sort result from largest "num" to smallest.
    result.sort(key=sort_on, reverse=True)
    # Return the list
    return result


