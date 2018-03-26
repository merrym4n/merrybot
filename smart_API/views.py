#from django.shortcuts import render
from django.http import JsonResponse
import json

def keyboard(request):
	return JsonResponse({
		'type' : 'button',
		'button' : ['gkrtlr']
	})

def message(request):
	'''
	message = ((request.body).decode('utf-8'))
	return_json_str = json.loads(message)
	return_str = return_json_str['content']
	requestMode = return_str.encode('utf-8')

	if requestMode == 'gkrtlr':
		return JsonResponse({
			'message' : {
				'text' : "gkrtlr vktldgksrj sjgdmfrj"
			},
			'keyboard' : {
				'type' : 'text'
			}
		})
	'''
	message = ((request.body).decode('utf-8'))
	return_json_str = json.loads(message)
	return_str = return_json_str['content']
	
	return JsonResponse({
		'message' : {
			return_str
		},
		'keyboard' : {
			'type' : 'buttons',
			'buttons' : ['1', '2']
		}
	})
