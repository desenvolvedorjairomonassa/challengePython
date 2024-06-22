def is_palindrome(string):
  """that takes a string as an argument and returns 
  True if it's a palindrome, and False otherwise. A palindrome is a word, 
  number, phrase, or other sequence of symbols that reads the same backward as forwards, such as madam or racecar."""
    reverse_list = list(string)[::-1]
    reverse_str = ''.join(reverse_list)
    return reverse_str == string
