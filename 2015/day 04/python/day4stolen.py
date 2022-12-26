# https://www.reddit.com/r/adventofcode/comments/3vdn8a/comment/cxmmc2b/?utm_source=share&utm_medium=web2x&context=3

from itertools import count
from hashlib import md5    

for x in count(1):
    test = 'bgvyzdsv' + str(x)
    if md5(test.encode('utf-8')).hexdigest()[:6] == '000000':
        print(x)
        break


# I had to edit my test. Forgot the () after hexdigest.