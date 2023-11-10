#!/usr/bin/python3
import requests
import argparse
from dotenv import load_dotenv

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    startdate = "start_date=" + args.startdate
    #enddate = "end_date=" + args.enddate

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    #neowrequest = requests.get(NEOURL + startdate + "&" + enddate + "&" + nasacreds)
    url = NEOURL + startdate + "&" + nasacreds
    
    if args.enddate:
        url += "&end_date=" + args.enddate
    neowrequest = requests.get(url)
    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pass arguments to search the NASA API")
    parser.add_argument('--startdate', metavar='SEARCHW', type=str, default='1900-01-01', help="Search's start date")
    parser.add_argument('--enddate', metavar='SEARCHW', type=str, help="Search's end date")
    args = parser.parse_args()
    main()

