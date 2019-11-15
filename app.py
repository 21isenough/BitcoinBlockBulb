#!/usr/bin/python3

import requests, sys, subprocess, time
from datetime import datetime

iftttkey = "kw4Iuargdss0Sl5p-cXKB"
debugfile = "/var/lib/docker/volumes/generated_bitcoin_datadir/_data/debug.log"

tailcommand = "tail -1 " + debugfile + " | awk '{printf $5}'"


def main():
    block = subprocess.check_output(tailcommand, shell=True).decode("utf-8")
    block = block[7:]
    while True:

        blocknow = subprocess.check_output(tailcommand, shell=True).decode("utf-8")

        if "height" in blocknow:
            blocknow = blocknow[7:]

            if (int(block) + 1) == int(blocknow):
                now = datetime.now()
                date = now.strftime("%d.%m.%Y %H:%M:%S")
                block = blocknow
                print(block + " - New Block! (" + str(date) + ")")
                lampcommand("new_block")
                time.sleep(2)
                lampcommand("turn_off")

        time.sleep(1)


def lampcommand(command):
    requests.post(
        "https://maker.ifttt.com/trigger/" + command + "/with/key/" + iftttkey
    )
