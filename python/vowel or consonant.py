#This program will read a character from user and check whether it is VOWEL or CONSONANT if entered character was an alphabet using conditional opertors statement.

ch=input()
v='aeiouAEIOU'
if ch in v:
    print('Vowel.')
elif 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
    print('Consonant.')
else: 
    print('Not an alphabet.')
