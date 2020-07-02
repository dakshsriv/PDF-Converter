#!/usr/bin/python3

# The following python code is the full program for this advanced PDF office!

import PySimpleGUI as sg
import os
import sys
import subprocess

def findOutdir(filename):
    i = 0
    e = range(0, len(filename))
    for x in e:
        i = i - 1
        if filename[i] == "/":
            break
    i = i + 1
    outdir = filename[:i]
    return outdir


def Create_PDF(file_to_convert, output_directory):
    subprocess.Popen(["/usr/bin/soffice", 
        "--convert-to", 
        "pdf", 
        "--outdir", 
        output_directory, 
        file_to_convert,
        '--headless']
    )

def Pdf_Office():
    Create_PDF_layout = [
        [sg.FilesBrowse()]
        ,
        [sg.Button("Create PDF", key="create pdf")],
        [sg.OK(), sg.Cancel()]
        ]
    window = sg.Window('PDF Office', Create_PDF_layout)
    while True:
        event, values = window.Read()
        if event == "Exit" or event is None:
            break
        if event != sg.TIMEOUT_KEY:
            sg.Print(f"Event: {event}")
        if event == "create pdf":
            filename = values["Browse"]
            print(f"The filename is {filename}")
            Create_PDF(filename, findOutdir(filename))

print(Pdf_Office())