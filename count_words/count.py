#!/usr/bin/env python3

from collections import Counter
import re

def count_words(line):
    return dict(Counter(re.findall(r'\b[\w\']+\b', line.lower())))

