#!/bin/bash

wayback_machine_downloader https://www.cheatography.com --only "/(latex)\/$/i" -c 4

wayback_machine_downloader https://www.cheatography.com --only "/(pdf)\/$/i" -c 4

wayback_machine_downloader http://www.cheatography.com --only "/\/cheat-sheets\/[a-z0-9\-_]+\/$/i" -c 4
