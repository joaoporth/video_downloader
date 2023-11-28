import sys, os
sys.path.insert(1, '././')


def get_str(text:str, start, end):

    try:
        return (text.split(start)[1]).split(end)[0]

    except:
        return