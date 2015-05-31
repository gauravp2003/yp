#!/usr/bin/env python
"""
usage: python args.py [options]

Fetching Names and Address listed in YP.

optional arguments:
  -h, --help            show this help message and exit
  -l LASTNAME, --lastname LASTNAME
                        Enter LastName
  -c CITY, --city CITY  Enter City
  -z ZIP, --zip ZIP     Enter ZipCode
  -s STATE, --state STATE
                        Enter State
  -d DELIMITER, --delimiter DELIMITER
                        Enter delimiter: Default - "|"

ubuntu@ubuntu:~$ ./address.py -l patterson -c 85029 -s AZ

[u'Bill  Patterson|3614 W Sunnyside Dr, Phoenix, AZ 85029|6028435715', u'Donald E Patterson|1653 W Yucca St #1, Phoenix, AZ 85029|6029972129', u'Elizabeth  Patterson|4027 W Mercer Ln, Phoenix, AZ 85029', u'Faith S Patterson|3608 W Sunnyside Dr, Phoenix, AZ 85029|6029381775', u'Gary L Patterson|10634 N 10th Dr, Phoenix, AZ 85029|6029970722', u'James L Patterson|3608 W Sunnyside Dr, Phoenix, AZ 85029|6029381775', u'James L Patterson|3608 W Sunnyside Ave, Phoenix, AZ 85029|6029381775', u'Kathy  Patterson|2616 W Corrine Dr, Phoenix, AZ 85029|6026332856', u'Kimberley  Patterson|11821 N 28th Dr, Phoenix, AZ 85029|6029389044', u'Kimberly  Patterson|11821 N 28th Dr, Phoenix, AZ 85029|6029389044', u'L M Patterson|3626 W Andora Dr, Phoenix, AZ 85029|6029783626', u'Lewis R Patterson|4027 W Mercer Ln, Phoenix, AZ 85029', u'Markelia M Patterson|2529 W Cactus Rd, Phoenix, AZ 85029|6029432788', u'Shirley  Patterson|2102 W Cholla St, Phoenix, AZ 85029|6029978040', u'Stanley P Patterson|2102 W Cholla St, Phoenix, AZ 85029|6029978040', u'Stephen R Patterson|3010 W Paradise Dr, Phoenix, AZ 85029|6029425966', u'Susan  Patterson|13448 N 31st Ave, Phoenix, AZ 85029|6028432972', u'Varrell  Patterson|4020 W Cortez St, Phoenix, AZ 85029', u'William R Patterson|3614 W Sunnyside Dr, Phoenix, AZ 85029|6028435715']


"""
import mechanize
import cookielib
import sys
from BeautifulSoup import BeautifulSoup          # For processing HTML
from mechanize import ParseResponse, urlopen, urljoin
import argparse
import time
import pprint
pp = pprint.PrettyPrinter(indent=4)

#def get_num(x):
#    return int(''.join(ele for ele in x if ele.isdigit()))
#def is_number(s):
#    try:
#        int(s)
#        return int(s)
#    except ValueError:
#        return 0
def getDetails(lastname,add,state):
    """
    address.getDetails("lastname","city","state","|")
    """
    br = mechanize.Browser(factory=mechanize.RobustFactory())
    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    # Don't handle HTTP-EQUIV headers (HTTP headers embedded in HTML).
    br.set_handle_equiv(False)
    # Don't Ignore robots.txt.
    br.set_handle_robots(True)
    #  add Referer (sic) header
    br.set_handle_referer(True)
    #  handle Refresh redirections
    br.set_debug_redirects(True)
    # Log HTTP response bodies (ie. the HTML, most of the time).
    br.set_debug_responses(True)
    # Print HTTP headers.
    #br.set_debug_http(True)
    
    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=10)
    i = 0
    gonext = True
    details = []
    while gonext:
        urlCreated = 'http://www.yellowpages.com/whitepages?first=&last='+str(lastname)+'&zip='+str(add)+'&state='+str(state)+'&start=' + str(i*10)
        #Opens the site to be navigated
        response = br.open(urlCreated)
        soup = BeautifulSoup(br.response().read())
        allLi = soup.findAll("div", { "class" : "phone-result-container"})
        gonext = len(allLi)>0
        if gonext:    
            for item in allLi:
                d = []
                d.append(item.find('a',{"class":'fullname'}).text)
                d.append(item.find('p',{"class":'address'}).text)
                d.append(item.find('p',{"class":'phone'}).text)
                details.append(d)
            i = i+1
        else:
            print "Processing Complete for",lastname,add,state
            return details

def main():
    parser = argparse.ArgumentParser(description='Fetching Names and Address listed in YP.',prog='python address.py', usage='%(prog)s [options]')
    parser.add_argument('-l','--lastname', help='Enter LastName',required=True)
    parser.add_argument('-c','--city', help='Enter City')
    parser.add_argument('-z','--zip', help='Enter ZipCode')
    parser.add_argument('-s','--state', help='Enter State',required = "True")
    parser.add_argument('-d','--delimiter', help='Enter delimiter: Default - "|"',default = "|")      
    values = parser.parse_args()
    lastname = values.lastname
    if (values.city is not None):
        add = "+".join(values.city.split())
    elif values.zip is not None:
        add = values.zip
    else:
        print "Enter City and State -s or Zip -z"
        sys.exit(0)
    lastName = "+".join(lastname.split())
    state = values.state
    delimiter = values.delimiter
    details = getDetails(lastname,add,state)
    details = [delimiter.join(item) for item in details]
    pp.pprint(details)


if __name__ == '__main__':
    main()  
