# -*- coding: utf-8 -*-
import csv
import random

outfile_name = 'test_outfile.csv'

outline = []
outlist = []
start_month = 4
start_year = 2018
edit_year = start_year
edit_month = 0

for i in range(18):
    outline = []
    edit_month = start_month + i
    if edit_month > 12:
        edit_month = edit_month - 12
    if edit_month == 4:
        edit_year = edit_year + 1
    outline.append('No' + str(i))
    outline.append('太郎')
    outline.append(edit_year)
    outline.append(edit_month)
    outline.append(random.randrange(3))
    outlist.append(outline)

edit_year = start_year
for i in range(24):
    outline = []
    edit_month = start_month + i
    if edit_month > 12:
        edit_month = edit_month - 12
    if edit_month == 4:
        edit_year = edit_year + 1
    outline.append('No' + str(i))
    outline.append('二郎')
    outline.append(edit_year)
    outline.append(edit_month)
    outline.append(random.randrange(20))
    outlist.append(outline)

edit_year = start_year
for i in range(12):
    outline = []
    edit_month = start_month + i
    if edit_month > 12:
        edit_month = edit_month - 12
    if edit_month == 4:
        edit_year = edit_year + 1
    outline.append('No' + str(i))
    outline.append('花子')
    outline.append(edit_year)
    outline.append(edit_month)
    outline.append(random.randrange(5))
    outlist.append(outline)

outfile = open(outfile_name, 'w')
out_csv_writer = csv.writer(outfile, delimiter=',')
out_csv_writer.writerows(outlist)
outfile.close()
