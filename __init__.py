from playsound import playsound
from pathlib import Path

import glob, os, keyboard
import sys

def __init__():
    folder_path = "{}\\{}".format(Path().absolute(), "notes")
    os.chdir(folder_path)

    all_notes = glob.glob("*.mp3")

    print("---------------------------")
    print("The notes available are:   ")
    print("---------------------------")

    for counter in range(lens(all_notes)):
        print("{} - {}".format(counter, all_notes[counter]))

    print("\n-1 - Cancel")
    print("\nType something...")

    while True:
        input = sys.stdin.readline().split()[0]

        if input == "-1":
            sys.exit()
        else:   
            try:
                note = all_notes[int(input)]
                playsound(note)
            except:
                print("-----\nThis note does not exists! \nPlease, try again. \n-----")

__init__()