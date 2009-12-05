from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import cgi
from google.appengine.api import mail

class MainPage(webapp.RequestHandler):
  def get(self):
    self.response.out.write("""
          <html>
            <body>
              <form action="/sign" method="post">
                <div><textarea name="content" rows="3" cols="60"></textarea></div>
                <div><input type="submit" value="Sign Guestbook"></div>
              </form>
            </body>
          </html>""")


  def post(self):
    self.response.out.write('<html><body>You wrote:<pre>')
    self.response.out.write(cgi.escape(self.request.get('content')))
    self.response.out.write('</pre></body></html>')

application = webapp.WSGIApplication( [('/.*', MainPage)],
                                      debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()


def mail(message):

  message = mail.EmailMessage(sender="Example <seansorrell@gmail.com>",
                            subject="Your account has been approved")

  message.to = "Sean <seansorrell@gmail.com>"
  message.body = message

  message.send
