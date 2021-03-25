def readFile(fileLoadRoute):
    a = "fileLoadRoute"
    with open(a, "r") as f:
        data = f.read()
        print(data)


if __name__ == '__main__':
    a = "./jsonData/readFile.py"
    readFile(a)
