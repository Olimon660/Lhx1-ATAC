#!/bin/bash

cut -f3,6 $1 |tail -n +2 | head -n -4 | sed -e 's/\:/	/' | sed -e 's/-/	/'
