# Write a Python program to print all the vowels present in the given list of strings
# # ["Dreamer", "infotech"]

def vowels_present(v):
    vowel = "aeiouAEIOU"
    # Loop through each string in the list
    for j in v:
        # Loop through each character in the current string
        for i  in j:
            # Check if the character is a vowel
            if i in vowel:
                print(i , end=" ")
        print() # Prints a newline after each word for cleaner output

# Given list of strings
words_list = ["Dreamer", "infotech"]

# Call the function
vowels_present(words_list)
