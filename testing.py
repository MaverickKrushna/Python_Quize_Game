words = input(">")
li1= words.split(" ")
dictt={
    ":)" : " 😊 ",
    ":(" : "😣"
}
result = ""
for word in li1 :
    result += dictt.get(word, word)
print(result)

