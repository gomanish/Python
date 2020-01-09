'''  The LetterChanges(str): function Replace every letter in the string with the letter following it in the alphabet 
(ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and 
finally return this modified string. '''

def LetterChanges(str):
  newstr = ""
  outstr = ""
  for char in str:
    if char.isalpha():
        if char != "z":
          newstr = newstr + chr(ord(char)+1)
        else:
          newstr = newstr + "a"
    else:
      newstr = newstr + char
  
  for char in newstr:
      if (char == "a") or (char == "e") or (char == "i") or (char == "o") or (char == "u"):
        char = char.upper()
      outstr = outstr + char
  return outstr


print(LetterChanges(raw_input()))     # Make function call
