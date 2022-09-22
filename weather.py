import urllib.request , urllib.parse , urllib.error 
import json
def n():
    print('')




location = input('Enter Location: ')

key = 'e213e86ba9c548c9b7f92445222209'

address =  'http://api.weatherapi.com/v1/current.json?key=e213e86ba9c548c9b7f92445222209'

test = '&'+urllib.parse.urlencode({'q':location})

#print(test)


try:
    url = urllib.request.urlopen(address+test)

    test1 = url.read().decode()

    js = json.loads(test1)

    #print(js)

    #print(json.dumps(js,indent=4))
    n()
    print('### Informatoin of Region ###','\n')
    country = js["location"]["country"]
    print('Country = ',country)
    city = js["location"]["name"]
    print('City = ',city)
    localtime= js["location"]["localtime"]
    print('Localtime = ',localtime)
    lat = js["location"]["lat"]
    lon = js["location"]["lon"]
    print('Latitude = ',lat)
    print('Longitude = ',lon)
    n()
    n()
    print('### Temperature Information of that Region ###')
    n()

    ctc=js["current"]["temp_c"]
    print('Temp C = ',ctc,'C')
    fctc = js["current"]["feelslike_c"]
    print('Feels like in C = ',fctc,'C')
    fctf = js["current"]["feelslike_f"]
    ctf = js["current"]["temp_f"]
    print('Temp F = ',ctf,'F')
    fctf =js["current"]["feelslike_f"]
    print('Feels like in F = ',fctf,'F')

    n()
    n()
    print('### Other Informatoin Weather Informatoin of that Region ###')
    n()
    env = js["current"]["condition"]["text"]
    print('Environment = ',env)
    cloud = js["current"]["cloud"]
    print('Cloud = ',cloud)
    humidity = js["current"]["humidity"]
    print('Humidity = ',humidity,'%')
    vis_km = js["current"]["vis_km"]
    print('Visibility in KM = ',vis_km,'km')
    vis_miles = js["current"]["vis_miles"]
    print('Visibility in Miles = ',vis_miles,'miles')
    wind_kph = js["current"]["wind_kph"]
    print('Wind KPH = ',wind_kph,'kph')
    wind_mph = js["current"]["wind_mph"]
    print ('Wind MPH = ',wind_mph,'mph')

except:
    print('You may have entered incorrect Location or The Service is unavailable right now.')
    exit()


print('Created by haroon.rehman6@gmail.com')