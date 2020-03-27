import tornado.ioloop
import tornado.web
import logging
import rethinkdb as rdb
from tornado import gen
from tornado.ioloop import IOLoop
from tornado import httpserver
from handlers.base import setup_db,MY_HOST,MY_DB
# from tornado.web import StaticFileHandler

r = rdb.RethinkDB()

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class StudentHandler(tornado.web.RequestHandler):
    # @gen.coroutine
    async def post(self):
        data = tornado.escape.json_decode(self.request.body)
        x = await r.table('student').insert(data["student"],return_changes=True).run(time_format="raw")
        data = x['changes'][0]["new_val"]
        self.write(dict(student = data))  
    # @gen.coroutine
    async def get(self):
        data = await r.table('student').order_by('name').run(time_format="raw")
        self.write(dict(student=data))

class StudentHandlers(tornado.web.RequestHandler):
    @gen.coroutine
    def put(self, id):
        data = tornado.escape.json_decode(self.request.body)
        data = data["student"]
        data = yield r.table('student').get(id).update(data).run(time_format="raw")
        self.write(dict(student = data))
    @gen.coroutine
    def delete(self, id):
        data = yield r.table('student').get(id).delete().run(time_format="raw")
        self.write(dict(student = data))

class AppStaticHandler(tornado.web.StaticFileHandler):
    def write_error(self, status_code, **kwargs):
        # errors = [403, 404, 500, 503]
        if status_code in [404]:
            with open("./dist/index.html") as f:
                self.write(f.read())
        else:
            self.write("Unknown Error %s" % status_code)

# class ListHandler(tornado.web.RequestHandler):

    # # @gen.coroutine
    # async def get(self):
    #     self.set_header('Content-Type', 'text/html')
    #     with open("./dist/index.html") as f:
    #         self.write(f.read())
    
class EnrollApp(tornado.web.Application):
    def __init__(self, conn):
        handlers = [
            (r"/", IndexHandler),
            (r"/students", StudentHandler),
            (r"/students/(\S+)", StudentHandlers),
            # (r"/(list)", ListHandler),
            (r"/(.*)", AppStaticHandler, {'path': "./dist/"}),
            # (r"/user", UserHandler),
            (r"/assets/(.*)", tornado.web.StaticFileHandler, {
                'path' : 'dist/assets'
            })
        ]
        settings = dict(
            debug=True,
            template_path="dist",
        )
        self.conn = conn
        tornado.web.Application.__init__(self, handlers, **settings)

# @gen.coroutine
async def main():
    todo_tables = ["student"]
    setup_db(todo_tables)
    r.set_loop_type('tornado')
    conn = (await r.connect(MY_HOST, db=MY_DB)).repl()
    http_server = httpserver.HTTPServer(EnrollApp(conn))
    http_server.listen(8889)

if __name__ == "__main__":
    IOLoop.current().run_sync(main)
    IOLoop.current().start()