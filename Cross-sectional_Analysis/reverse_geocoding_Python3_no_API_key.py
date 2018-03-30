import csv
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

##from bs4 import BeautifulSoup
import codecs
#import unicodedata
import json
import time

#1. read the inpit file

#2. define a function
#def reversegeocode(starting_value, ending_value, output_seq, api_key):
def reversegeocode(starting_value, ending_value, api_key):
    ##myfile=open('M:/Millennial_20UA/Data/GooglePlacesAPI/restaurant/restaurant_outcome01.csv', 'wt')
    point_blkgrp = []
    point_lat = []
    point_lng = []
    input_addr = '../Dataset_MAIN/School_District_Quality/CT_Centroid.csv'
    #"M:/Millennial_CA/21_RC_LCCM/03_data_process/07_Python/Bak_reversegeocode/blkgrp10_meancenter245.csv"
    with open(input_addr) as inputfile:
        next(inputfile)
        inputread = csv.reader(inputfile, delimiter=',')
        for row in inputread:
            point_blkgrp.append(row[0])
            point_lat.append(row[2])
            point_lng.append(row[1])

    ##output_addr= "M:/Millennial_CA/21_RC_LCCM/03_data_process/07_Python/blkgrp10_meancenter_addr" + output_seq + ".csv"
    output_addr= "../Dataset_MAIN/School_District_Quality/CT_Centroid_outcome.csv"
    myfile=open(output_addr, 'wt')
    outputfile = csv.writer(myfile, delimiter=',', lineterminator='\n')
    outputfile.writerow(["FIPS_alt", "formatted_add", "loc_type", "add_type", "status"])

    for i in range(starting_value, ending_value):
        row = []
        row.append(point_blkgrp[i])
        y = point_lat[i]
        x = point_lng[i]
        url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='+"%s"%y+","+"%s"%x+'&key='+api_key
        print(url)
        try:
            page = urlopen(url)
            reader=codecs.getreader("utf-8") # in case foreign characters appear
            queryresult = json.load(reader(page)) # load a dataset in the jason format
            status = queryresult["status"] # check the query status
            if status == "OK":
                formatted_add = queryresult["results"][0]["formatted_address"]
                loc_type = queryresult["results"][0]["geometry"]["location_type"]
                add_type = queryresult["results"][0]["types"][0]
                results = [formatted_add, loc_type, add_type, status]
                row.extend(results)
                print (row)
                outputfile.writerow(row)
                myfile.flush()
                del row[1:5]
            else:
                results = ['-1', '-1', 'Status not OK']
                row.extend(results)
                print (row)
                outputfile.writerow(row)
                myfile.flush()
                #del row[1:6]
        except HTTPError as e:
            print(e)
            results = ['-1', '-1', 'HTTPError']
            row.extend(results)
            print (row)
            outputfile.writerow(row)
            myfile.flush()
            #del row[1:6]
            time.sleep(30)
        except URLError as e:
            print(e)
            results = ['-1', '-1', 'URLError']
            row.extend(results)
            print (row)
            outputfile.writerow(row)
            myfile.flush()
            #del row[1:6]
            time.sleep(180)
        except ConnectionResetError as e:
            print(e)
            results = ['-1', '-1', 'ConnectionResetError']
            row.extend(results)
            print (row)
            outputfile.writerow(row)
            myfile.flush()
            #del row[1:6]
            time.sleep(180)
    myfile.close()

#3.execute each run of 140,000 queries

API01 = 'AIzaSyCZ7TzH5FDCAjfvjDkLqrOvRgWWmfgQTLk'
API02 = ''
API03 = ''
API04 = ''
API05 = ''
API06 = ''
API07 = ''
API08 = ''
API09 = ''
API10 = ''
API11 = ''
API12 = ''

#reversegeocode(    0,  10, '01', API01)
#reversegeocode(    0,  2000, '01', API01)
#reversegeocode( 2000,  4000, '02', API02)
#reversegeocode( 4000,  6000, '03', API03)
#reversegeocode( 6000,  8000, '04', API04)
#reversegeocode( 8000, 10000, '05', API05)

#reversegeocode(10000, 12000, '06', API06)
#reversegeocode(12000, 14000, '07', API07)
#reversegeocode(14000, 16000, '08', API08)
#reversegeocode(16000, 18000, '09', API09)
#reversegeocode(18000, 20000, '10', API10)

#reversegeocode(20000, 22000, '11', API11)
#reversegeocode(22000, 23162, '12', API12)
reversegeocode(0, 976, API01)
