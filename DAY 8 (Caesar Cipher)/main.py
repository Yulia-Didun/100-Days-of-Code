from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def ceasar(direction, text, shift):
  shift %= 26
  result_text = ""
  
  if direction == "decode":
    shift *= -1

  for char in text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift
      result_text += alphabet[new_position]
    else:
      result_text += char

  print(f"The {direction}d text is {result_text}.")

should_continue = True

while should_continue:
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  ceasar(direction, text, shift)
  
  desicion = input("\nDo you want to continue? Type 'yes' or 'no': ").lower()

  if desicion == 'no':
    should_continue = False
    print("Goodbye!")