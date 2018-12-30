import nltk

doc = open('ZodiacWriting.txt', 'r').read()
sentences = nltk.sent_tokenize(doc)

tagTableList = []
def getTagId(tag):
   if not tag in tagTableList: tagTableList.append(tag) 
   return tagTableList.index(tag)

tags = {}
seq = ""
lenSeq = 0
for s in sentences:
   l = nltk.pos_tag(nltk.word_tokenize(s))
   for word, tag in l:
      if word in [',', '(', ')']: continue #skip non words
      tagId = getTagId(tag)
      seq += "%d, " % tagId
      lenSeq += 1
      if not tagId in tags: tags[tagId] = []
      if not word in tags[tagId]: tags[tagId].append(word)

for tagId in tags:
   print("%d_%s : %s " % (tagId, tagTableList[tagId], tags[tagId]))

seq = "static int obsers[%d] = {%s};" % (lenSeq, seq[:-2])
print("tag table list (len %d) = %s" % (len(tagTableList), tagTableList))
print("tags = %s" % tags)
print(seq)
print("M = %d" % len(tagTableList))
