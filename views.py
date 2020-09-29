from django.shortcuts import render, redirect
from django.contrib import messages
import requests
import json
import datetime , calendar

# Create your views here.
def PLhome(request):
    return render(request, 'PLhome.html')

def PLinfo(request):
    import requests
    import json
    vanityID = request.POST['vanityID']
    steam_api_key = '26FAF13010711CA55DEE6148E4327B21'
    is_int = True
    goodtogo = True
    try:
        int(vanityID)
    except ValueError:
        is_int = False
    if is_int == False:
        try:
            vanityID_converter = 'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key='+ steam_api_key + '&vanityurl=' + vanityID
            r = requests.get(vanityID_converter)
            steamID_data = r.json()
            steamID = steamID_data['response']['steamid']
            # print(steamID)
        except KeyError:
            goodtogo = False
    else:
        try:
            steamID = vanityID
            check = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=' + steam_api_key + '&steamids=' + steamID
            x = requests.get(check)
            summmary_data = x.json()
            thing = summmary_data['response']['players'][0]['personaname']
        except IndexError:
            goodtogo = False
    if goodtogo == True:
        try:
            # code below gets the total hours of all the games played combined ~~~ 
            GetOwnedGames = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=' + steam_api_key + '&steamid=' + steamID + '&format=json&include_appinfo=true'
            tempGetOwnedGames = requests.get(GetOwnedGames)
            dataGetOwnedGames = tempGetOwnedGames.json()
            countPlaytime_forever = 0
            L = []
            for i in range(len(dataGetOwnedGames['response']['games'])):
                L.append(int(dataGetOwnedGames['response']['games'][i]['playtime_forever']))
                countPlaytime_forever = countPlaytime_forever + int(dataGetOwnedGames['response']['games'][i]['playtime_forever'])
            total_hours_all = countPlaytime_forever // 60

            L.sort(reverse=True)

            Favorite_games = []
            Favorite_games_imgurl = []
            Favorite_games_appid = []
            for i in range(3):
                for j in range(len(dataGetOwnedGames['response']['games'])):
                    if dataGetOwnedGames['response']['games'][j]['playtime_forever'] == L[i]:
                        Favorite_games.append(dataGetOwnedGames['response']['games'][j]['name'])
                        Favorite_games_imgurl.append(dataGetOwnedGames['response']['games'][j]['img_icon_url'])
                        Favorite_games_appid.append(dataGetOwnedGames['response']['games'][j]['appid'])   
            F_game_one = Favorite_games[0]
            F_game_two = Favorite_games[1]
            F_game_three = Favorite_games[2]
            F_game_one_hours = str(L[0] // 60)
            F_game_two_hours = str(L[1] // 60)
            F_game_three_hours = str(L[2] // 60)
            F_game_one_imgurl = Favorite_games_imgurl[0]
            F_game_two_imgurl = Favorite_games_imgurl[1]
            F_game_three_imgurl = Favorite_games_imgurl[2]
            F_game_one_appid = Favorite_games_appid[0]
            F_game_two_appid = Favorite_games_appid[1]
            F_game_three_appid = Favorite_games_appid[2]
            F_game_one_icon = 'http://media.steampowered.com/steamcommunity/public/images/apps/'+ str(F_game_one_appid) + '/' + F_game_one_imgurl + '.jpg'
            F_game_two_icon = 'http://media.steampowered.com/steamcommunity/public/images/apps/'+ str(F_game_two_appid) + '/' + F_game_two_imgurl + '.jpg'
            F_game_three_icon = 'http://media.steampowered.com/steamcommunity/public/images/apps/'+ str(F_game_three_appid) + '/' + F_game_three_imgurl + '.jpg'
        except KeyError:
            total_hours_all = '0'
            F_game_one_hours = '0'
            F_game_two_hours = '0'
            F_game_three_hours = '0'
            F_game_one = 'need more games sorry'
            F_game_two = 'account may be private'
            F_game_three = 'yeap'
            F_game_one_icon = '/static/Pipeline/Images/default_steam_icon.jpg'
            F_game_two_icon = '/static/Pipeline/Images/default_steam_icon.jpg'
            F_game_three_icon = '/static/Pipeline/Images/default_steam_icon.jpg'
        
        # THE CODE BELOW IS TEMPORARY !
        if F_game_one_hours == '0':
            graph_one_move = 'margin-top: 180px;'
        elif int(F_game_one_hours) < 300:
            graph_one_move = 'margin-top: 150px;'
        elif int(F_game_one_hours) < 400 and int(F_game_one_hours) > 299:
            graph_one_move = 'margin-top: 145px;'
        elif int(F_game_one_hours) < 500 and int(F_game_one_hours) > 399:
            graph_one_move = 'margin-top: 140px;'
        elif int(F_game_one_hours) < 600 and int(F_game_one_hours) > 499:
            graph_one_move = 'margin-top: 135px;'
        elif int(F_game_one_hours) < 700 and int(F_game_one_hours) > 599:
            graph_one_move = 'margin-top: 130px;'
        elif int(F_game_one_hours) < 800 and int(F_game_one_hours) > 699:
            graph_one_move = 'margin-top: 125px;'
        elif int(F_game_one_hours) < 1000 and int(F_game_one_hours) > 799:
            graph_one_move = 'margin-top: 115px;'
        elif int(F_game_one_hours) < 1200 and int(F_game_one_hours) > 999:
            graph_one_move = 'margin-top: 105px;'
        elif int(F_game_one_hours) < 1400 and int(F_game_one_hours) > 1199:
            graph_one_move = 'margin-top: 95px;'
        elif int(F_game_one_hours) < 1600 and int(F_game_one_hours) > 1399:
            graph_one_move = 'margin-top: 85px;'
        elif int(F_game_one_hours) < 1800 and int(F_game_one_hours) > 1599:
            graph_one_move = 'margin-top: 75px;' 
        elif int(F_game_one_hours) > 2000 and int(F_game_one_hours) > 1799:
            graph_one_move = 'margin-top: 50px;'
        elif int(F_game_one_hours) < 3000 and int(F_game_one_hours) > 1999:
            graph_one_move = 'margin-top: 35px;'
        elif int(F_game_one_hours) < 4000 and int(F_game_one_hours) > 2999:
            graph_one_move = 'margin-top: 20px;'
        
        if F_game_two_hours == '0':
            graph_two_move = 'margin-top: 180px;'
        elif int(F_game_two_hours) < 300:
            graph_two_move = 'margin-top: 150px;'
        elif int(F_game_two_hours) < 400 and int(F_game_two_hours) > 299:
            graph_two_move = 'margin-top: 145px;'
        elif int(F_game_two_hours) < 500 and int(F_game_two_hours) > 399:
            graph_two_move = 'margin-top: 140px;'
        elif int(F_game_two_hours) < 600 and int(F_game_two_hours) > 499:
            graph_two_move = 'margin-top: 135px;'
        elif int(F_game_two_hours) < 700 and int(F_game_two_hours) > 599:
            graph_two_move = 'margin-top: 130px;'
        elif int(F_game_two_hours) < 800 and int(F_game_two_hours) > 699:
            graph_two_move = 'margin-top: 125px;'
        elif int(F_game_two_hours) < 1000 and int(F_game_two_hours) > 799:
            graph_two_move = 'margin-top: 115px;'
        elif int(F_game_two_hours) < 1200 and int(F_game_two_hours) > 999:
            graph_two_move = 'margin-top: 105px;'
        elif int(F_game_two_hours) < 1400 and int(F_game_two_hours) > 1199:
            graph_two_move = 'margin-top: 95px;'
        elif int(F_game_two_hours) < 1600 and int(F_game_two_hours) > 1399:
            graph_two_move = 'margin-top: 85px;'
        elif int(F_game_two_hours) < 1800 and int(F_game_two_hours) > 1599:
            graph_two_move = 'margin-top: 75px;' 
        elif int(F_game_two_hours) > 2000 and int(F_game_two_hours) > 1799:
            graph_two_move = 'margin-top: 50px;'
        elif int(F_game_two_hours) > 3000 and int(F_game_two_hours) > 1999:
            graph_two_move = 'margin-top: 35px;'
        elif int(F_game_two_hours) > 4000 and int(F_game_two_hours) > 2999:
            graph_two_move = 'margin-top: 20px;'

        if F_game_three_hours == '0':
            graph_three_move = 'margin-top: 180px;'
        elif int(F_game_three_hours) < 300:
            graph_three_move = 'margin-top: 150px;'
        elif int(F_game_three_hours) < 400 and int(F_game_three_hours) > 299:
            graph_three_move = 'margin-top: 145px;'
        elif int(F_game_three_hours) < 500 and int(F_game_three_hours) > 399:
            graph_three_move = 'margin-top: 140px;'
        elif int(F_game_three_hours) < 600 and int(F_game_three_hours) > 499:
            graph_three_move = 'margin-top: 135px;'
        elif int(F_game_three_hours) < 700 and int(F_game_three_hours) > 599:
            graph_three_move = 'margin-top: 130px;'
        elif int(F_game_three_hours) < 800 and int(F_game_three_hours) > 699:
            graph_three_move = 'margin-top: 125px;'
        elif int(F_game_three_hours) < 1000 and int(F_game_three_hours) > 799:
            graph_three_move = 'margin-top: 115px;'
        elif int(F_game_three_hours) < 1200 and int(F_game_three_hours) > 999:
            graph_three_move = 'margin-top: 105px;'
        elif int(F_game_three_hours) < 1400 and int(F_game_three_hours) > 1199:
            graph_three_move = 'margin-top: 95px;'
        elif int(F_game_three_hours) < 1600 and int(F_game_three_hours) > 1399:
            graph_three_move = 'margin-top: 85px;'
        elif int(F_game_three_hours) < 1800 and int(F_game_three_hours) > 1599:
            graph_three_move = 'margin-top: 75px;' 
        elif int(F_game_three_hours) > 2000 and int(F_game_three_hours) > 1799:
            graph_three_move = 'margin-top: 50px;'
        elif int(F_game_three_hours) > 3000 and int(F_game_three_hours) > 1999:
            graph_three_move = 'margin-top: 35px;'
        elif int(F_game_three_hours) > 4000 and int(F_game_three_hours) > 2999:
            graph_three_move = 'margin-top: 20px;'
    
        #____________________________________________________ ~~~
        # code below gets the Profile name of the steamID given / it also gets the Profile img of the steamID given / it also gets the Profiles status ~~~
        GetPlayerSummaries = ' http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=' + steam_api_key + '&steamids=' + steamID
        tempGetPlayerSummaries = requests.get(GetPlayerSummaries)
        dataGetPlayerSummaries = tempGetPlayerSummaries.json()
        proile_name = dataGetPlayerSummaries['response']['players'][0]['personaname']
        Profile_avatar = dataGetPlayerSummaries['response']['players'][0]['avatarfull']
        tempProfile_status = dataGetPlayerSummaries['response']['players'][0]['profilestate']
        tempProfile_state = dataGetPlayerSummaries['response']['players'][0]['communityvisibilitystate']
        online = False
        offline = False
        away = False
        if tempProfile_status == 0:
            Profile_status = 'Offline'
            offline = True
        elif tempProfile_status == 1:
            Profile_status = 'Online'
            online = True
        elif tempProfile_status == 2:
            Profile_status = 'Busy'
            away = True
        elif tempProfile_status == 3:
            Profile_status = 'Away'
            away = True
        elif tempProfile_status == 4:
            Profile_status = 'Snooze'
            away = True
        elif tempProfile_status == 5:
            Profile_status = 'Looking to Trade'
            online = True
        elif tempProfile_status == 6:
            Profile_status = 'Looking to Play'
            online = True
        
        if tempProfile_state == 1:
            Profile_state = 'Private'
        elif tempProfile_state == 2:
            Profile_state = 'Private'
        elif tempProfile_state == 3:
            Profile_state = 'Public'
        
        
        if Profile_state == 'Public':
            tempProfile_created = dataGetPlayerSummaries['response']['players'][0]['timecreated']
            dataProfile_created = datetime.datetime.fromtimestamp(tempProfile_created)
            monthname = calendar.month_name[dataProfile_created.month]
            Profile_created =  str(monthname) + ' ' + str(dataProfile_created.day) + ', ' + str(dataProfile_created.year)
        elif Profile_state == 'Private':
            Profile_created = 'Private'
        link_to_steam_prof = 'http://steamcommunity.com/profiles/' + steamID
        
        #_______________________________________________________ ~~~
        #
        context = {
            'info': {
                'steamID': steamID ,
                'total_hours': total_hours_all,
                'profile_name': proile_name,
                'profile_img': Profile_avatar,
                'profile_status': Profile_status,
                'profile_state': Profile_state,
                'profile_created': Profile_created,
                'online': online,
                'offline': offline, 
                'away': away,
                'F_game_one': F_game_one,
                'F_game_two': F_game_two,
                'F_game_three': F_game_three,
                'F_game_one_icon': F_game_one_icon,
                'F_game_two_icon': F_game_two_icon,
                'F_game_three_icon': F_game_three_icon,
                'link_to_steam_prof': link_to_steam_prof,
                'F_game_one_hours': F_game_one_hours,
                'F_game_two_hours': F_game_two_hours,
                'F_game_three_hours': F_game_three_hours,
                'graph_one_move': graph_one_move,
                'graph_two_move': graph_two_move,
                'graph_three_move': graph_three_move,
                
            }
        }
        return render(request, 'PLinfo.html', context)
        
    if goodtogo == False:
        messages.info(request, "SteamID Doesn't Exist")
        return redirect('/pipeline/')