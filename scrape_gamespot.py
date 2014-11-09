#!/usr/bin/env python
# Aaron Meisner, 11/8/2014

import requests
from pattern import web
import json
import time

def scrape_one_page(pagenum, jsondata):

    url = 'http://www.gamespot.com/reviews/?page='+str(pagenum)
    html = requests.get(url).text

    dom = web.Element(html)

    articles = dom.by_tag("article")

    for art in articles:
        if art.attr['class'] == 'media media-review':
            review_summary = art.by_tag('p')
            review_score = art.by_tag('strong')
            review_time = art.by_tag('time')
            summary = review_summary[0].content
            score = review_score[0].content
            datetime = review_time[0].attr['datetime']
            gamedata = {'summary' : summary, 
                        'score' : score,
                        'datetime' : datetime}
            jsondata.append(gamedata)
    return jsondata

def scrape_many_pages(pstart, npages, delay=10.):
    jsondata = []
    for pagenum in range(pstart, pstart+npages):
        print "Working on page ", pagenum
        jsondata = scrape_one_page(pagenum, jsondata)
        print "Waiting..."
        # avoid thrashing GameSpot servers
        time.sleep(delay)

    # write out the json data accumulated
    with open('gamespot.json', 'w') as outfile:
        json.dump(jsondata, outfile)

if __name__=='__main__':
    # as of 11/8/2014, there were 653 pages of reviews available from GameSpot
    npages = 653
    scrape_many_pages(1, npages)
