alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char not in alphabet:
      end_text += char
    else:
      position = alphabet.index(char)
      new_position = position + shift_amount
      if new_position >= len(alphabet):
        new_position = new_position % len(alphabet)
      end_text += alphabet[new_position]
  
  print(f"Here's the {cipher_direction}d result: {end_text}")



#Flow:
from art import logo
print(logo)

on_switch = True
while on_switch == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift >= len(alphabet):
    shift = shift % len(alphabet)

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  go_again = input("Type 'yes' if want to go again. If not, type 'no' ").lower()
  if go_again == "no":
    on_switch = False