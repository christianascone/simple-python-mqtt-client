import paho.mqtt.client as mqtt #import the client1
import time
import os
import random
from dotenv import load_dotenv
load_dotenv()

def on_connect(pahoClient, obj, flags, rc):
	# Once connected, publish message
    print("Connected Code = %d"%(rc))

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")


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
	client.on_connect = on_connect
	client.on_message=on_message #attach function to callback
	client.on_publish = on_publish
	print("connecting to broker")
	client.connect(broker_address, broker_port) #connect to broker
	return client

def powermode_change(client, base_topic, value):
	print("Publishing message to topic","{}/powermode".format(base_topic))
	client.publish("{}/powermode".format(base_topic), value)

def listen_logs(client, log_topic):
	try:
		print("Subscribing to topic",log_topic)
		client.subscribe(log_topic, qos=1)
		client.loop_forever()        #start the loop
	except KeyboardInterrupt:
		print("Exiting")
		client.disconnect()

def listen_main_topic(client, base_topic):
	try:
		print("Subscribing to topic", base_topic)
		client.subscribe(base_topic, qos=1)
		client.loop_forever()        #start the loop
	except KeyboardInterrupt:
		print("Exiting")
		client.disconnect()

def main():
	action = input('Choose the action:\n[0] Log\n[1] Power On\n[2] Power Off\n[3] Listen Main topic\n')
	action = int(action)
	BASE_TOPIC = os.getenv("BASE_TOPIC")
	LOG_TOPIC = os.getenv("LOG_TOPIC")
	client = connect_client()
	if action == 0:
		print("Listening")
		listen_logs(client, LOG_TOPIC)
	elif action == 1:
		print("Power on")
		powermode_change(client, BASE_TOPIC, 1)
	elif action == 2:
		print("Power off")
		powermode_change(client, BASE_TOPIC, 0)
	elif action == 3:
		print("Listening main topic")
		listen_main_topic(client, BASE_TOPIC)
	else:
		print("Unknown action")


if __name__ == '__main__':
    main()