def clearDigits(s: str) -> str:
    stk = []
    for c in s:
        if c.isalpha():
            stk.append(c)
        else:
            stk.pop()
    return "".join(stk)