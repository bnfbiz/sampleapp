import tornado.ioloop
import tornado.web
from opensourcelist import OpenSourceSoftware
from addhandler import AddHandler
from delhandler import DelHandler
from gethandler import GetHandler

softwarelist = OpenSourceSoftware()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("OpenSource Software API v1")

def make_app():
    return tornado.web.Application([
        (r"/v1",MainHandler),
        (r"/v1/add_OpenSourceSoftware",AddHandler, dict(softwarelist = softwarelist)),
        (r"/v1/delete_OpenSourceSoftware",DelHandler, dict(softwarelist = softwarelist)),
        (r"/v1/list",GetHandler, dict(softwarelist = softwarelist))
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    