# !/bin/bash

run
wget --limit-rate=200k --no-clobber --convert-links --random-wait -p -E -e robots=off -U mozilla [domain]
done
