'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for 
player plays (using input), compare them, print out a message 
of congratulations to the winner, and ask if the players want to
start a new game Remember the rules:
Rock beats scissors Scissors beats paper Paper beats rock'''

#input section
Name1=(input())
Name2=(input())
dicision1=int(input())
dicision2=int(input())

#logic section
if dicision1==Rock and dicision2==scissors:
   print("{Name1}",Win)
elif dicision1==scissors and dicision2==paper:
   print("{Name1}",Win)
elif dicision1==paper and dicision2==Rock:
    print("{Name1}",Wins)
else:
    print("{Name2}",Wins)

