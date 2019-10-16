#!/usr/bin/python3
import json
import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


name = "add_item.json"
try:
    listt = load_from_json_file(name)
except:
    listt = []

for i in range(1, len(sys.argv)):
    listt.append(sys.argv[i])

save_to_json_file(listt, name)
