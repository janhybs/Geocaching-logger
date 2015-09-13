#!/usr/bin/env python
# -*- coding: utf8 -*-

import creds

__author__ = 'x3mSpeedy'
import urllib2
import urllib
import webbrowser
from mechanize import *
import sys
from bs4 import BeautifulSoup, NavigableString
import json

from encodings import hex_codec

class Geo(object):
    br = Browser()
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; \
          rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    br.set_handle_robots(False)

    def login(self, username, password):
        self.br.open('https://www.geocaching.com/login/default.aspx')
        self.br.select_form(name="aspnetForm")

        self.br["ctl00$ContentBody$tbUsername"] = username
        self.br["ctl00$ContentBody$tbPassword"] = password
        response = self.br.submit()
        html = response.read()

        if html.find(username) != -1:
            return html

        return None

    def log_cache(self, url, message, date_visited, tb=True):
        self.br.open(url)
        self.br.follow_link(text_regex="Log your visit")

        self.br.select_form(name="aspnetForm")
        self.br.form.set_all_readonly(False)
        self.br["ctl00$ContentBody$LogBookPanel1$ddLogType"] = ["2", ]
        self.br["ctl00$ContentBody$LogBookPanel1$uxDateVisited"] = date_visited
        self.br["ctl00$ContentBody$LogBookPanel1$uxLogInfo"] = message

        if tb:
            self.br["ctl00$ContentBody$LogBookPanel1$uxTrackables$hdnSelectedActions"] = "4996238_Visited,"
            # self.br["ctl00$ContentBody$LogBookPanel1$uxTrackables$repTravelBugs$ctl02$ddlAction"] = [
            #     '4996238_Visited', ]

        response = self.br.submit()
        html = response.read()
        return html


if __name__ == "__main__":
    urls = [
        "http://www.geocaching.com/geocache/GC23E1A_milnik-milestone",
        "http://www.geocaching.com/geocache/GC3TGXA_cisarska-alej",
        "http://www.geocaching.com/geocache/GC2W5EW_rychlostnice-praha-liberec-night-edition",
        "http://www.geocaching.com/geocache/GC1T9W2_skakal-pes-pres-oves",
        "http://www.geocaching.com/geocache/GC573AC_walking-trail-1",
        "http://www.geocaching.com/geocache/GC3QA3R_slunce-seno-a-par-facek",
        "http://www.geocaching.com/geocache/GC573AD_walking-trail-2",
        "http://www.geocaching.com/geocache/GC573AJ_walking-trail-3",
        "http://www.geocaching.com/geocache/GC573AR_walking-trail-4-dobrodruzstvi-pavouka-stestika",
        "http://www.geocaching.com/geocache/GC573AW_walking-trail-5-liska-bystrouska",
        "http://www.geocaching.com/geocache/GC573B0_walking-trail-6-slepice-domaci",
        "http://www.geocaching.com/geocache/GC573B9_walking-trail-7-skokan-hndy",
        "http://www.geocaching.com/geocache/GC573BE_walking-trail-8-u-krtka",
        "http://www.geocaching.com/geocache/GC573BP_walking-trail-9-parezova-chaloupka",
        "http://www.geocaching.com/geocache/GC573BZ_walking-trail-10-pod-jezevci-skalou",
        "http://www.geocaching.com/geocache/GC573C4_walking-trail-11-vres-obecny",
        "http://www.geocaching.com/geocache/GC573CA_walking-trail-12-kachna-obecna",
        "http://www.geocaching.com/geocache/GC3VYK4_zapomenute-jezirko-2",
        "http://www.geocaching.com/geocache/GC573CF_walking-trail-13",
        "http://www.geocaching.com/geocache/GC3VP9J_zapomenute-jezirko",
        "http://www.geocaching.com/geocache/GC573CK_walking-trail-14-sycek-obecny",
        "http://www.geocaching.com/geocache/GC573CX_walking-trail-15-jezek-vychodni",
        "http://www.geocaching.com/geocache/GC573D1_walking-trail-16",
        "http://www.geocaching.com/geocache/GC573D5_walking-trail-17",
        "http://www.geocaching.com/geocache/GC573D8_walking-trail-18",
        "http://www.geocaching.com/geocache/GC2HZN7_tajemstvi-archivu-dr-watsona",
        "http://www.geocaching.com/geocache/GC573DG_walking-trail-19",
        "http://www.geocaching.com/geocache/GC573DV_walking-trail-20-mravenec-lesni",
        "http://www.geocaching.com/geocache/GC58CYD_strycek-skrblik-bonus",
        "http://www.geocaching.com/geocache/GC587KT_kacer-uu",
        # "http://www.geocaching.com/geocache/GC58AD1_kaceri-pribehy"
    ]
    urls.reverse()
    message = "Bezvadný výlet s partou pohodových geokačerů. Přálo nám počasí a udělali jsme 32 kousků. Při cestě nechyběla legrace ani nadšení. Díky moc za kešku!"
    g = Geo()
    print 'login'
    g.login(creds.username, creds.password)

    for link in urls:
        print 'logging: ' + link
        g.log_cache(url=link, message=message, date_visited="03.May.2015")