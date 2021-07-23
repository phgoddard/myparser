import cmd

from app.myparser import *
import pytest

def test_readFile():
    d = Dialog("Docusign_p08.txt")
    assert d.DialogLines[:3] == ['WEBVTT\n', '\n', '1\n']

def test_changeWorkingDir():
    d = Dialog("Docusign_p08.txt")
    assert d.changeWorkingDir() == '/Users/tandemseven/Desktop/HLT Program/596A HLT Internship/Thematic-data/docusignresearchtranscriptthemetopicevaluation'

def test_getFileName():
    d = Dialog("Docusign_p08.txt")
    assert d.filename == 'Docusign_p08.txt'
    assert len(d.DialogLines) == 1386
    assert d.DialogLines[:3] == ['WEBVTT\n', '\n', '1\n']

def test_cleanNLandNumbers():
    d = Dialog("Docusign_p08.txt")
    assert d.cleanListText[:3] == ['WEBVTT', '00:00:04.170 --> 00:00:05.819', 'Mike Melton: Can you tell me about your business.']