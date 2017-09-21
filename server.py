import tornado.ioloop
import tornado.web
import tornado.websocket

clients = []

class IndexHandler(tornado.web.RequestHandler):
  @tornado.web.asynchronous
  def get(request):
    request.render("Rajesh")

class WebSocketChatHandler(tornado.websocket.WebSocketHandler):

  def check_origin(self, origin):
        return True
        
  def open(self, *args):
    clients.append(self)

  def on_message(self, message):
    if message[-4:] == "pass": #just a security check to ignore the message if it does not end with 'pass'
      for client in clients:
  		  client.write_message(message[:-4])
        
  def on_close(self):
  	clients.remove(self)

def run_server():
  app = tornado.web.Application([(r'/chat', WebSocketChatHandler), (r'/', IndexHandler)])
  app.listen(9090)
  tornado.ioloop.IOLoop.instance().start()