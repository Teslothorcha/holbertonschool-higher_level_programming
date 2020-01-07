#!/bin/bash
# size
curl -sI "$1" | grep Allow | cut -d " " -f2-
