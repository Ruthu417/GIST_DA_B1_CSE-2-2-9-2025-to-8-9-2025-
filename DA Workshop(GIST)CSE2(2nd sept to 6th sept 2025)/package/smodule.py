#string module
def is_palindrome(st):
    if st==st[::-1]:
        return True
    else:
        return False
    
def string_methods():
    st=input("Enter the string:")
    ch=input("Enter the char:")
    print("string startswith=",st.startswith(ch))
    print("string endswith=",st.endswith(ch))
    print("char frequency=",st.count(ch))
    print("string title=",st.title())
    print("swapped string=",st.swapcase())
    print("string lower=",st.lower())
    print("string upper=",st.upper())
    print("string length=",len(st))
    
#string_methods()