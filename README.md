tvshowrenamer
=============
This python script Edits the file names of 
a TV show directory to the format
Show Name-seasonNoXepisodeno-episodeTitle

The required directory structure for this script to work
TVShows/
	Show1/
		folder1/
		folder2/
			folder3/
				/file4
			file3
		file1
		file2
	Show2/
		folder1/
		file

This script converts the files of names
[720pMkv.Com]_doctor.who.2005.s02e04.480p.BluRay.x264-GAnGSteR.mkv
to
Doctor Who (2005)-02x04-The Girl in the Fireplace.mp4

For this script to work 
1. Edit the allShowDir variable to point to your TV Show Directory
2. Make Sure that the files have the format SxxExx or xxXxx 
to recognise their season number and episode number values.
