# Youtube_Download_Extension
This is a python script to download any YouTube Videos with additional function

Tested Environment:
RaspberryPi Google AIY Kit

$cat /etc/debian_version
>10.13

$python3 -V
>Python 3.7.3

$youtube-dl --version
>2021.12.17

You also need set up 2 directories with name Audios and Videos to obtain the downloaded .mp4 and .mp3 files.
Be careful of your disk size.

This wcript works on Youtube_DL base.
and it can download single video or videos list with specified format for .mp3 and .mp4 at same time.

Oops! sometimes if the video have no specified format, it will get error to skip the download.
No problem, I am working on it to improve it anyway.

Very simple!
1. set the video or videos list URL in your [YoutubeURLList.txt].
2. Run [downloadYoutube_SUB.py].

I tried to add sub for it, but it didnot work yet, anyway, the name keep as what it should be.

It will be pleasure if this can help you with some new idea.
