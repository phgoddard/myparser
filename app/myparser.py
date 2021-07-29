import os
import re

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
    def __init__(self, filename: str, outfilename: str):
        #class level variables
        self.cwd = str
        self.WorkingDir = str
        self.filename = filename
        self.DialogLines = []
        self.cleanListText = []
        self.noTimeStampsText = []
        self.speaker = str
        self.speakers = []
        self.speakerSet = set
        self.speakerList = []
        self.speaker_segments = []
        self.metaData = []
        self.questions = []
        self.responses = []
        self.finalDialog = []
        self.outfilename  = outfilename

        #initialized class methods
        self.WorkingDir = self.changeWorkingDir()
        self.DialogLines = self.readFile()
        self.cleanListText = self.cleanNLandNumbers()
        self.noTimeStampsText = self.cleanTimeStamps()
        self.speakerSet = self.getSpeakers()
        self.cleanListText = self.getMetaData()
        #self.speaker_segments = self.getSpeakerDialog(0)

    def changeWorkingDir(self):
        self.WorkingDir = os.chdir('/Users/tandemseven/Desktop/HLT Program/596A HLT Internship/Thematic-data/docusignresearchtranscriptthemetopicevaluation')
        return os.getcwd()

    def readFile(self):
        #first data file created: -> DialogLines
        for line in open(self.filename,'r'):
            self.DialogLines.append(line)
        return self.DialogLines

    def cleanNLandNumbers(self):
        #removes newlines and integer IDs for snippet of dialog: -> cleanListText
        self.rx = '^\d\d*\\n'
        for line in self.DialogLines:
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

    def getSpeakerDialog(self, speaker:str):
        #takes speaker name as input and loops through each line/string in cleanListText
        #if speaker name is present in line, extracts line for that speaker
        #writes all speaker lines to an output file, does not write timestamps
        #stores speaker lines in list of tuples: speaker_segments
        #each line is tuple: [(1,'Mike Melton: text....),(15, 'Mike Melton: text'),(),()]

        self.speaker_segments = []
        for i, line in enumerate(self.cleanListText):
            self.res = re.search(speaker, line)
            if self.res:
                self.speaker_segments.append((i,line))

        #write file
        self.speakfile = open(speaker+"_dialog.txt",'w')
        self.speakfile.write("Speaker Dialog: ")
        self.speakfile.write(speaker+'\n')
        for i, sent in enumerate(self.speaker_segments):
            self.speakfile.write(str(i) + ' ')
            self.speakfile.write(sent[1])
            self.speakfile.write('\n')
        self.speakfile.close()

        return self.speaker_segments

    def getFinalDialog(self, speaker1: str, speaker2: str, skip: int):
        #combines question and response files as a time sequence using the ID of each tuple
        #skip is used if transcipt has incremental ID for each utternance, sometimes all odd or even
        self.questions = self.getSpeakerDialog(speaker1)
        self.responses = self.getSpeakerDialog(speaker2)
        self.counter = len(self.questions) + len(self.responses)
        print("length of dialog: ", self.counter)
        self.qcounter = 0
        self.rcounter = 0
        k=1
        for i in range(0,self.counter-1):
            if self.questions[self.qcounter][0] == k:
                print(i,"Qk: ", self.questions[self.qcounter][0],"Qcounter: ",self.qcounter, self.questions[self.qcounter][1])
                self.finalDialog.append(self.questions[self.qcounter][1])
                self.qcounter+=1
            else:
                self.finalDialog.append(self.responses[self.rcounter][1])
                print(i,"Rk: ", self.responses[self.rcounter][0],"Rcounter: ",self.rcounter, self.responses[self.rcounter][1])
                self.rcounter+=1
            k+=skip
        return self.finalDialog

    def saveDialog(self, data: list):
        #writes out cleanListText (both interviewer and respondent) with metadata
        self.outFile = open(self.outfilename,'w')
        self.outFile.write("Input file: ")
        self.outFile.write(self.filename + '\n')

        self.outFile.write("Speakers: ")
        for i in range(len(self.speakerList)):
            self.outFile.write(self.speakerList[i])
            self.outFile.write('\n')

        for i, sent in enumerate(data):
            self.outFile.write(str(i) + ' ')
            self.outFile.write(sent + '\n')
        self.outFile.close()



if __name__ == "__main__":

    d = Dialog('Docusign_p08.txt','notimestamps_Docusign_p08.txt')
    print(d.filename)
    print(d.outfilename)
    print("output dialogLines: ",d.DialogLines[:10])
    print("output cleanListText: ",d.cleanListText[:10])
    print("output noTimeStampText: ",d.noTimeStampsText[:10])
    print("output getSpeakers: ",d.getSpeakers())
    print("output getMetaData: ",d.getMetaData())
    d.saveDialog(d.noTimeStampsText)


