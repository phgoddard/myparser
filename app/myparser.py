import os
import re
from db import mysql_repository

class Study():
    #store study name and id for any study that has research associated with it
    def __init__(self, studyname: str, study_id: int):
        #class variables
        self.studyname = studyname
        self.study_id = study_id

class File():
    #store file metadata and the original text from the file
    def __init__(self, filename: str, outfilename: str):
        # class level variables
        self.cwd = str
        self.WorkingDir = str
        self.filename = filename
        self.outfilename  = outfilename
        self.DialogLines = []           #original text is read as lines
        #class methods
        self.WorkingDir = self.changeWorkingDir()
        self.DialogLines = self.readFile()

    def changeWorkingDir(self):
        self.WorkingDir = os.chdir('/Users/tandemseven/Desktop/HLT Program/596A HLT Internship/Thematic-data/docusignresearchtranscriptthemetopicevaluation')
        return os.getcwd()

    def readFile(self):
        #first data file created: -> DialogLines
        for line in open(self.filename,'r'):
            self.DialogLines.append(line)
        return self.DialogLines


class Dialog():
    '''
    Dialog ingests a transcript consisting of an interview between an interviewer and respondent
    Users specify the filename ana assumes the file is in the current working directory
    Methods do the following:
    1 - read
    2 - remove newlines and junk numbers
    3 - Find the speakers (there may be more than 2)
    4 - Extracts the timestamps
    5 - Extracts into two lists the dialog for the interviewer and the respondent
    6 - Removes file meta-data (e.g. the transcript tool name)
    7 -
    '''
    def __init__(self, inputDialog: list):
        self.cleanListText = []         #new lines and extraneous int digits are stripped
        self.noTimeStampsText = []      #all timestamps are removed
        self.speaker = str
        self.speakers = []              #acculumative list of all references to speakers of dialog
        self.speakerSet = set           #just the set of unique speakers is stored
        self.speakerList = []           #set is converted to list
        self.speaker_segments = []      #list of dialog for a given speaker
        self.metaData = []              #everything before the first timestamp
        self.questions = []             #all dialog from the interviewer
        self.responses = []             #all dialog from the respondent

        #initialized class methods

        self.cleanListText = self.cleanNLandNumbers()
        self.noTimeStampsText = self.cleanTimeStamps()
        self.speakerSet = self.getSpeakers()
        self.cleanListText = self.getMetaData()
        #self.speaker_segments = self.getSpeakerDialog(0)

    def cleanNLandNumbers(self):
        #removes newlines and integer IDs for snippet of dialog: -> cleanListText
        self.rx = '^\d\d*\\n'
        for line in f.DialogLines:
            if line != "\n" and not re.search(self.rx,line):
                self.cleanListText.append(line.strip())
        return self.cleanListText

    def cleanTimeStamps(self):
        self.rgTimestamp1 = '\d\d:\d\d:\d\d.\d\d\d --> \d\d:\d\d:\d\d.\d\d\d'
        for line in self.cleanListText:
            res = re.search(self.rgTimestamp1, line)
            if res:
                continue
            else:
                self.noTimeStampsText.append(line)

        return self.noTimeStampsText[1:]

    def getSpeakers(self):
        #reads cleanListText and finds speakers: -> speakerList
        self.rgSpeaker = '[A-za-z]+ ?[A-Za-z]+:'
        for line in self.cleanListText:
            self.smatch = re.search(self.rgSpeaker, line)
            if self.smatch != None:
                self.speakers.append(self.smatch.group())
        self.speakerSet = set(self.speakers)
        self.speakerList = sorted(list(self.speakerSet))
        return self.speakerList

    def getMetaData(self):
        #reads cleanListText and looks for first timestamp, then extracts metadata before it
        #strips metadata off and overwrites cleanListText with list of strings
        #includes timestamps
        i = 0
        self.rgTimestamp1 = '\d\d:\d\d:\d\d.\d\d\d --> \d\d:\d\d:\d\d.\d\d\d'
        while i < 5:
            self.metaData.append(self.cleanListText[i])
            self.res = re.search(self.rgTimestamp1, self.cleanListText[i])
            if self.res:
                self.cleanListText.pop()
                break
            i+=1
        return self.cleanListText[1:]

    def saveDialog(self, data: list):
        #writes out cleanListText (both interviewer and respondent) with metadata
        self.outFile = open(f.outfilename,'w')
        self.outFile.write("Input file: ")
        self.outFile.write(f.filename + '\n')

        self.outFile.write("Speakers: ")
        for i in range(len(self.speakerList)):
            self.outFile.write(self.speakerList[i])
            self.outFile.write('\n')

        for i, sent in enumerate(data):
            self.outFile.write(str(i) + ' ')
            self.outFile.write(sent + '\n')
        self.outFile.close()

if __name__ == "__main__":

    s = Study('Docusign','1')
    print(s.studyname, s.study_id)

    f = File('Docusign_p08.txt','notimestamps_Docusign_p08.txt')
    print(f.filename, f.outfilename)
    print(f.DialogLines[:5])

    d = Dialog(f.DialogLines)
    #repo = mysql_repository()

    print("output cleanListText: ",d.cleanListText[:10])
    print("output noTimeStampText: ",d.noTimeStampsText[:10])
    d.saveDialog(d.noTimeStampsText)


