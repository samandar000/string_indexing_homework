def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    n=0
    if s[0]=='*':
        n+=1
    if s[1]=='*':
        n+=1
    if s[2]=='*':
        n+=1 
    if s[3]=='*':
        n+=1    
    if s[4]=='*':
        n+=1        
    elif n==0:
        return False

        
    return n

        