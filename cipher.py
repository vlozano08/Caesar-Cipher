def shift_char(char, shift):
    if char.isalpha():
      base = ord('A') if char.issupper() else ord('a')
      return chr((ord(char)-base+shift) % 26 + base)
    return char
def encrypt(test, shift):
  return "".join(shift_char(char, shift) for char in text)

def decript(text, shift):
  return enctypt(text, -shift)

