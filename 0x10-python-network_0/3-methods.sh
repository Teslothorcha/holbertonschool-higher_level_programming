#!/bin/bash
# size
curl -sI "$1" | grep Allow | cut -b 8-25
