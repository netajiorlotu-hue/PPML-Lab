def rstring(s):
    if len(s)==0:
        return s
    else:
        return rstring(s[1:])+s[0]
print(rstring("I am sushobhan Pal"))