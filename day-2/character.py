# Write a sample program to teach characters
# Declare a character
char = 'a'
print("The character is:", char)

# Get the ASCII value of the character
ascii_val = ord(char)
print("The ASCII value of", char, "is:", ascii_val)

# Convert ASCII value back to character
char_again = chr(ascii_val)
print("The character for ASCII value", ascii_val, "is:", char_again)

# Converting small letter to capital letter modifying ascii value
small_char = 'a'
print("The small letter is:", small_char)

# Get the ASCII value of the small letter
ascii_val = ord(small_char)
print("The ASCII value of", small_char, "is:", ascii_val)

# Convert ASCII value back to capital letter
capital_char = chr(ascii_val - 32)
print("The capital letter for ASCII value", ascii_val, "is:", capital_char)

# Converting capital letter to small letter modifying ascii value
capital_char = 'A'
print("The capital letter is:", capital_char)

# Get the ASCII value of the capital letter
ascii_val = ord(capital_char)
print("The ASCII value of", capital_char, "is:", ascii_val)

