from models import *
from django.shortcuts import *
from django.db.models import *
import feedparser
import requests
from bs4 import BeautifulSoup

# World-Herald Live home page
def Main(request):
    shows = Show.objects.all()
	
    dictionaries = { 'shows': shows, }
    return render_to_response('whlive/main.html', dictionaries)

# javascript player on omaha.com/bottomline
def TBLsegments(request):
    segments = Segment.objects.all().order_by('-date')[:30]
    feed = feedparser.parse('http://owh.backbonebroadcast.com/owh_mp3/tbl_podcast_alt.xml')
    new_segments = feed.entries
      
    dictionaries = { 'segments': segments, 'new_segments': new_segments, }
    return render_to_response('whlive/tbl-segments.html', dictionaries)
	
	
def TBLsegmentsBackbone(request):
    d = feedparser.parse('http://66.135.50.41/owh_mp3/tbl_podcast.xml')

    dictionaries = { 'd': d, }
    return render_to_response('whlive/tbl-segments-backbone.html', dictionaries)	
	
# TuneIn feed, Dataomaha Segments app XML, Segments app not updated after 16-Feb-2015
def TBLfeed(request):
    segments = Segment.objects.all().order_by('-date')[:30]
    pubdate = segments[0]

    dictionaries = { 'segments': segments, 'pubdate': pubdate, }
    return render_to_response('whlive/tbl-rss.xml', dictionaries)

# New TuneIn feed with Backbone XML
def TBLfeed2(request):
    feed = feedparser.parse('http://owh.backbonebroadcast.com/owh_mp3/tbl_podcast.xml')
    new_segments = feed.entries[:40]
    pubdate = new_segments[0].published

    dictionaries = { 'new_segments': new_segments, 'pubdate': pubdate, 'feed': feed, }
    return render_to_response('whlive/tbl-rss-backbone-feed.xml', dictionaries)
	
# ????
def TBLfeedAirkast(request):
    segments = Segment.objects.all().order_by('-date')[:30]
 
    dictionaries = { 'segments': segments, }
    return render_to_response('whlive/tbl-rss-airkast.xml', dictionaries)

	
# used to embed schedule on Blox version of omaha.com/bottomline
def TBLguests(request):
    guests = Schedule.objects.get(show__name="The Bottom Line")
	
    dictionaries = { 'guests': guests, }
    return render_to_response('whlive/tbl-guests.html', dictionaries)

	
def SingleSegment(request, segment):
    segment = Segment.objects.get(id=segment)

    dictionaries = { 'segment': segment }
    return render_to_response('whlive/segment.html', dictionaries)

	
def SingleSchedule(request, schedule):
    schedules = Schedule.objects.get(id=schedule)

    dictionaries = { 'schedule': schedule }
    return render_to_response('whlive/schedule.html', dictionaries)	

# testing
def Backbone(request):
    d = feedparser.parse('http://66.135.50.41/owh_mp3/tbl_podcast.xml')
    
    dictionaries = { 'd': d, }
    return render_to_response('whlive/backbone.html', dictionaries)

def TBLmain(request):
    feed = feedparser.parse('http://owh.backbonebroadcast.com/owh_mp3/tbl_podcast_alt.xml')
    guests = Schedule.objects.get(show__name="The Bottom Line")
    new_segments = feed.entries[:20]
    url = "http://feeds.newsinc.com/feeds/playlist?format=rss&encoding=utf16&adnetid=91341&sitesection=omahawh&apikey=aAzQWSqIsEPisXEKnlfQog%3D%3D"
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    ls = []
    videos = soup("item")[:10]
    for video in videos:
        ls.append([video.title.text, video.description.text, video.image.text, video.landingpageurl.text ])
    
    dictionaries = {'new_segments': new_segments, 'videos': videos, 'guests': guests, 'ls':ls, }
    return render_to_response('whlive/tbl-main.html', dictionaries)

def Stream(request):

    dictionaries = { }
    return render_to_response('whlive/tbl-stream.html', dictionaries)

    
def Suzanna(request):
    feed = feedparser.parse('http://owh.backbonebroadcast.com/owh_mp3/suzanna.xml')
    segments = feed.entries[:15]

    dictionaries = { 'segments': segments, }
    return render_to_response('whlive/suzanna.html', dictionaries)

def SuzannaFeed(request):	
    feed = feedparser.parse('http://owh.backbonebroadcast.com/owh_mp3/suzanna.xml')
    new_segments = feed.entries[:40]
    pubdate = new_segments[0].published

    dictionaries = { 'feed': feed, 'new_segments': new_segments, 'pubdate': pubdate, }
    return render_to_response('whlive/suzanna-podcast-feed.xml', dictionaries)

#automated feed, using Segments from dataomaha admin, 29 May 2015 / Vankat / Created for Pick Six	
def PickSixFeed(request):	
    segments = Segment.objects.filter(show__nameslug="pick-six").order_by('-date')[:30]
    pubdate = segments[0]

    dictionaries = { 'segments': segments, 'pubdate': pubdate, }
    return render_to_response('whlive/pick-six-feed.xml', dictionaries)
