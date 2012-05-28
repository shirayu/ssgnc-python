#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""

__author__ = 'Yuta Hayashibe' 
__version__ = ""
__copyright__ = ""
__license__ = "GPL v3"

import random
import unittest

import ssgnc

class Test(unittest.TestCase):
    def setUp(self):
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

        INDEX_PATH = "/data/google-ngram-en/index/"
        self.d = ssgnc.Database()
        self.d.open(INDEX_PATH)

        self.q = ssgnc.Query()
        self.q.parseKeyValue(ORDER_OPTION['FLAG'], ORDER_OPTION['DEFAULT'])
        self.q.parseKeyValue(RESULTS_OPTION['FLAG'], RESULTS_OPTION['DEFAULT'])

    def tearDown(self):
        pass


    def search(self, query):
        assert isinstance(query, str) or isinstance(query, unicode)
        ret = {}
        if self.d.parseQuery(query, self.q):
            agent = ssgnc.Agent()
            if self.d.search(self.q, agent):
                myagent = ssgnc.MyAgent(agent)
                while myagent.next():
                    ret[myagent.getToken(self.d)] = myagent.getFreq(self.d)
        return ret

    def test_search(self):
        self.assertEqual(self.search("."), {'.': 22000000000})
        self.assertEqual(self.search("<S>"), {'<S>': 95100000000})

        self.assertEqual(self.search("orange"), {'orange': 9640000})
        self.assertEqual(self.search("愛"), {})
#        self.assertRaises(TypeError, self.search(u"orange tea"))

        self.assertEqual(self.search("orange tea"), {'orange tea':1570})
        self.assertEqual(self.search("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"), {})

        self.assertEqual(len(self.search("* tea")) > 5, True)



if __name__ == '__main__':
    unittest.main()
