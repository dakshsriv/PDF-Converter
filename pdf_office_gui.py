#!/usr/bin/python3

# The following python code is the full program for this advanced PDF office!

import PySimpleGUI as sg
from pprint import pprint
from io import StringIO
from magic import from_file as findtype
from docx2pdf import convert

def detect_file_type(filename):
    a = findtype(filename)
    a = a.split()
    filetype = a[0]
    return filetype

def createPDF(filename):
    filetype = detect_file_type(filename)
    if filetype == "docx":
        convert(f"{filename}", "C:{filename}")

def Pdf_Office():
    Create_PDF_layout = [
        [sg.FilesBrowse()]
        ,
        [sg.Button("Create PDF", key="create pdf")],
        [sg.OK(), sg.Cancel()]
        ]
    while True:
        window = sg.Window('PDF Office', default_element_size=(400, 100)).Layout(Create_PDF_layout)
        event, values = window.Read()
        if event == "create PDF":
            filename = event[0]
            my_windows_size = window.Size
            print(filename)
            createPDF(filename)

print(Pdf_Office())

