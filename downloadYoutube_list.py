#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals
import os
import glob
import youtube_dl

URLFILE = "YoutubeURLList.txt"

"""
f = open(URLFILE, "r")
print(f.readline())
f.close()
"""

# consts
VIDEO_DIR = "/home/pi/Videos" 
MP3_DIR = "/home/pi/Audios"
OPTS = {
    "format": "136+140",
    "outtmpl": "{VIDEO_DIR}/%(title)s.mp4".format(VIDEO_DIR=VIDEO_DIR)
}
OPTS_MP3 = {
    "format": "bestaudio/best",
    "outtmpl": "{MP3_DIR}/%(title)s.m4a".format(MP3_DIR=MP3_DIR),
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
        }]
}

def download(url):
    """
    Download video from YouTube.

    Parameters

    ----------
    url : str
        YouTube video URL

    Returns
    ----------
    info : dict
        Downloaded video info.
    """
    print("Downloading {url} MP4 start..".format(url=url))
    with youtube_dl.YoutubeDL(OPTS) as y:
        info = y.extract_info(url, download=True)
        print("Downloading {url} MP4 finish!".format(url=url))
    return info

def downloadmp3(url):
    print("Downloading {url} MP3 start..".format(url=url))
    with youtube_dl.YoutubeDL(OPTS_MP3) as z:
        info_mp3 = z.extract_info(url, download=True)
        print("Downloading {url} MP3 finish!".format(url=url))
    return info_mp3

def rename(info):
    """
    Rename downloaded video filename as camelcase.

    Parameters
    ----------
    info : dict
        Downloaded video info.
    """
    title = info["title"]
    pattern = '{VIDEO_DIR}/{title}.mp4'.format(VIDEO_DIR=VIDEO_DIR, title=title)
   # for v in glob.glob(pattern, recursive=True):
    for v in glob.glob(pattern):
        print("{title}.mp4 found! Renaming MP4 start..".format(title=title))
        file_path = os.path.join(VIDEO_DIR, v)
        new_file_path = file_path.replace(' ', '_')
        os.rename(file_path, new_file_path)
        print("Renaming MP4 finish!".format(title))

def renamemp3(info_mp3):
    """
    Rename downloaded video filename as camelcase.

    Parameters
    ----------
    info : dict
        Downloaded video info.
    """
    title = info_mp3["title"]
    pattern = '{MP3_DIR}/{title}.mp3'.format(MP3_DIR=MP3_DIR, title=title)
   # for v in glob.glob(pattern, recursive=True):
    for v in glob.glob(pattern):
        print("{title}.mp3 found! Renaming MP3 start..".format(title=title))
        file_path = os.path.join(MP3_DIR, v)
        new_file_path = file_path.replace(' ', '_')
        os.rename(file_path, new_file_path)
        print("Renaming MP3 finish!".format(title))

if __name__ == "__main__":
#    url = raw_input(">> ")
#    info = download(url)
#    rename(info)
#    info_mp3 = downloadmp3(url)
#    renamemp3(info_mp3)

    rowNumber = 0
    fileobj = open(URLFILE, "r")
    #fileobj = open(URLFILE, "r", encoding="utf_8")
    while True:
       url = fileobj.readline()
       if url:
           try:
               info = download(url)
               rename(info)
               info_mp3 = downloadmp3(url)
               try:
                   renamemp3(info_mp3)
               except:
                   print("Error is in MP3")
                   pass
               while True: time.sleep(100)
           except (KeyboardInterrupt, SystemExit):
               print('\n !Received keyboard interrupt, quitting threads.\n')
           except Exception as err:
               print("Unknown issue")
               print('Unexpected {err=}, {type(err)=}')
           else:
               print(rowNumber, ":", url, " download completed.")
           finally: 
               rowNumber += 1
               print(rowNumber, ":", url)
       else:
           break
