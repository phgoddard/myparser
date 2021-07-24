import os
import re

class Dialog():

    def __init__(self, filename: str):
        #class level variables
        self.cwd = str
        self.WorkingDir = str
        self.filename = filename
        self.DialogLines = []
        self.cleanListText = []
        self.speaker = str
        self.speakers = []
        self.speakerSet = set
        self.speakerList = []
        self.speaker_segments = []
        self.metaData = []

        #initialized class methods
        self.WorkingDir = self.changeWorkingDir()
        self.DialogLines = self.readFile()
        self.cleanListText = self.cleanNLandNumbers()
        self.speakerSet = self.getSpeakers()
        self.cleanListText = self.getMetaData()
        self.speaker_segments = self.getSpeakerDialog()

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
        self.rx = '^\d\d*\\n'
        for line in self.DialogLines:
            if line != "\n" and not re.search(self.rx,line):
                self.cleanListText.append(line.strip())
        return self.cleanListText

    def getSpeakers(self):
        self.rgSpeaker = '[A-za-z]+ ?[A-Za-z]+:'
        for line in self.cleanListText:
            self.smatch = re.search(self.rgSpeaker, line)
            if self.smatch != None:
                self.speakers.append(self.smatch.group())
        self.speakerSet = set(self.speakers)
        self.speakerList = sorted(list(self.speakerSet))
        return self.speakerList

    def getMetaData(self):
        i = 0
        self.rgTimestamp1 = '\d\d:\d\d:\d\d.\d\d\d --> \d\d:\d\d:\d\d.\d\d\d'
        while i < 5:
            self.metaData.append(self.cleanListText[i])
            self.res = re.search(self.rgTimestamp1, self.cleanListText[i])
            if self.res:
                self.cleanListText.pop()
                break
            i+=1
        return self.cleanListText

    def getSpeakerDialog(self):
        for i, line in enumerate(self.cleanListText):
            self.res = re.search(self.speakerList[1], line)
            if self.res:
                self.speaker_segments.append((i,line))
        return self.speaker_segments


if __name__ == "__main__":

    d = Dialog('Docusign_p08.txt')
    print(d.filename)
    print(d.WorkingDir)
    print(d.DialogLines[:10])
    print(d.cleanListText[:10])
    print(d.getSpeakers())
    print(d.speakerList)
    print(d.getMetaData())
    print(d.getSpeakerDialog())


