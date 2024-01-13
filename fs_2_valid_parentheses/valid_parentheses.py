def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    stack = []
    parentheses = {')': '('}

    for char in parens:
        if char in parentheses.values():
            stack.append(char)
        elif char in parentheses.keys():
            if not stack or stack.pop() != parentheses[char]:
                return False
            
    return not stack