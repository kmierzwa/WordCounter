"""25 most popular english words in txt"""
import sys

def Counter(subtitleFile, questedWordsFile):
        qwDict = {}

        for qw in qwWords:
             qwDict.update({qw:subWords.count(qw.strip())})
        print qwDict

def ChangeFile(s, f, mode):
        orig_stdout = sys.stdout
        changeFile = open(f, mode)
        sys.stdout = changeFile
        print s
        sys.stdout = orig_stdout
        changeFile.close()
                
subFile = "F1_T4_Subtitle - English.srt"
qwFile = "out.txt"

subWords = open(subFile).read().split(' ')
qwWords = open(qwFile).read().replace('\n','').replace(' ','').split(',')

user_input = raw_input('add new word to the list, if word exists would be removed ').replace('\n','')

if user_input in qwWords:
       answear = raw_input("Ar u wsiur?(Y/N)")
       if answear == 'Y':
               qwWords.remove(user_input)
               ChangeFile(",".join(qwWords), qwFile, 'w')
else:
        ChangeFile(','+user_input, qwFile, 'a')

Counter(subWords, qwWords)

