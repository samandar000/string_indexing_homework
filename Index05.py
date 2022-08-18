def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    n=0
    l="1234567890"
    if s[0] in l:
        n+=1
    elif s[1] in l:
        n+=1
    elif s[2] in l:
        n+=1
    elif s[3] in l:
        n+=1
    elif s[4] in l:
        n+=1
    return n