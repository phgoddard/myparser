from app.myparser import *
import pytest


def test_getWorkingDir():
    assert getWorkingDir() == '/Users/tandemseven/Desktop/HLT Program/508 Comp Tech for Linguists/Course Project/508_courseproject/tests'

def test_changeWorkingDir():
    assert changeWorkingDir() == '/Users/tandemseven/Desktop/HLT Program/596A HLT Internship/Thematic-data/docusignresearchtranscriptthemetopicevaluation'

def test_getFileName():
    assert getFileName() == 'Docusign_p08.txt'

def test_readFile():
    assert (readFile())[:3] == ['WEBVTT\n', '\n', '1\n']

def test_cleanNLandNumbers():
    listText = readFile()
    assert cleanNLandNumbers()
