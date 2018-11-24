

def readText():
    lines = []
    inFile = open("InText.txt", 'r')
    for line in inFile:
        lines.append(line.rstrip().lower())
    inFile.close()
    return lines

def makeFunnyText(text):
    cipher = text
    return cipher

def save(svg):
    pass

if __name__ == '__main__':
    text = readText()
    print("plain text:")
    for line in text:
        print(line)
    cipher = makeFunnyText(text)
    save(cipher)
