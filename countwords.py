sentence="how are how is how are joke are king are"
words=sentence.split()
col=dict()
for word in words:
  if word in col:
    col[word]=col[word]+1
  else:
    col[word]=1

wordCount=0
mostWord=""
for key in col.keys():
    if col[key]>wordCount:
        wordCount=col[key]
        mostWord=key

print(col)
print(mostWord)
