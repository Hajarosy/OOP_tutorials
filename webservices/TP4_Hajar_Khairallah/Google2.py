api_key = 'AIzaSyBE9uTW092pQDZDkQ9KgRvwBMuVShiuM54'
url='https://maps.googleapis.com/maps/api/directions/json?origin=Paris&destination=Anto ny&mode=driving&key=AIzaSyBE9uTW092pQDZDkQ9KgRvwBMuVShiuM54'


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


print (color.BOLD +color.BLUE + 'Welcome !' + color.END)

import json
import requests
page=requests.get(url)
content=page.content
data=json.loads(content)
routes=data['routes']
legs=routes[0]['legs'][0]['steps']
print(color.BOLD + color.RED + "Follow the itinerary:" + color.END)
for e in legs:
    instructions=e['html_instructions']
    distance=e['distance']['text']
    print("In {} {} {}".format(distance,",",instructions.replace("<b>",color.BOLD).replace("</b>",color.END).replace("<div style=" ,"").replace("</div>","").replace("font-size:0.9em","").replace('"">'," - ")))
print(color.BOLD + color.YELLOW + "Congratulations, you have reached your destination :)" + color.END)
    #print(instructions)





