import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
   print ("[+] Listo")
   client.subscribe('#', qos = 1)        # Suscribimos todos los topicos
   client.subscribe('$SYS/#')            # Estadisticas broker

def on_message(client, userdata, msg):
   print ('[+] Topic: %s - Mensaje: %s' % (msg.topic, msg.payload))

client = mqtt.Client(client_id = "s4p0")
client.on_connect = on_connect
client.on_message = on_message
client.connect('167.71.210.68', 1883, 60)
client.loop_forever()
