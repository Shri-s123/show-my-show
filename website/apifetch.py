import requests, json
from .models import Shows_onair
from . import db





def fetch_api1():
    req=requests.get('https://api.tvmaze.com/schedule/full')
    data=json.loads(req.content)
    for item in range(300):

        id=data[item]['_embedded']['show']['id']
        name=data[item]['_embedded']['show']['name']
        language=data[item]['_embedded']['show']['language']
        genres=data[item]['_embedded']['show']['genres']
        rating=data[item]['_embedded']['show']['rating']['average']
        try:
            image=data[item]['_embedded']['show']['image']['medium']
        except:
            image=''
        summary=data[item]['_embedded']['show']['summary']
        
            
        while genres:
            show_obj=Shows_onair(showid=id,name=name,language=language,genres=genres[-1],rating=rating,image=image,summary=summary)
            genres.pop()
            db.session.add(show_obj)
            try:
                db.session.commit()
            except:
                db.session.rollback()

        






    
    