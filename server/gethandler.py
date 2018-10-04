import tornado.web
import opensourcelist
import json

class GetHandler(tornado.web.RedirectHandler):
    def initialize(self, softwarelist):
        self.softwarelist = softwarelist

    def get(self):
        self.write(self.softwarelist.json_list())
