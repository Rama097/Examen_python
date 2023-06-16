def divin(a,b):
    if a<b:
        return 0
    else:
        return 1+ divin(a-b,b)