import os
import re

class Dialog():

    def __init__(self, filename: str):
        self.cwd = str
        self.WorkingDir = str
        self.filename = filename
        self.DialogLines = []
        self.cleanListText = []

        self.cwd = self.getWorkingDir()
        self.WorkingDir = self.changeWorkingDir()
        self.DialogLines = self.readFile()
        self.cleanListText = self.cleanNLandNumbers()

    def getWorkingDir(self):
        self.cwd = os.getcwd()
        return self.cwd

    def changeWorkingDir(self):
        self.WorkingDir = os.chdir('/Users/tandemseven/Desktop/HLT Program/596A HLT Internship/Thematic-data/docusignresearchtranscriptthemetopicevaluation')
        return os.getcwd()

    def readFile(self):
        self.DialogLines = []
        for line in open(self.filename,'r'):
            self.DialogLines.append(line)
        return self.DialogLines

    def cleanNLandNumbers(self):
        self.cleanListText = []
        rx = '^\d\d*\\n'
        for line in self.DialogLines:
            if line != "\n" and not re.search(rx,line):
                self.cleanListText.append(line.strip())
        return self.cleanListText

if __name__ == "__main__":

    d = Dialog('Docusign_p08.txt')
    print(d.filename)
    print(d.WorkingDir)
    print(d.cwd)
    print(d.DialogLines[:10])
    print(d.cleanListText[:10])


