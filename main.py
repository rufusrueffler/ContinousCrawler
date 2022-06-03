# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 18:00:50 2020

@author: rufus
"""

import ImmoScout

from datetime import datetime, timedelta
from threading import Timer
day_t = 60*60*24
def trigger_event():
    urlList =['https://www.immobilienscout24.de/Suche/de/berlin/berlin/haus-kaufen?pagenumber=','https://www.immobilienscout24.de/Suche/de/baden-wuerttemberg/boeblingen-kreis/haus-kaufen?pagenumber=']
    ImmoScout.getImmoscoutData(urlList)
    day_t = 60*60*24
    t = Timer(day_t , trigger_event)
    t.start()

trigger_event()