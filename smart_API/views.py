from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def keyboard(requests):
    return JsonResponse({
        'type': 'text'
    })


@csrf_exempt
def message(requests):
    message = ((requests.body).decode('utf-8'))
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
