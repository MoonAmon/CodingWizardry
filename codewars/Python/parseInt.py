def parse_int(string):
    number = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twenteen': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fiveteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
        'thirty': 30,
        'forty': 40,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90,
        'hundred': 100,
        'thousand': 1000,
        'million': 1000000
    }

    total = 0
    current = 0
    
    string = string.replace('-', " ")
    words = string.split()

    for word in words:
        if word == 'and':
            continue
        if word == 'hundred' or word == 'thousand' or word == 'million':
            current *= number[word]
            if word == 'thousand' or word == 'million':
                total += current
                current = 0
            
        else:
            current += number[word]
        print(word, current, total + current)
    return total + current

parse_int('seven hundred ninety-six thousand eight hundred twenty-three')