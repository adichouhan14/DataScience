
reverseString= lambda s: s[::-1]

changeChar= lambda s: s[0]+(s[1:].replace(s[0],"$"))

removeChar = lambda s,n: s[:n]+s[n+1:]

print(reverseString('abcd'))
print(changeChar("restart"))
print(removeChar("This iis error",5))
