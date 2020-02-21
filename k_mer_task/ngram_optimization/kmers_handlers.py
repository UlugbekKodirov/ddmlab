def slicing_ngram_list(seq, k):
    """SLICING (list) -> SET"""
    kmers = []
    for i in range(len(seq)-k+1):
        kmers.append(seq[i:i+k])
    return kmers


def slicing_ngram_generator(seq, k):
    """SLICING (generator) -> SET"""
    for i in range(len(seq)-k+1):
        yield seq[i:i+k]


def slicing_ngram_set(seq,k):
    """SLICING - adding to set"""
    kmers = set()
    for i in range(len(seq)-k+1):
        kmers.add(seq[i:i+k])
    return kmers


def custom_nltk_ngrams_list(seq, n):
    """CUSTOM NLTK.NGRAMS (list) -> SET"""
    sequence = iter(seq)
    history = []
    while n > 1:
        try:
            next_item = next(sequence)
        except StopIteration:
            # no more data, terminate the generator
            return
        history.append(next_item)
        n -= 1
    result = []
    for item in sequence:
        history.append(item)
        result.append("".join(history))
        del history[0]
    return result


def custom_nltk_ngrams_generator(seq, n):
    """CUSTOM NLTK.NGRAMS (generator) -> SET"""
    sequence = iter(seq)
    history = []
    while n > 1:
        try:
            next_item = next(sequence)
        except StopIteration:
            # no more data, terminate the generator
            return
        history.append(next_item)
        n -= 1
    for item in sequence:
        history.append(item)
        yield "".join(history)
        del history[0]


def custom_nltk_ngrams_set(seq, n):
    """CUSTOM NLTK.NGRAMS - adding to set"""
    sequence = iter(seq)
    history = []
    while n > 1:
        try:
            next_item = next(sequence)
        except StopIteration:
            # no more data, terminate the generator
            return
        history.append(next_item)
        n -= 1
    result = set()
    for item in sequence:
        history.append(item)
        result.add("".join(history))
        del history[0]
    return result

