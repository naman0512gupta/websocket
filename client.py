from websocket import create_connection

def sendSocketMessage(message):
       ws = create_connection("ws://localhost:9090/chat")
       ws.send(message)
       ws.close()