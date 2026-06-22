str1 = "This is python code @anuj @# $$"
str1 = str1.rsplit(" ", 1)[0]
vowels="aeiouAEIOU"
str1 = str1.replace(" ", "")
remove_vowel= ''.join(a for a in str1 if a.lower() not in 'aeiouAEIOU')
for i in str1:
    if i in vowels:
        print(i)
for j in str1:
    if not j.isalnum() and not j.isspace():
        print(j)        

print(str1)
print(remove_vowel)
print(str1)