import re
from constraints import numConstraintsMet

#f = 'brown.txt' # try another book as well?
#f = 'ZodiacWriting.txt'
f = 'dummy.txt'

doc = open(f, 'r').read().lower()

#remove all non-letter characters
txt = re.sub('[^a-z]+', '', doc)

n = 136
ngrams = [txt[i:i+n] for i in range(len(txt)-n+1)] 

cur = [0, 0, []]
count = 0
N = len(ngrams)

for grams in ngrams:
   meet, total = numConstraintsMet(grams) 
   if meet > cur[0]:
      cur = [meet, total, [grams,]]
   elif meet == cur[0]: 
      cur[2].append(grams)
   if meet >= 30: print("%d: %s" % (meet, grams))
   count += 1
   if count % N == 1000: print("progress %.3f%%" % (count*100/N,))

print("meet = %d out of %d" % (cur[0], cur[1]))
for t in cur[2]: print(t)
print("<<DONE>>")
