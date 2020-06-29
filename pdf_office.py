#!/usr/bin/python3

import argparse
import os
import sys
import subprocess

def Create_PDF(file_to_convert, output_directory):
    subprocess.Popen(["/usr/bin/soffice", 
        "--convert-to", 
        "pdf", 
        "--outdir", 
        output_directory, 
        file_to_convert,
        '--headless']
    )


if __name__ == "__main__":
        Create_PDF( sys.argv[1], '/home/daksh/Projects/PDF_Office')
    sys.exit(1)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-e",
        "--edit",
        type=str,
        default="",
        help="Enter beat settings. Example: 4,4,n,a,r,s,1,60 for 4, 4, Normal, Accent, Rest, Subaccent, 1 beat subdivision, 60 bpm respectively.",
    )
    parser.add_argument(
        "-edit",
        "--multiedit",
        type=str,
        default="",
        help="Enter multirhythm settings. Example: 4,5,60 for Ratio of 4 to 5 at 60 bpm.",
    )
    parser.add_argument("-p", "--play", help="Play?", action="store_true")
    parser.add_argument("-play", "--multiplay", help="Play?", action="store_true")
    args = parser.parse_args()
    if args.play:
        play_music()
    elif args.edit:
        store_settings(args)
    elif args.multiedit:
        store_multi(args)
    elif args.multiplay:
        multi_play()
