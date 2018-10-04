import tornado.web
import opensourcelist
import json

class AddHandler(tornado.web.RedirectHandler):
    def initialize(self, softwarelist):
        self.softwarelist = softwarelist

    def get(self):
        name = self.get_argument('name')
        short_description = self.get_argument('short_description')
        site = self.get_argument('site')
        self.softwarelist.add_OpenSourceSoftware(name=name,short_description=short_description,site=site)
