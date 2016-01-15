from django.conf.urls import *

urlpatterns = patterns('',
    (r'^/schedule/(?P<schedule>[a-zA-Z0-9_.-]+)$', 'myproject.whlive.views.SingleSchedule'), 
    (r'^/segment/(?P<segment>[0-9_.-]+)$', 'myproject.whlive.views.SingleSegment'),
    (r'^/TBL/segments2', 'myproject.whlive.views.TBLsegmentsBackbone'),
    (r'^/TBL/segments', 'myproject.whlive.views.TBLsegments'), # javascript player on omaha.com/bottomline
    (r'^/TBL/stream', 'myproject.whlive.views.Stream'), # Live stream iframe. Using rtmp feed from Mike Flood's group
    (r'^/TBL/guests', 'myproject.whlive.views.TBLguests'), # used to embed schedule on Blox version of omaha.com/bottomline
    (r'^/TBL/feed2', 'myproject.whlive.views.TBLfeed'), # TuneIn feed, Dataomaha Segments app XML, Segments app not updated after 16-Feb-2015
    (r'^/TBL/feed', 'myproject.whlive.views.TBLfeed2'), # New TuneIn feed with Backbone XML
    (r'^/TBL/airkast', 'myproject.whlive.views.TBLfeedAirkast'), # ????
    (r'^/TBL/backbone', 'myproject.whlive.views.Backbone'), # testing
    (r'^/TBL', 'myproject.whlive.views.TBLmain'), # TBL home page
    (r'^/tbl', 'myproject.whlive.views.TBLmain'), # TBL home page
    (r'^/bottomline', 'myproject.whlive.views.TBLmain'), # TBL home page
    (r'^/suzanna/feed', 'myproject.whlive.views.SuzannaFeed'), #Suzanna feed for iTunes
    (r'^/suzanna', 'myproject.whlive.views.Suzanna'), #Suzanna home page
    (r'^/pick-six/feed$', 'myproject.whlive.views.PickSixFeed'), #Added 29 May 2015 / vankat
    (r'^', 'myproject.whlive.views.Main') # potential for use as WHLive home page
)
