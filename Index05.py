def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    k=0
    if s[0]=="0" or s[0]=="1" or s[0]=="2" or s[0]=="3" or s[0]=="4" or s[0]=="5" or s[0]=="6" or s[0]=="7" or s[0]=="8" or s[0]=="9" :
        k+=1
    if s[1]=="0" or s[1]=="1" or s[1]=="2" or s[1]=="3" or s[1]=="4" or s[1]=="5" or s[1]=="6" or s[1]=="7" or s[1]=="8" or s[1]=="9": 
        k+=1
    if s[2]=="0" or s[2]=="1" or s[2]=="2" or s[2]=="3" or s[2]=="4" or s[2]=="5" or s[2]=="6" or s[2]=="7" or s[2]=="8" or s[2]=="9":
        k+=1
    if s[3]=="0" or s[3]=="1" or s[3]=="2" or s[3]=="3" or s[3]=="4" or s[3]=="5" or s[3]=="6" or s[3]=="7" or s[3]=="8" or s[3]=="9":
        k+=1
    if s[4]=="0" or s[4]=="1" or s[4]=="2" or s[4]=="3" or s[4]=="4" or s[4]=="5" or s[4]=="6" or s[4]=="7" or s[4]=="8" or s[4]=="9":
        k+=1
    return k
print(main('12sd2'))

