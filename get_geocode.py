# -*- coding: utf-8 -*- 
import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
import json
import urllib2

def get_geodata(url, addr_str):
    #print url     
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request = urllib2.Request(url=url+addr_str, data='')
    request.get_method = lambda: 'GET'
    try:
        request_result = opener.open(request)
        the_page = request_result.read()
        response = json.loads(the_page)
        #fordebug
        #print response
        if int(response['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData']['found'])>0:
            for k in response['response']['GeoObjectCollection']['featureMember']:
                if k['GeoObject']['metaDataProperty']['GeocoderMetaData']['precision'] in ['exact','street','near','number']:
                    po = k['GeoObject']['Point']['pos'].split(" ")
                    return '['+po[1]+','+po[0]+']'
                else:
                    print "no coordinates were found for address "+addr_str
            #print "Found"
        else:
            print addr_str
            return ''
    except urllib2.HTTPError, err:
        print 'HTTP error ' +str(err.code)
        raise

if __name__ == "__main__":
    #Reading arguments
    api_url = 'https://geocode-maps.yandex.ru/1.x/?format=json&geocode='

    json_file_path = './data/deliveries_spb.json'
    fp = open(json_file_path, 'r')
    #print fp.read()
    json_value = fp.read()
    raw_data = json.loads(json_value)
    address_list = []

    for a in raw_data:
        address_list.append('Saint Petersburg, '+a.get('street','')+", "+a.get('house','')+"/"+a.get('corps','')+", "+a.get('apartment',''))
        

    #print get_geodata(url = api_url, addr_str = str("Saint Petersburg, Альпийский пер, 15-1/, 173 "))    
    fdata = open('static/data_spb.js','w')
    fdata.write('var data = [')
    
    data = []
    for i in range(len(address_list)):
        points = get_geodata(url = api_url, addr_str = str(address_list[i]))
        data.append(points) 

    #print data 
    for k in range(0,len(data)):
        #print address_list[k], data[k] 
        if data[k]<>None:
            fdata.write(str(data[k]))
            fdata.write(',')
    fdata.write('];')
    fdata.close()

    # #print processed_data
    # with open(csv_file_path, 'wb+') as f:
    #     writer = csv.DictWriter(f, header, quoting=csv.QUOTE_ALL)
    #     writer.writeheader()
    #     for row in processed_data:
    #         writer.writerow(row)

    #print "Just completed writing csv file with %d columns" % len(header)