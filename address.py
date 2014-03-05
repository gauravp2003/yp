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
gaurav@ubuntu:~/Documents/address$ 


"""
import mechanize
import cookielib
import sys
from BeautifulSoup import BeautifulSoup          # For processing HTML
from mechanize import ParseResponse, urlopen, urljoin
import argparse
import time


def get_num(x):
    return int(''.join(ele for ele in x if ele.isdigit()))
def is_number(s):
    try:
        int(s)
        return int(s)
    except ValueError:
        return 0
def getDetails(lastname,add,state,delimiter):
    """
    address.getDetails("lastname","city","state","|")
    """
    br = mechanize.Browser(factory=mechanize.RobustFactory())
    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    # Don't handle HTTP-EQUIV headers (HTTP headers embedded in HTML).
    br.set_handle_equiv(False)
    # Ignore robots.txt.  Do not do this without thought and consideration.
    br.set_handle_robots(False)
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
    # User-Agent (this is cheating, ok?)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    i = 0
    gonext = True
    details = []
    while gonext:
        urlCreated = 'http://www.yellowpages.com/whitepages?fap_terms%5Bcity%5D='+add+'&amp;fap_terms%5Bfirst%5D=&amp;fap_terms%5Blast%5D=' +  lastname + '&amp;fap_terms%5Bstate%5D='+ state + '&amp;offset='+ str(i*10)

        #Opens the site to be navigated
        response = br.open(urlCreated)
        soup = BeautifulSoup(br.response().read())
        #t = soup.find("h2", {"id": "pagination-count"})
        allLi = soup.findAll("address", { "class" : "fap-address-result"})
        gonext = len(allLi)>0
        #print "length:" ,len(allLi)     
        if gonext:    
	    for item in allLi:
	        numberPhone = is_number("".join(str(item.text[-12:]).split("-")))
	        if numberPhone != 0:
                    d = delimiter.join([item.a.text,item["data-street"],str(numberPhone)])
	        else:
	            d = delimiter.join([item.a.text,item["data-street"]])
                #print d,item.text
                details.append(d)
        #else:
            #print "Processing Complete for",lastname,add,state
        i = i+1
    return details

def main():
	parser = argparse.ArgumentParser(description='Fetching Names and Address listed in YP.',prog='python args.py', usage='%(prog)s [options]')
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
	    print "Enter City and State or Zip"
	    sys.exit(0)
	lastName = "+".join(lastname.split())
        state = values.state
        delimiter = values.delimiter
        details = getDetails(lastname,add,state,delimiter)
        print details


if __name__ == '__main__':
    main() 	
