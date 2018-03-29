from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import sys

sys.path.insert(0, '/home/ubuntu/merrybot/parser')
import test
import cafeteria

def keyboard(requests):
    return JsonResponse({
        'type': 'text'
    })


@csrf_exempt
def message(requests):
    message = ((requests.body).decode('utf-8'))
    
    if(message.find(u'ㅎㅇ')>-1 or message.find(u'안녕')>-1):
        return_str = (test.hello())#.decode('utf-8') + "안녕하세요!!!\n"

    elif(message.find(u'학생회관')>-1 or message.find(u'학관')>-1 or message.find(u'ㅎㄱ')>-1):
        return_str = cafeteria.students_hall()

    elif(message.find(u'우정')>-1 or message.find(u'ㅇㅈ')>-1):
        return_str = cafeteria.woojung()

    elif(message.find(u'군자')>-1 or message.find(u'ㄱㅈ')>-1):
        return_str = cafeteria.gunja()

    else:
        return_json_str = json.loads(message)
        return_str = return_json_str['content']

    return JsonResponse({
        'message':{
            'text':return_str
        },
        'keyboard':{
            'type':'text'
        }
    }) 
