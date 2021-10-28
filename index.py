paymentTexts = []

# open text file and add text to the list

fileRead = open("text.txt", errors="ignore")

paymentTexts = fileRead.readlines()

fileRead.close()
# loop through the mpesa text lines
processedTexts = []
for paymentText in paymentTexts:
    processedTexts.append(paymentText.split(' '))

# open file to write processed text to

newfile = open('newfile.txt', 'w')
for processedText in processedTexts:
    initialString = ' '.join(map(str, processedText))
    initialString = initialString.replace(',', '')
    # do a code to remove specifics such as receiver etc
    initialString = initialString.replace('[', '')
    initialString = initialString.replace(']', '')
    newfile.write(initialString)
newfile.close()
# print(processedTexts)
