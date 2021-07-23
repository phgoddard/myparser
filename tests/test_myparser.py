from app.myparser import *

def test_fileName():
    assert getFilename('file') == 'hellofile'