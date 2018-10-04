import tornado.web
import opensourcelist
import json

class DelHandler(tornado.web.RedirectHandler):
    def initialize(self, softwarelist):
        self.softwarelist = softwarelist

    def get(self):
        name = self.get_argument('name')
        result = self.softwarelist.delete_OpenSourceSoftware(name)
        if result:
            self.write("Deleted OpenSource Software name: {0} successfully".format(name))
            self.set_status(200)
        else:
            self.write("OpenSource Software '{0}' not found".format(name))
            self.set_status(404)
