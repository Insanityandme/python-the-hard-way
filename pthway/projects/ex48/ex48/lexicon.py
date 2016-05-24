"""Script to convert user input into something the computer understands."""

LEXICON = {
            'north': 'direction',
            'south': 'direction',
            'east': 'direction',
            'west': 'direction',
            'down': 'direction',
            'up': 'direction',
            'left': 'direction',
            'right': 'direction',
            'back': 'direction',
            'go': 'verb',
            'stop': 'verb',
            'kill': 'verb',
            'eat': 'verb',
            'the': 'stop',
            'in': 'stop',
            'of': 'stop',
            'from': 'stop',
            'at': 'stop',
            'it': 'stop',
            'door': 'noun',
            'bear': 'noun',
            'princess': 'noun',
            'cabinet': 'noun',
        }


def scan(words, lexicon=LEXICON):
    """Returns a list of tuples containing (TOKEN, WORD) pairings."""
    words = words.split()
    pairs = []
    for word in words:
        cn = convert_number(word)
        wl = word.lower()
        if wl in lexicon:
            pairs.append((lexicon[wl], wl))
        elif cn is None and word not in lexicon:
            pairs.append(('error', word))
        elif type(cn) == int:
            pairs.append(('number', cn))

    return pairs


def convert_number(s):
    """Tests if something is a number."""
    try:
        return int(s)
    except ValueError:
        return None
