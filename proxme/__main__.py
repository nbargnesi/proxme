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


content = {
    'proxy': '127.0.0.1:1080'
}


class Handler(tornado.web.RequestHandler):
    def get(self, path, **kwargs):
        path = './' + path
        self.set_header('Content-Type', X_NS_PROXY_AUTOCONFIG)

        if not os.path.isfile(path):
            self.render('template.pac', content=content)
            return

        with open(path) as fh:
            self.write(fh.read())

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r"/(.*)", Handler),
    ], autoreload=True)
    app.listen(sys.argv[1])
    tornado.ioloop.IOLoop.current().start()
