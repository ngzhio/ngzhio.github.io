from sys import argv
from slugify import slugify
import os

title = len(argv) >= 2 and argv[1] or "New Post"
drafts_path = '_drafts'
template = f'''\
---
title: "{title}"
categories: []
tags: []
---
'''

if not os.path.isdir(drafts_path):
    os.mkdir(drafts_path)

filename = drafts_path + '/' + slugify(title) + '.md'
if not os.path.isfile(filename):
    f = open(filename, 'w', encoding='UTF-8')
    f.write(template)
    f.close()
    print('Created a new post: ' + filename)
