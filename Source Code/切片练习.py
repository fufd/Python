def trim(s):
    if s[:1] != " " and s[-1:] != " ":
        return s
    elif s[:1] == " ":
        s = s[1:]
        return trim(s)
    elif s[-1:] == " ":
        s = s[:-1]
        return trim(s)

a=" cc "
print(a)
d=trim(a)
print(d)