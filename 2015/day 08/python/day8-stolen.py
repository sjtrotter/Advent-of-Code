# from https://www.reddit.com/r/adventofcode/comments/3vw32y/comment/cxrad1k/?utm_source=share&utm_medium=web2x&context=3
# requires a newline at the end of input for part1

print (sum(len(s[:-1]) - len(eval(s)) for s in open('../input.txt')))
print (sum(2+s.count('\\')+s.count('"') for s in open('../input.txt')))

# D: lol too clean to modify honestly.
# I think my issue was the way I was parsing the strings. I also didn't use eval.