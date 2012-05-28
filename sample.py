#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""

__author__ = 'Yuta Hayashibe' 
__version__ = ""
__copyright__ = ""
__license__ = "GPL v3"

DIR = '/data/google-ngram-en/index/'

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
q.parseKeyValue(ORDER_OPTION['FLAG'], ORDER_OPTION['DEFAULT'])
q.parseKeyValue(RESULTS_OPTION['FLAG'], RESULTS_OPTION['DEFAULT'])

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
