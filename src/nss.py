#! /usr/bin/env python
"""
Author: Robert Owens
Date: 06/17/2022
License: MIT
"""

import json
import modules.general as mg
from colorama import Fore, Style
import pathlib
import netmiko as nm
ROOTPATH = pathlib.Path(__file__).parent.resolve()
MODULESPATH = str(ROOTPATH) + "\Modules"
TARGET = "myTargetHost"
username = "myUsername"
password = "myPassword"

# Intake STIG JSON file
with open(f"{ROOTPATH}/stigData.json") as file:
    data = json.load(file)

stig = data["stig"]
findings = stig["findings"]
stigReleaseDate = stig["date"]
stigTitle = stig["title"]

print(f"{Fore.CYAN}Currently Running Stig:{Fore.BLUE} {stigTitle}")
print(f"{Fore.CYAN}Released:{Fore.MAGENTA} {stigReleaseDate}{Style.RESET_ALL}\n")

# TODO Establish ssh connection
# connection = nm.ConnectHandler(ip=TARGET, device_type="cisco_ios", username=username, password=password)

# * Output vuln currently being checked
for i in range(len(findings)):
    for finding in findings:
        title = findings[finding]["title"]
        vulnId = findings[finding]["id"]
        severity = findings[finding]["severity"]
        description = (
            findings[finding]["description"]
            .replace("\n\n", "")
            .replace("\n", "")
            .replace("  ", " ")
        )  # Cleaning up output

        if i == 0:
            print(mg.display_stig(title, vulnId, mg.classify_color(severity), description))

# ! Testing Purposes (Remove later)
# testJson = json.dumps(findings, indent=4)
# print(testJson)
