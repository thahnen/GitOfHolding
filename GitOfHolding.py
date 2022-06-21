#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
GitOfHolding:
============

Creates a backup of the savegames from the games specified down below (see "mapping").
The currently supported games are:
- Baldur's Gate: Enhanced Edition
- Baldur's Gate II: Enhanced Edition
- Icewind Dale: Enhanced Edition
"""

import os
import pathlib
import shutil


# Constants to user profile and the actual data directory
HOME: str = os.environ["USERPROFILE"]
DATA: str = os.path.normpath(os.path.join(pathlib.Path(__file__).parent.resolve(), "data"))

# Mapping of game to savegame folder
KEY_TITLE = "title"
KEY_SAVEGAMES = "savegames"

mapping: list[dict[str, str]] = [
    {
        KEY_TITLE:      "Baldur's Gate: Enhanced Edition",
        KEY_SAVEGAMES:  os.path.normpath(
            os.path.join(HOME, "Documents\\Baldur's Gate - Enhanced Edition\\save")
        )
    },
    {
        KEY_TITLE:      "Baldur's Gate II: Enhanced Edition",
        KEY_SAVEGAMES:  os.path.normpath(
            os.path.join(HOME, "Documents\\Baldur's Gate II - Enhanced Edition\\save")
        )
    },
    {
        KEY_TITLE:      "Icewind Dale: Enhanced Edition",
        KEY_SAVEGAMES:  os.path.normpath(
            os.path.join(HOME, "Documents\\Icewind Dale - Enhanced Edition\\save")
        )
    }
]


"""
Main method called when script / executable is running
"""
if __name__ == "__main__":
    for game in mapping:
        if not os.path.exists(game[KEY_SAVEGAMES]):
            print(f"{game[KEY_TITLE]} -> no savegames available, maybe game not installed!")
            continue

        print(f"{game[KEY_TITLE]} -> savegames found, therefore backuping them!")

        saved_files: str = os.path.join(
            DATA, game[KEY_TITLE].replace("'", "").replace(":", "").replace(" ", "-")
        )
        if os.path.exists(saved_files):
            shutil.rmtree(saved_files)
        else:
            os.mkdir(saved_files)
        
        for element in os.listdir(game[KEY_SAVEGAMES]):
            element_path = os.path.join(game[KEY_SAVEGAMES], element)
            if (os.path.isdir(element_path)):
                shutil.copytree(element_path, os.path.join(saved_files, element))
            else:
                shutil.copy(element_path, os.path.join(saved_files, element))
        
        print(f"{game[KEY_TITLE]} -> savegames fully backuped!")
