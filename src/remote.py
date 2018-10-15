import cherrypy

index_html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Slideshow</title>
    <style>
      html, body {
        font-family: sans-serif;
        text-align: center;
        background-color: #333;
        color: #ccc;
        margin: 0;
        padding: 0;
      }
      button {
        width: 100%;
        max-width: 768px;
        margin: auto;
        padding: 1rem;
        font-size: 3rem;
        border: none;
        border-bottom: 2px white solid;
        background-color: #333;
        color: #ccc;
      }
      a, a:visited {
        color: white;
      }
    </style>
  </head>
  <body>
    <div class="content">
      <h1>Slideshow</h1>
      <form action="/start" method = "POST">
        <button type="submit">Start/Update</button>
      </form>
      <form action = "/stop" method = "POST">
        <button type = "submit">Stop</button>
      </form>
      <p>Made using <a href="https://cherrypy.org/">cherry py</a> which is licensed<br />under the <a href="https://github.com/cherrypy/cherrypy/blob/master/LICENSE.md">BSD License</a></p>
    </div>
  </body>
</html>
"""

class Remote(object):
    def __init__(self, slideshow):
        self.slideshow = slideshow
    def run(self):
        cherrypy.config.update({'server.socket_host': '0.0.0.0'})
        cherrypy.quickstart(self)
    @cherrypy.expose
    def index(self):
        return index_html
    @cherrypy.expose
    def start(self):
        self.slideshow.start()
        raise cherrypy.HTTPRedirect('/')
    @cherrypy.expose
    def stop(self):
        self.slideshow.stop()
        raise cherrypy.HTTPRedirect('/')