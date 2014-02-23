import urllib.request
from urllib.error import URLError, HTTPError
import xml.etree.ElementTree as ET
import os
import re

def openResource(link):
	req = urllib.request.Request(link)
	try:
		response = urllib.request.urlopen(req)
	except HTTPError as e:
	    print('The server couldn\'t fulfill the request.')
	    print('Error code: ', e.code)
	except URLError as e:
	    print('We failed to reach a server.')
	    print('Reason: ', e.reason)
	else:
		content = response.read()
		return content.decode('utf-8')
def findShowId(showName):
	urlShowName = showName.strip().replace(' ','%20')
	linkUrl = "http://services.tvrage.com/feeds/search.php?show="+urlShowName
	xml = openResource(linkUrl)
	root = ET.fromstring(xml)
	for show in root.findall('show'):
		showname = show.find('name').text
		showid = show.find('showid').text
		started = show.find('started').text
		country = show.find('country').text
		print("Name: ",showname,"\nStarted:",started,'country:',country)
		choice = input("Is this the correct match to your show '"+showName+"'?(Y/N) "+': ')
		if choice == 'y' or choice == 'Y':
			return showid
	return -1
def seasonEpisode(fileName):
	result = re.search('.*([sS]{1}([0-9]+)[eE]{1}([0-9]+)).*',fileName);
	if result:
		found = result.group(1)
		ret = []
		ret.append(int(result.group(2)))
		ret.append(int(result.group(3)))
		return ret
	result = re.search('.*(([0-9]+)[xX]{1}([0-9]+)).*',fileName);
	if result:
		found = result.group(1)
		ret = []
		ret.append(result.group(2))
		ret.append(result.group(3))
		return ret
	return -2

def newName(showid,season,episode):
	epInfoUrl = "http://services.tvrage.com/feeds/episodeinfo.php?"
	epInfoUrl = epInfoUrl+"sid="+str(showid)
	epInfoUrl = epInfoUrl+"&ep="+str(season)+"x"+str(episode)
	xml = openResource(epInfoUrl)
	root = ET.fromstring(xml)
	ret = root.find('name').text
	if len(root.findall('episode')) == 1:
		for episode in root.findall('episode'):
			ret = ret + "-" + episode.find('number').text
			ret = ret + '-' + episode.find('title').text
		return ret
	return -3
if __name__ == '__main__':        
	allShowsDir = ""
	#Edit this variable to point to you Tv shows Directory
	showNameList = [x for x in os.listdir(allShowsDir)]
	for show in showNameList:
		showDir = allShowsDir+'/'+ show
		showid = findShowId(show)
		if showid == -1:
			print("Sorry We couldn't find any matches for the folder '"+show+"'")
			continue
		for root,dirs,files in os.walk(showDir):
			for fyle in files:
				temp = seasonEpisode(fyle)
				if temp == -2:
					print("file: "+fyle+' in show: '+show+" doesn't seem to match to any episode")
					print("Please check its name contains format SxxExx or xxXxx format")
					continue
				print("Old Name:"+fyle)
				newFyle = newName(showid,temp[0],temp[1])
				if newFyle == -3:
					print("Sorry Couldn't file the correct episode for show: "+show+' file: '+fyle)
					continue
				newFyle = newFyle + "." + fyle.split('.')[-1]
				print("New Name:"+newFyle)
