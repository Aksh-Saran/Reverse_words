def reverse_words(str):     # Starting by defining a function and passing 'str' as a parameter
    result = []             # Storing result as an empty array
    i = 0                   # Initializing i to 0
    n = len(str)            # Storing the length of 'str' in 'n'

    while i < n:            # Checking if it is an empty string          
        if str[i].isalnum():  # It iterates through the given word by checking if it is alphanumeric
            start = i
            while i < n and str[i].isalnum():
                i += 1
            word = str[start:i] # If a non alphanumeric character is found like ;, then the word is sliced till 'i'
            result.append(word[::-1])  # The word till alphanumeric  character is reversed using slicing operation and added to 'result' array
        else:
            result.append(str[i]) # For a non alphanumeric character, the word is directly appended to the 'result' array
            i += 1

    return ''.join(result)  # The final result(alnum and non alnum) is merged to form a single output string. 

# Simple test
test_str = "String; 2be reversed..."
expected = "gnirtS; eb2 desrever..."
assert reverse_words(test_str) == expected
