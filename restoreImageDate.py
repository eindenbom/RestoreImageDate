#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
from datetime import datetime
from os import utime, stat

import piexif

SectionExif = 'Exif'
TagExifDateTimeOriginal = 0x9003
# noinspection SpellCheckingInspection
ExifDateTimeFormat = '%Y:%m:%d %H:%M:%S'


def restoreImageDate( fileName ):
    # Loading exif information
    exif = piexif.load( fileName )
    # DateTimeOriginal as ASCII string
    dateTimeStr = str( exif[SectionExif][TagExifDateTimeOriginal], encoding = 'ASCII' )
    # date & time in current time zone
    d = datetime.strptime( dateTimeStr, ExifDateTimeFormat )
    # access and modification time
    utime( fileName, times = (datetime.now().timestamp(), d.timestamp()) )


if __name__ == '__main__':
    parser = argparse.ArgumentParser( description = 'restore image modification time from EXIF data' )
    parser.add_argument( 'files', nargs = argparse.REMAINDER, help = 'files to restore modification time' )
    cmdArgs = parser.parse_args()

    for fn in cmdArgs.files:
        restoreImageDate( fn )
