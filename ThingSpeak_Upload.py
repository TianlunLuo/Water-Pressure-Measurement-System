from __future__ import print_function
import paho.mqtt.publish as publish
import psutil

###   Start of user configuration   ###

#  ThingSpeak Channel Settings
def connect_to_thingspeak(depth,pressure):
    # The ThingSpeak Channel ID
    # Replace this with your Channel ID
    channelID = "232016"

    # The Write API Key for the channel
    # Replace this with your Write API key
    apiKey = "OXAHWJTOL4FA8ATC"

    #  MQTT Connection Methods

    # Set useUnsecuredTCP to True to use the default MQTT port of 1883
    # This type of unsecured MQTT connection uses the least amount of system resources.
    useUnsecuredTCP = False

    # Set useUnsecuredWebSockets to True to use MQTT over an unsecured websocket on port 80.
    # Try this if port 1883 is blocked on your network.
    useUnsecuredWebsockets = False

    # Set useSSLWebsockets to True to use MQTT over a secure websocket on port 443.
    # This type of connection will use slightly more system resources, but the connection
    # will be secured by SSL.
    useSSLWebsockets = True

    ###   End of user configuration   ###

    # The Hostname of the ThinSpeak MQTT service
    mqttHost = "mqtt.thingspeak.com"

    # Set up the connection parameters based on the connection type
    if useUnsecuredTCP:
        tTransport = "tcp"
        tPort = 1883
        tTLS = None

    if useUnsecuredWebsockets:
        tTransport = "websockets"
        tPort = 80
        tTLS = None

    if useSSLWebsockets:
        import ssl
        tTransport = "websockets"
        tTLS = {'ca_certs':"/etc/ssl/certs/ca-certificates.crt",'tls_version':ssl.PROTOCOL_TLSv1}
        tPort = 443

    tPayload = "&field1=" + str(depth) + "&field2=" + str(pressure)

    # Create the topic string
    topic = "channels/" + channelID + "/publish/" + apiKey
    try:
        publish.single(topic, payload=tPayload, hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)
    except:
        print ("There was an error while publishing the data.")
