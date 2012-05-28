#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""

__author__ = 'Yuta Hayashibe' 
__version__ = ""
__copyright__ = ""
__license__ = "GPL v3"

DIR = '/data/google-ngram-en/index/'
DUMMYFILENAME='dummy.txt'

ORDER_OPTION = { "FLAG" : "--ssgnc-order",
                "UNORDERED" : "UNORDERED",
                "ORDERED" : "ORDERED",
                "PHRASE" : "PHRASE",
                "FIXED" : "FIXED",
                "DEFAULT" : "FIXED" }
RESULTS_OPTION = { "FLAG" : "--ssgnc-max-num-results",
                "DEFAULT" : "20" }
FLEQ_OPTION = { "FLAG" : "--ssgnc-min-freq",
                "DEFAULT" : "0" }
NGRAM_OPTION = { "FLAG" : "--ssgnc-num-tokens",
                "DEFAULT" : "1-7" }


import ssgnc
d = ssgnc.Database()
d.open(DIR)

q = ssgnc.Query()
q.setOption(ORDER_OPTION['FLAG'], ORDER_OPTION['DEFAULT'])
q.setOption(RESULTS_OPTION['FLAG'], RESULTS_OPTION['DEFAULT'])

def printout(query):
    if d.parseQuery(query, q):
        agent = ssgnc.Agent()
        if d.search(q, agent):
            myagent = ssgnc.MyAgent(agent)
            print "--"
            while myagent.next():
                print myagent.getToken(d), myagent.getFreq(d)

printout("the")
printout("hot tea")
printout("hot")
printout("tea")
printout(".")
printout("I had * tea")

def search(query):
    if d.parseQuery(query, q):
        agent = ssgnc.Agent()
        if d.search(q, agent):
            myagent = ssgnc.MyAgent(agent)
            while myagent.next():
                tk = myagent.getToken(d)
                freq = myagent.getFreq(d)

def testSpeed():
    i = 0
    from time import time
    start = time()
    line = allLines = open(DUMMYFILENAME).read()
    items = line.split()
    leng = len(items)
    for item in items:
        search(item)
        i += 1
    for j in xrange(0, leng-3):
        search(" ".join(items[j:j+2]))
        search(" ".join(items[j:j+3]))
        i += 2
    end = time()
    return end - start, i

print "======"
print "===SPEED TEST (x3)==="
for i in xrange(0,3):
    tm, cnt = testSpeed()
    print "%dth : %f (%d times call)" % (i, tm, cnt)
print "===FINISED==="
print "======"

#if __name__ == '__main__':

