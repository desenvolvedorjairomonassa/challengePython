def reverse_string(input_string):
    if input_string != "":
        reverse = list(input_string)
        reverse = reverse[::-1]
        return ''.join(reverse)
    else: 
        return ""
