def scramble(myList):
    ogList = myList
    print(myList)
    for i in range(len(myList)):
        j = i + 1
        if j < len(myList):
            myList[i], myList[j] = myList[j], myList[i]
            print(myList)
            myList = ogList


if __name__ == "__main__":
    myList = ['foo', 'roo', 'doo']
    scramble(myList)
