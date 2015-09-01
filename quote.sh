#!/bin/bash
# A launcher script to run quote.py. Attempts to run it again if the
# first try is unsuccessful.
# usage:
# ./quote.sh
#    generetate a quote to stdout
# ./quote.sh --bot quote
#    tweets a quote

python ./quote.py $1 $2
date +"%d.%m.%Y-%H:%M"

ret=$?
if [ $ret -ne 0 ]; then
  echo "Not a valid quote, trying again..."
  python ./quote.py $1 $2
fi
