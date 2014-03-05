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

