from django.shortcuts import render
import boto3
from boto3.dynamodb.conditions import Key, Attr
from django.http import HttpResponse

# Create your views here.
def MLCView(request):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="https://dynamodb.us-east-1.amazonaws.com")
    table = dynamodb.Table('SeatMonitor')
    response = table.query(
        KeyConditionExpression=Key('Building').eq('MLC')
        )
    for i in response['Items']:
        print(i['Room Number'])
    return HttpResponse('Index Page Info')
