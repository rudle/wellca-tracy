from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import mail
from waveapi import events
from waveapi import model
from waveapi import robot
import cgi
import re

def OnRobotAdded(properties, context):
  root_wavelet = context.GetRootWavelet()
  root_wavelet.CreateBlip().GetDocument().SetText("Hey now!")

def OnBlipSubmitted(properties, context):

  blipId = properties['blipId']
  blip = context.GetBlipById(blipId) #OpBasedBlip

  if blip:
    doc = blip.GetDocument() # OpBasedDocument

    ticketRe = re.compile('(?:.*?)#([0-9]+)*')
    revRe = re.compile('(?:.*?)r([0-9]+)*')

    text = doc.GetText()
    while (True):
      ticketMatch = ticketRe.match(text)

      if ticketMatch:
        ticketId = ticketMatch.group(1)
        doc.AppendText("\n\nhttp://wellington.well.lan/trac/ticket/" + ticketId)
        text = text.lstrip(ticketMatch.group(0))
      else:
        break;

    text = doc.GetText()
    while (True):
      revMatch = revRe.match(text)
      if revMatch:
        revId = revMatch.group(1)
        doc.AppendText("\n\nhttp://wellington.well.lan/trac/changeset/" + revId)
        text = text.lstrip(revMatch.group(0))
      else:
        break;

  else:
    root_wavelet = context.GetRootWavelet()
    root_wavelet.CreateBlip().GetDocument().SetText("No blip found :(")
    logging.info( 'No blip found at %s' % blipId)


def main():
  myRobot = robot.Robot('wellca-tracy',
      image_url='http://wellca-tracy.appspot.com/well.gif', 
      version=1,
      profile_url='http://wellca-tracy.appspot.com/')
  myRobot.RegisterHandler(events.BLIP_SUBMITTED, OnBlipSubmitted)
  myRobot.RegisterHandler(events.WAVELET_SELF_ADDED, OnRobotAdded)
  myRobot.Run()

if __name__ == "__main__":
  main()


def mail(message):
  message = mail.EmailMessage(sender="Example <seansorrell@gmail.com>",
                            subject="Your account has been approved")

  message.to = "Sean <seansorrell@gmail.com>"
  message.body = message

  message.send
