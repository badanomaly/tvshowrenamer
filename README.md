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

Final Structure Of directories
TVShows/
	Show1/
		season 1/
			1x01 - episode title
			1x02 - episode title
		season 2/
			2x01 - episode title
			2x02 - episode title
	Show2/
		season 1/
			1x01
	Show3/
		season 3
This script converts the files of names
[720pMkv.Com]_doctor.who.2005.s02e04.480p.BluRay.x264-GAnGSteR.mkv
to
Doctor Who (2005)-02x04-The Girl in the Fireplace.mp4

For this script to work 
1. Edit the allShowDir variable to point to your TV Show Directory
2. Make Sure that the files have the format S01E03 or 01x03 (SxxExx or xxXxx) 
to recognise their season number and episode number values.

This script also stores a log file for all the renames in the directory
so that you can revert manually the renames that turn out to be wrong
