#!/usr/bin/python3

import requests, sys, subprocess, time
from datetime import datetime

iftttkey = "kw4Iuargdss0Sl5p-cXKB"
debugfile = "/var/lib/docker/volumes/generated_bitcoin_datadir/_data/debug.log"

tailcommand = "tail -1 " + debugfile + " | awk '{printf $5}'"
