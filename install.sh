#!/bin/bash

SCRIPT="/usr/local/bin/pusheen-sl"

# check for root
if [ "$(id -u)" == "0" ]; then
    # check if uninstall option is being used
    if [ "$1" == "-u" ]; then
        # check if script is installed (checks if the file exist)
        if [ -f $SCRIPT ]; then
            rm $SCRIPT
            echo "$SCRIPT deleted successfully"
        else
            echo "pusheen-sl is not installed"
        fi
    else
        cp ./pusheen-sl.py $SCRIPT
    fi
else
    echo "Run this script as root to (un)install pusheen-sl"
    echo "ex: sudo $0 [-u]"
fi
