import paho.mqtt.client as mqtt #import the client1
import time
import os
import random
from helpers import globals
from helpers import mqtt_callback
from helpers import mqtt_communication
from dotenv import load_dotenv
load_dotenv()

NAME_INDEX = 0
TOPIC_INDEX = 1

def choose_device():
	BASE_TOPIC = os.getenv("BASE_TOPIC")
	topic_list = BASE_TOPIC.split()
	topic_objects = [x.split(':') for x in topic_list]
	message = 'Choose device:\n'
	for num, topic in enumerate(topic_objects):
		message += '[{}] {}\n'.format(num, topic[NAME_INDEX])
	selected_device_index = int(input(message))
	device_topic = topic_objects[selected_device_index][TOPIC_INDEX]
	return device_topic

def connect_client():
	# Read from env
	HOST = os.getenv("HOST")
	PORT = os.getenv("PORT")
	USERNAME = os.getenv("USERNAME")
	PASSWORD = os.getenv("PASSWORD")

	broker_address=HOST
	broker_port = int(PORT)
	hash = str(random.getrandbits(128))
	print("creating new instance with id: {}".format(hash))
	client = mqtt.Client(hash) #create new instance

	client.username_pw_set(username=USERNAME,password=PASSWORD)
	client.on_connect = mqtt_callback.on_connect
	client.on_message = mqtt_callback.on_message #attach function to callback
	client.on_publish = mqtt_callback.on_publish
	print("connecting to broker")
	client.connect(broker_address, broker_port) #connect to broker
	return client

def main():
	globals.print_project_title()
	device_topic = choose_device()

	action = input('Choose the action:\n[0] Log\n[1] Listen Main topic\n[2] Power On\n[3] Power Off\n[4] Send value\n')
	action = int(action)
	LOG_TOPIC = os.getenv("LOG_TOPIC")
	client = connect_client()
	if action == 0:
		print("### Listening ###")
		mqtt_communication.listen_logs(client, LOG_TOPIC)
	elif action == 1:
		print("### Listening main topic ###")
		mqtt_communication.listen_main_topic(client, device_topic)
	elif action == 2:
		print("### Power on ###")
		mqtt_communication.powermode_change(client, device_topic, 1)
	elif action == 3:
		print("### Power off ###")
		mqtt_communication.powermode_change(client, device_topic, 0)
	elif action == 4:
		value = int(input('Insert value (between 1 and 255) :'))
		print("### Send value ###")
		mqtt_communication.send_value(client, device_topic, value)
	else:
		print("### Unknown action ###")


if __name__ == '__main__':
    main()