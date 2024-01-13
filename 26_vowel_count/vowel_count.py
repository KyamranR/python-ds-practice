def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    vowels = set('aeiou')

    frequency_map = {}

    for char in phrase:
        char_lower = char.lower()

        if char_lower in vowels:
            frequency_map[char_lower] = frequency_map.get(char_lower, 0) + 1

    return frequency_map