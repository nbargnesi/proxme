# coding: utf-8
"""Proxme main."""
import os
import sys
import proxme
import proxme.lib
import tornado
import tornado.options
import tornado.web
import tornado.ioloop

X_NS_PROXY_AUTOCONFIG = 'application/x-ns-proxy-autoconfig'


class Handler(tornado.web.RequestHandler):
    def get(self, path, **kwargs):
        path = './' + path
        if not os.path.isfile(path):
            self.set_status(404)
            return
        self.set_header('Content-Type', X_NS_PROXY_AUTOCONFIG)
        with open(path) as fh:
            self.write(fh.read())

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/(.*)", Handler),
    ], autoreload=True)
    app.listen(sys.argv[1])
    tornado.ioloop.IOLoop.current().start()
