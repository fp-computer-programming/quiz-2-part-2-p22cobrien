# Author: CMOB 11/17/2021

sentence = input("Please enter a positive or negative input. ")

sentence1 = sentence
sentence1.lower()

if "not" not in sentence1:
    print("You're not " + sentence + ". Now SCRAM!")
elif "not" in sentence1:
    if "not" == sentence1:
        print("Say something more than just not")
    else:
        print(sentence)
