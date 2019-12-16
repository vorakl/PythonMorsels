#!/usr/bin/env python3

from collections import Counter
import re

def count_words(line):
    c = Counter(re.split(r'[^\w\']', line.lower()))
    del(c[''])
    return dict(c)

