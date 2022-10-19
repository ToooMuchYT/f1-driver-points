import requests
import json
from pprint import pprint

def driver_names(season):

    url="http://ergast.com/api/f1/"+season+"/drivers.json"
    response = requests.get(url)
    dinfo=json.loads(response.text)['MRData']
    totalDrivers =int(dinfo['total'])
    result=[]
    for i in range(totalDrivers):
        result.append(dinfo['DriverTable']['Drivers'][i]['driverId'])
    return result

def driver_points(dname,season):

    url="http://ergast.com/api/f1/"+season+"/drivers/"+dname+"/driverStandings.json"
    response = requests.get(url)
    dinfo=json.loads(response.text)['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'][0] 
    result = dinfo['points']
    return result

def Schedule(season):
    url="https://ergast.com/api/f1/"+season+".json"
    response=requests.get(url)
    dinfo=json.loads(response.text)['MRData']
    totalGp=int(dinfo['total'])
    result = []
    for i in range(totalGp):
        dict1={'race':dinfo["RaceTable"]["Races"][i]['raceName'],'date':dinfo["RaceTable"]["Races"][i]['date']}
        result.append(dict1)
    return result
    #pprint(response.text)



# pprint(driver_names("2022"))