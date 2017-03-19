# -*- coding: utf-8 -*-
#!/usr/bin/env python

import urllib2
from BeautifulSoup import BeautifulSoup

def printToFile(fname, arr):
    print >> open(fname, 'w'), len(arr), u' '.join(arr)

def getName(soup, cur_id):
	# web_page = urllib2.urlopen("http://acmp.ru/index.asp?main=user&id=" + cur_id).read()
	# soup = BeautifulSoup(web_page)
	return soup.html.body.table.tr.nextSibling.nextSibling.nextSibling.nextSibling.td.table.tr.td.nextSibling.nextSibling.table.tr.td.nextSibling.nextSibling.nextSibling.nextSibling.next

def getSolved(soup, cur_id):
	for e in soup.html.body.table.findAll('b'):
	    if (e.next.startswith(u'Решенные задачи')):
	        return [r.next for r in e.nextSibling.nextSibling.findAll('a')]
	return []

def check(soup, cur_id, problems):
    solved = getSolved(soup, cur_id)
    return ["+" if solved.count(p) > 0 else "-" for p in problems]

def readList(fname):
	i = open(fname, "r")
	return [x for x in i.read().split('\n')]

problems = readList("problems.txt")
ids = readList("ids.txt")

problems.pop()
ids.pop()

print "<meta charset=\"utf-8\">"

for p in problems:
    print "<a href=\"http://acmp.ru/index.asp?main=task&id_task= + p\">" + p + "</a>"

print "<br>"

# print problems

for cur_id in ids:
    web_page = urllib2.urlopen("http://acmp.ru/index.asp?main=user&id=" + cur_id).read()
    soup = BeautifulSoup(web_page)
    print " <br> ", getName(soup, cur_id), " ", check(soup, cur_id, problems)

# print check("93028", ["15", "56", "697"])
