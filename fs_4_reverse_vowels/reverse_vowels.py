def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    s_list = list(s)

    vowels = set('aeiouAEIOU')

    left, right = 0, len(s_list) - 1

    while left < right:
        while left < right and s_list[left].lower() not in vowels:
            left += 1

        while left < right and s_list[right].lower() not in vowels:
            right -= 1

        s_list[left], s_list[right] = s_list[right], s_list[left]

        left += 1
        right -= 1
    return ''.join(s_list)