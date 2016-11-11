import dropbox_server

token = ''

with open('token.txt', 'r')as f:
    global token
    token = f.read()

dbx = dropbox_server.DropboxServer(token=token)
