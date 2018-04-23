import RPi.GPIO as GPIO
import spidev
import time
import boto3
from boto3.dynamodb.conditions import Key, Attr

GPIO.setmode(GPIO.BCM)

PORT = 0
DEVICE0 = 0
DEVICE1 = 1
START_BYTE = 1
SEND_BYTE = 128
CHAN_IN0 = 0
CHAN_IN1 = 1
HALF_BYTE_SHIFT = 4
NONE = 0
AND_FACTOR = 3
RECEIVE_FACTOR = 256
MIN_RESPONSE_VALUE = 30

spi = spidev.SpiDev()
spi.open(PORT, DEVICE0)
spi.open(PORT, DEVICE1)
dynamodb = boto3.resource('dynamodb', region_name='us-east-2', endpoint_url="https://dynamodb.us-east-2.amazonaws.com")
table = dynamodb.Table('StudyRoom')

print ("Pin0 : Pin1")

while True:
	try:
		response0 = spi.xfer2([START_BYTE, SEND_BYTE + (CHAN_IN0 << HALF_BYTE_SHIFT), NONE])
		response1 = spi.xfer2([START_BYTE, SEND_BYTE + (CHAN_IN0 << HALF_BYTE_SHIFT), NONE])

		value0 = (response0[1] & AND_FACTOR) * RECEIVE_FACTOR + response0[2]
		value1 = (response1[1] & AND_FACTOR) * RECEIVE_FACTOR + response1[2]
                
		if value0 > MIN_RESPONSE_VALUE or value1 > MIN_RESPONSE_VALUE:
			print(" {:^5d} / {:^5d} ".format(value0, value1))
			print("Unavailable")
			table.put_item(
				Item={
					'Building': 'MLC',
					'RoomNumber': 101,
					'Available': 0
				}
			)
		else:
			table.put_item(
				Item={
					'Building': 'MLC',
					'RoomNumber': 101,
					'Available': 1
				}
			)
			print("Available")
		time.sleep(2)
	except KeyboardInterrupt:
		spi.close()
		GPIO.cleanup();
