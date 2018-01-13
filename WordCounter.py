"""25 most popular english words in txt"""
import sys


def Counter(subtitleFile, questedWordsFile):
        subWords = open(subtitleFile).read().split(' ')
        qwWords = open(questedWordsFile).read().replace('\n','').split(',')
        wordsCounter = dict()
        qwDict = {}

        for qw in qwWords:
             qwDict.update({qw:subWords.count(qw.strip())})
        print qwDict
        
        
       
subFile = "F1_T4_Subtitle - English.srt"

       


qwFile = "out.txt"

#print handle.read()

Counter(subFile, qwFile)

user_input = raw_input('Give me a word: ')
orig_stdout = sys.stdout
appendentWord = open('out.txt', 'a')

sys.stdout = appendentWord

print ',',user_input
sys.stdout = orig_stdout
appendentWord.close()

Counter(subFile, qwFile)

