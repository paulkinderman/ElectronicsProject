from django.shortcuts import render
import boto3
from boto3.dynamodb.conditions import Key, Attr
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")
    table = dynamodb.Table('Buildings')
#   response = table.query(
#       KeyConditionExpression=Key('Building').eq('MLC')
#       )
#   print(response)
#   for i in response['Items']:
#       print(i['Room Number'])
    response = table.scan()
#    request.session['buildings'] = response
    template = loader.get_template('website/index.html')
    context = {
        'buildings': response,
    }
    return HttpResponse(template.render(context, request))

def detail(request, building):
     dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")
     table = dynamodb.Table('SeatMonitor')
     response = table.query(                                                                                                    
         KeyConditionExpression=Key('Building').eq(building)
     )
     template = loader.get_template('website/detail.html')
     context = {
         'rooms': response,
     }
     return HttpResponse(template.render(context, request))
