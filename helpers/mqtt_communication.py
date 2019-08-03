def publish_message(client, topic, value):
	print("Publishing message to topic",topic)
	client.publish(topic, value)

def powermode_change(client, base_topic, value):
	publish_message(client, "{}/powermode".format(base_topic), value)

def send_value(client, base_topic, value):
	publish_message(client, "{}/value".format(base_topic), value)

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