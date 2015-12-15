from django.http import *
import os
import collections

PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = ( PROJECT_PATH + '/templates')


def func(request, filename):
    file_path = (TEMPLATE_DIRS + '/%s' %filename)
    file = open(file_path,"r+")
    info = 'Name: %s <br> Words: <br>' %filename
    wordcount = collections.Counter()
    for line in file:
        wordcount.update(line.split())
    for k,v in wordcount.iteritems():
        info += '%s,%d <br>' %(k,v)
    file.close()
    return HttpResponse(info)

