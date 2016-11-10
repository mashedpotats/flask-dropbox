import dropbox_server

TOKEN = 'mfcRgIwx6aAAAAAAAAAAWhRuPZRpiGb9bHNNDzudgYyMZr-MDae0eOMjxYD6hyJd'
dbx = dropbox_server.DropboxServer(token=TOKEN)

print dbx.read()
