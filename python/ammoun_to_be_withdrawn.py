#input section
ammount=int(input("ammount to be withdrawn:"))-100

#logic section
two_k=ammount//2000
ammount=ammount%2000

five_h=ammount//500
ammount=ammount%500

two_h=ammount//200
ammount=ammount%200

one_h=ammount//100
ammount=ammount%100

#display section
print("Notes of 2000:",two_k)
print("Notes of 500:",five_h)
print("Notes of 200:",two_h)
print("Notes of 100:",one_h+1)
