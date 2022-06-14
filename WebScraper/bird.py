import messagebird
# client = messagebird.Client("wRAF3IFqjdlMyNLSBeulol67i")
# try:
#     msg = client.voice_message_create('+447944633730', 'hey you', {'voice' : 'male'})
#     print(msg.__dict__)
# except messagebird.client.ErrorException as e:
#     for error in e.errors:
#         print(error)

client = messagebird.Client("0SLPuvmvLSueTwgEXsSRABBNI")
try:
    message = client.message_create(
          'TestMessage',
          '+989212469161',
          'This is a test message',
          { 'reference' : 'Foobar' }
      )
except messagebird.client.ErrorException as e:
    for error in e.errors:
        print(error)
