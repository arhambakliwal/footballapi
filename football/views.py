from django.shortcuts import render
import requests
import json
def start(request):

    city_id = [2002, 2003]



    # connection = http.client.HTTPConnection('api.football-data.org')
    data = []
    for i in city_id:
        # connection.request('GET', f'/v2/competitions/{i}/matches?matchday=1', None, headers)
        # response = json.loads(connection.getresponse().read().decode())
        url = (f'http://api.football-data.org/v2/competitions/{i}/matches?matchday=1')
        headers = {'X-Auth-Token': '529a6ff7d330482293a2fb4dfa64ce8a'}
        response = requests.get(url, headers=headers).json()
        data.append(response)
    d = []
    for i in range(len(data)):
        d.append(data[i]['matches'][0]['season']['currentMatchday'])
    a = 0
    finaldata = []
    for i in city_id:
        b = d[a]
        # connection.request('GET', f'/v2/competitions/{i}/matches?matchday={b}', None, headers)
        # response = json.loads(connection.getresponse().read().decode())
        url = (f'http://api.football-data.org/v2/competitions/{i}/matches?matchday={b}')
        headers = {'X-Auth-Token': '529a6ff7d330482293a2fb4dfa64ce8a'}
        response = requests.get(url, headers=headers).json()
        finaldata.append(response)
        a += 1

    result = []
    img=["https://upload.wikimedia.org/wikipedia/en/thumb/d/df/Bundesliga_logo_%282017%29.svg/285px-Bundesliga_logo_%282017%29.svg.png","https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Eredivisie_nieuw_logo_2017-.svg/1920px-Eredivisie_nieuw_logo_2017-.svg.png"]

    for i in range(len(finaldata)):

        for j in range(len(finaldata[0]['matches'])):
            if finaldata[i]['matches'][j]['status'] == "SCHEDULED":
                d1 = {'name': finaldata[i]['competition']['name'],
                      'hteam': finaldata[i]['matches'][j]['homeTeam']['name'],
                      'ateam': finaldata[i]['matches'][j]['awayTeam']['name'],
                      'date': finaldata[i]['matches'][j]['utcDate'][0:10],
                      'score': '',
                      'img':img[i]

                      }
            else:
                d1 = {'name': finaldata[i]['competition']['name'],
                      'hteam': finaldata[i]['matches'][j]['homeTeam']['name'],
                      'ateam': finaldata[i]['matches'][j]['awayTeam']['name'],
                      'date': finaldata[i]['matches'][j]['utcDate'][0:10],
                      'score': finaldata[i]['matches'][j]['score']['fullTime'],
                      'img':img[i]
                      }

            result.append(d1)

    x={'result':result}
    print(len(x['result']))
    return render(request,'index.html',x)

