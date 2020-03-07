list_books = ["dracula.txt", "frankestein.txt", "the_jungle_book.txt"]
words = []

for book in list_books:
    fp = open(book, "r")

    punct = [".","," ,"!", "?", "-", ";", ":", '"', "'", "--", "(", ")"]

    text = ""

    for line in fp:
        for p in punct:
            line = line.replace(p, "")
        #print(line)

        text = text + line

    #print(text)

    list_text = text.split()
    #print(list_text)
    new_words = []
    for element in list_text:
        if element not in new_words:
            new_words.append(element)

    words.append(len(new_words))

    print("number of different words in " + book, len(new_words))
    print("total number of words in " + book, len(list_text))

variable = max(words)
winner = words.index(max(words))

print("the winner is ", list_books[winner])

