from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import mail
from waveapi import events
from waveapi import model
from waveapi import robot
import cgi
import urllib
import re

def well_send_mail(message_text):
  message = mail.EmailMessage(sender="From Wave <seansorrell@gmail.com>", subject="Bug filed from Wave")
  message.to = "Noone <email@example.com>"
  message.body = message_text
  message.send()


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
    mailRe = re.compile('(?:.*?)mail\:\<(.*)\>', re.DOTALL)

    text = doc.GetText()

    newText = re.sub('#([0-9]+)', r'ticket \1 : http://wellington.well.lan/trac/ticket/\1' , text)
    newText = re.sub('r([0-9]+)', r'rev \1 : http://wellington.well.lan/trac/changeset/\1' , newText) # I acknowledge that this is gross

    while (True):
      mailMatch = mailRe.match(newText)
      if mailMatch:
        message_text = mailMatch.group(1)
        well_send_mail(message_text)
        newText = re.sub('mail\:\<(.*)\>', r'bug filed: http://wellington.well.lan/trac/search?q=' + urllib.quote(message_text), newText)
      else:
        break;

    if newText != text:
      doc.SetText(newText)

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


