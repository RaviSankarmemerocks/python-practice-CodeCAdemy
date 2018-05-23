pig="ay"
name=raw_input("enter your name")
if len(name)>0 and name.isalpha():
  word=name.lower()
  first=word[0]
  new_word=word+first+pig
  new_word=new_word[1:len(new_word)]
  print new_word
else:
  print "invalid string"
