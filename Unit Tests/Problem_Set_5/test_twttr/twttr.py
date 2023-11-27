def main():
#Get input.
    userip=input("Input: ")
#Get message without vowels from shorten fn.
    word=shorten(userip)
#Print output.
    print("Output: "+word)
#Shoeten definition.
def shorten(word):
    new_word=""
#Get new word with all vowels removed.
    for i in word:
        if not (i=='a' or i=='A'or i=='e' or i=='E'or i=='o' or i=='O'or i=='i'or i=='I'or i=='u' or i=='U'):
            new_word+=i
#Return the word.
    return(new_word)

if __name__=="__main__":
    main()