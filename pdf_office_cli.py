#!/usr/bin/python3

import argparse
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

def Export_to_xlsx(file_to_convert, output_directory):
    subprocess.Popen(["/usr/bin/soffice", 
        "--convert-to", 
        "xlsx", 
        "--outdir", 
        output_directory, 
        file_to_convert,
        '--headless']
    )

def Export_to_doc(file_to_convert, output_directory):
    subprocess.Popen(["/usr/bin/soffice", 
        "--convert-to", 
        "doc", 
        "--outdir", 
        output_directory, 
        file_to_convert,
        '--headless']
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--createPDF",
        "--createPDF",
        type=str,
        default="",
        help="Create a PDF from countless file types. Usage python3 --createPDF /home/user/Documents/random_file.xlsx",
    )
    args = parser.parse_args()
    if args.createPDF:
        Create_PDF( args.createPDF, findOutdir(args.createPDF))
    sys.exit(1)
