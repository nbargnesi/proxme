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
from optparse import OptionParser

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


def main():
    app = tornado.web.Application([
        (r"/(.*)", Handler),
    ], autoreload=True)
    tornado.log.enable_pretty_logging()
    if len(sys.argv) == 1:
        address = '127.0.0.1'
        port = 8888
    elif len(sys.argv) == 3:
        address = sys.argv[1]
        port = sys.argv[2]
    else:
        raise RuntimeError('invalid arguments')


    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(port, address=address)
    print('Listening on %s:%d; ready for requests.' % (address, port))

    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()