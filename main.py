__author__ = 'x3mSpeedy'
import urllib2
import urllib
import webbrowser
from mechanize import *
import sys
from bs4 import BeautifulSoup, NavigableString


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
            self.br[
                "ctl00$ContentBody$LogBookPanel1$uxTrackables$hdnSelectedActions"] = "2045329_Visited,4996238_Visited,"
            self.br["ctl00$ContentBody$LogBookPanel1$uxTrackables$repTravelBugs$ctl01$ddlAction"] = [
                '2045329_Visited', ]
            self.br["ctl00$ContentBody$LogBookPanel1$uxTrackables$repTravelBugs$ctl02$ddlAction"] = [
                '4996238_Visited', ]

        response = self.br.submit()
        html = response.read()
        return html


if __name__ == "__main__":
    urls = ['http://www.geocaching.com/geocache/GC4XHWT_dum-cesko-nemeckeho-porozumeni', 'http://www.geocaching.com/geocache/GC2KM4G_spoutana-nisa', 'http://www.geocaching.com/geocache/GC26DB4_areal-volnocasovych-aktivit-celakovskeho', 'http://www.geocaching.com/geocache/GC573ZY_izs-v-lk-stanice-hzs-jablonec-nad-nisou', 'http://www.geocaching.com/geocache/GC5HZJZ_pan-vajicko', 'http://www.geocaching.com/geocache/GC2N9PN_oko-bere', 'http://www.geocaching.com/geocache/GC1E0WP_hori', 'http://www.geocaching.com/geocache/GC1MY27_javor-ve-msene', 'http://www.geocaching.com/geocache/GC54KK9_sidliste-s-barvami-duhy', 'http://www.geocaching.com/geocache/GC2W50Q_pepicek-jde-do-skolky', 'http://www.geocaching.com/geocache/GC5BRV7_bobik', 'http://www.geocaching.com/geocache/GC4PYM3_kostel-nejsvetejsi-trojice', 'http://www.geocaching.com/geocache/GC4P2RZ_budka-pro-roryse', 'http://www.geocaching.com/geocache/GC2JCZF_draci-pribeh-i-evropska-legenda', 'http://www.geocaching.com/geocache/GC2M9AP_modra-je-dobra', 'http://www.geocaching.com/geocache/GC4ET7A_mseno-nad-nisou', 'http://www.geocaching.com/geocache/GC5GG9K_0-5-l-vody', 'http://www.geocaching.com/geocache/GC1DVEF_magicky-strom-magic-tree', 'http://www.geocaching.com/geocache/GC4PMVW_nefnukej-veverko', 'http://www.geocaching.com/geocache/GC2E3DR_paternity-2', 'http://www.geocaching.com/geocache/GC19GYE_prehradni-zahada', 'http://www.geocaching.com/geocache/GC2QK1P_tajvan', 'http://www.geocaching.com/geocache/GC2KN3R_singltrek', 'http://www.geocaching.com/geocache/GC1C8BP_haskovy-vily', 'http://www.geocaching.com/geocache/GC4FVQY_filmova', 'http://www.geocaching.com/geocache/GC1MF58_the-sculptures-of-jablonec-nad-nisou', 'http://www.geocaching.com/geocache/GC47J74_aprilek', 'http://www.geocaching.com/geocache/GC1KY0N_ceska-mincovna-the-czech-mint', 'http://www.geocaching.com/geocache/GCZYRN_prehrada-mseno-mseno-dam', 'http://www.geocaching.com/geocache/GC5JJZG_slunecni-hodiny', 'http://www.geocaching.com/geocache/GC2P455_rychla-smrt', 'http://www.geocaching.com/geocache/GC4EBY7_schody-do-pekla', 'http://www.geocaching.com/geocache/GC1P7NT_jizdarna-hippodrome', 'http://www.geocaching.com/geocache/GC2XG8M_lesni-tramvaj-ii-waldbim-ii']
    urls = ['http://www.geocaching.com/geocache/GC4XHWT_dum-cesko-nemeckeho-porozumeni']
    """[
    "http://www.geocaching.com/geocache/GC2XG8M_lesni-tramvaj-ii-waldbim-ii",
    "http://www.geocaching.com/geocache/GC1P7NT_jizdarna-hippodrome",
    "http://www.geocaching.com/geocache/GC4EBY7_schody-do-pekla",
    "http://www.geocaching.com/geocache/GC2P455_rychla-smrt",
    "http://www.geocaching.com/geocache/GC5JJZG_slunecni-hodiny",
    "http://www.geocaching.com/geocache/GCZYRN_prehrada-mseno-mseno-dam",
    "http://www.geocaching.com/geocache/GC1KY0N_ceska-mincovna-the-czech-mint",
    "http://www.geocaching.com/geocache/GC47J74_aprilek",
    "http://www.geocaching.com/geocache/GC1MF58_the-sculptures-of-jablonec-nad-nisou",
    "http://www.geocaching.com/geocache/GC4FVQY_filmova",
    "http://www.geocaching.com/geocache/GC1C8BP_haskovy-vily",
    "http://www.geocaching.com/geocache/GC2KN3R_singltrek",
    "http://www.geocaching.com/geocache/GC2QK1P_tajvan",
    "http://www.geocaching.com/geocache/GC19GYE_prehradni-zahada",
    "http://www.geocaching.com/geocache/GC2E3DR_paternity-2",
    "http://www.geocaching.com/geocache/GC4PMVW_nefnukej-veverko",
    "http://www.geocaching.com/geocache/GC1DVEF_magicky-strom-magic-tree",
    "http://www.geocaching.com/geocache/GC5GG9K_0-5-l-vody",
    "http://www.geocaching.com/geocache/GC4ET7A_mseno-nad-nisou",
    "http://www.geocaching.com/geocache/GC2M9AP_modra-je-dobra",
    "http://www.geocaching.com/geocache/GC2JCZF_draci-pribeh-i-evropska-legenda",
    "http://www.geocaching.com/geocache/GC4P2RZ_budka-pro-roryse",
    "http://www.geocaching.com/geocache/GC4PYM3_kostel-nejsvetejsi-trojice",
    "http://www.geocaching.com/geocache/GC5BRV7_bobik",
    "http://www.geocaching.com/geocache/GC2W50Q_pepicek-jde-do-skolky",
    "http://www.geocaching.com/geocache/GC54KK9_sidliste-s-barvami-duhy",
    "http://www.geocaching.com/geocache/GC1MY27_javor-ve-msene",
    "http://www.geocaching.com/geocache/GC1E0WP_hori",
    "http://www.geocaching.com/geocache/GC2N9PN_oko-bere",
    "http://www.geocaching.com/geocache/GC5HZJZ_pan-vajicko",
    "http://www.geocaching.com/geocache/GC573ZY_izs-v-lk-stanice-hzs-jablonec-nad-nisou",
    "http://www.geocaching.com/geocache/GC26DB4_areal-volnocasovych-aktivit-celakovskeho",
    "http://www.geocaching.com/geocache/GC2KM4G_spoutana-nisa",
    "http://www.geocaching.com/geocache/GC4XHWT_dum-cesko-nemeckeho-porozumeni"
    ]"""
    message = "Po dlouhem cekani nastal cas planovaneho vyletu do Jablonce k prehrade. Spolu s cz_1shark1 a cz_Yetti jsme se chladneho sobotniho rana dopravili k prehrade a posbirali nejake ty krabicky. Peclive pripravenou trasu kolem prehrady, jsme jeste navic museli obohatit keskami 'pri ceste'. Na konci dne jsme slavili peknych 34 kesi. Diky za pozvani a dalsi bodik."
    g = Geo()
    print 'login'
    g.login('', '')

    for link in urls:
        print 'logging: ' + link
        g.log_cache(url=link, message=message, date_visited="20.Mar.2015")