#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
Stupid Backoff
    http://acl.ldc.upenn.edu/D/D07/D07-1090.pdf
    http://pastebin.com/0axkuqdv
"""

__author__ = 'Yuta Hayashibe' 
__version__ = ""
__copyright__ = ""
__license__ = "GPL v3"


import myssgnc
import math

class SBLM(object):

	def __init__(self, fname, n, constant, total):
		self.total = total
		self.N = n
                self.agent = myssgnc.MyAgent(fname)
                self.constant = constant

	def _score(self, tokens, head, tail):
            assert isinstance(tokens, list) or isinstance(sentence, tuple)
            assert isinstance(head, int)
            assert isinstance(tail, int)

            score = 0.0

            freq =  self.agent.get_frequency(' '.join(tokens[head:tail]))
            if tail - head == 1:
                if freq >0:
                    score += freq / self.total
                else:
                    score = 0 

            else:
                if freq > 0:
                    sub_freq =  self.agent.get_frequency(' '.join(tokens[head:tail-1]))
                    score += freq / float(sub_freq)
                else:
                    sub_score = self._score(tokens, head+1, tail)
                    score += (self.constant * sub_score)

            return score


	def score(self, sentence):
            assert isinstance(sentence, list) or isinstance(sentence, tuple)
            score = 0.0 

            if len(sentence) < self.N:
                return float('NaN')

            for head in xrange(0, len(sentence) - self.N + 1):
                score += self._score(sentence, head, head + self.N)
            return score



if __name__ == "__main__":
    import optparse
    parser = optparse.OptionParser()
    parser.add_option('-f', dest = 'file')

    #'Web 1T 5-gram Version 1'
    # http://www.ldc.upenn.edu/Catalog/CatalogEntry.jsp?catalogId=LDC2006T13
    parser.add_option('-t', '--total', dest = 'total', type=int, default = 1024908267229)
    parser.add_option('-n', '--ngram', dest = 'n', type=int, default = 3)
    parser.add_option('-c', '--constant', dest = 'constant', type=float, default = 0.4)

    (opts, args) = parser.parse_args()


    if not opts.file:
        raise 'Designate the file name'
    elif not opts.total:
        pass
    else:
        sblm = SBLM(opts.file, opts.n, opts.constant, opts.total)
        tests = [u"I live in Canada",
                u"I live in USA",
                u"I live in Tokyo",
                u"I live in Nara",
                u"I live in Ikoma",
                u"I live in NAIST",
                u"I live in matsu-lab",
                u"AVEWE RGEBF RGR",
                ]

        for sent in tests:
            score = sblm.score(sent.split())
            print ''
            print sent
            print score

