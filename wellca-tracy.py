from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import mail
from waveapi import events
from waveapi import model
from waveapi import robot
import cgi


def OnRobotAdded(properties, context):
  root_wavelet = context.GetRootWavelet()
  root_wavelet.CreateBlip().GetDocument().SetText("REMEMBER ME")

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
  myRobot.RegisterHandler(events.WAVELET_SELF_ADDED, OnRobotAdded)
  run_wsgi_app(application)

if __name__ == "__main__":
  main()


def mail(message):

  message = mail.EmailMessage(sender="Example <seansorrell@gmail.com>",
                            subject="Your account has been approved")

  message.to = "Sean <seansorrell@gmail.com>"
  message.body = message

  message.send