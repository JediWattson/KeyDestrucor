#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:25:10 2019

@author: jediwattson
"""

# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import googleapiclient.discovery
import cv2
from pytube import YouTube

# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"

'''
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY)


request = youtube.search().list(
    part="snippet",
    maxResults=25,
    q="super mario brothers 1985"
)

ids = []
response = request.execute()

for r in response["items"]:
    ids.append(r["id"]["videoId"])
'''
    
prepend = "https://www.youtube.com/watch?v="
 
yt = YouTube('https://www.youtube.com/watch?v=1FnPe6tinVs') #prepend + ids[0])
stream = yt.streams.filter(file_extension='webm').first()
print (stream.url)
stream.download()

'''
cap = cv2.VideoCapture('smb1.webm')

while (cap.isOpened()):
    ret,frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''
