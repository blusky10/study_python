def changeStringInFile(filePath, orgValue, newValue):
    with open(filePath, "r+") as file_object:
        fileContents = file_object.read()
        newFileContents = fileContents.replace(orgValue, newValue)   
        file_object.seek(0)
        file_object.write(newFileContents)
        file_object.close()

changeStringInFile("c:\\Users\\SDS\\.gitconfig", "#", "")