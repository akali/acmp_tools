# -*- coding: utf-8 -*-
#!/usr/bin/env python

import urllib2
from BeautifulSoup import BeautifulSoup

def printToFile(fname, arr):
    print >> open(fname, 'w'), len(arr), u' '.join(arr)

def check(cur_id, problems):
	web_page = urllib2.urlopen("http://acmp.ru/index.asp?main=user&id=" + cur_id).read()
	soup = BeautifulSoup(web_page)

	name = soup.html.body.table.tr.nextSibling.nextSibling.nextSibling.nextSibling.td.table.tr.td.nextSibling.nextSibling.table.tr.td.nextSibling.nextSibling.nextSibling.nextSibling.next

	# print name

	solved = 0
	for e in soup.html.body.table.findAll('b'):
	    if (e.next.startswith(u'Решенные задачи')):
	        solved = [r.next for r in e.nextSibling.nextSibling.findAll('a')]

	result = ""

	for p in problems:
		if solved.count(p) > 0:
			result = result + ("+")
		else:
			result = result + ("-")

	return result

	# printToFile(cur_id, solved)

print check("93028", ["15", "56", "697"])
