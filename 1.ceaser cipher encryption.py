def encrypt(text,s):
    s=s   
    text =text.replace(" ","")
    result=""  
    for i in range(len(text)):
        char=text[i]
        if(char.isupper()):  
            result=result+chr((ord(char)+s-65)%26+65)
        else:
            result=result+chr((ord(char)+s-97)%26+97)
    return result
word=str(input("enter the word:"))
k=int(input("Enter the key: "))
print("Encoded word in Caeser cipher is: ",encrypt(word,k))
