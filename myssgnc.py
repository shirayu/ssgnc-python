#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""

__author__ = 'Yuta Hayashibe' 
__version__ = ""
__copyright__ = ""
__license__ = "GPL v3"


import ssgnc

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

class MyAgent(object):
    def __init__(self, INDEX_PATH):
        if isinstance(INDEX_PATH, unicode):
            INDEX_PATH = INDEX_PATH.encode('utf-8') #OK?
        self.d = ssgnc.Database()
        self.d.open(INDEX_PATH)
        self.q = ssgnc.Query()
        self.q.setOption(ORDER_OPTION['FLAG'], ORDER_OPTION['DEFAULT'])
        self.q.setOption(RESULTS_OPTION['FLAG'], RESULTS_OPTION['DEFAULT'])


    def get_frequency(self, query):
        if isinstance(query, unicode):
            query = query.encode('utf-8') #OK?
        assert isinstance(query, str)
        if self.d.parseQuery(query, self.q):
            agent = ssgnc.Agent()
            if self.d.search(self.q, agent):
                myagent = ssgnc.MyAgent(agent)
                if myagent.next():
                    return myagent.getFreq(self.d)
                else:
                    return 0
#                while myagent.next():
#                    tk = myagent.getToken(d)
#                    freq = myagent.getFreq(d)


if __name__=='__main__':
    pass

