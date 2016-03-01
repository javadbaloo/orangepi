import urllib2
import sys
 
key = "AIzaSyDNEUKPEp8jErUyFMkr5vmiJes7ZeQBUZs"
url = "https://www.google.com/speech-api/v2/recognize?output=json&lang=ru-ru&key="+key
try:
   filename = sys.argv[1]
except IndexError:
    print 'Usage: democode.py <file>'
    sys.exit(1)
 
audio = open(filename,'rb').read()
 
headers={'Content-Type': 'audio/x-flac; rate=44100'}
 
request = urllib2.Request(url, data=audio, headers=headers)
response = urllib2.urlopen(request)
print response.read()
