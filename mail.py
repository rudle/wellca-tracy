from google.appengine.api import mail

message = mail.EmailMessage(sender="Example <seansorrell@gmail.com>",
                            subject="Your account has been approved")

message.to = "Sean <seansorrell@gmail.com>"
message.body = """
Dear Albert:

Your example.com account has been approved.  You can now visit
http://www.example.com/ and sign in using your Google Account to
access new features.

Please let us know if you have any questions.

The example.com Team
"""

if message.is_initialized():
  print 'sending'
  print message.send()

print message
