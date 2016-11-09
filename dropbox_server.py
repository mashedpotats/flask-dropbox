# TODO Possibly change from using non-classes since I can only save JSON values to sessions. Any advice is welcome.

import dropbox


class DropboxServer:
    dbx = None

    def __init__(self, token=None):
        self.set_token(token)

    def set_token(self, token):
        dbx = dropbox.Dropbox(token)

    def create(self, filename, data):
        if self.dbx is not None:
            return self.dbx.files_upload(data, '/' + filename)

    def read(self):
        if self.dbx is not None:
            return self.dbx.files_list_folder('')

    def update(self, filename, data):  # to be clear. but they act the same
        self.create(filename, data)

    def delete(self, filename):
        if self.dbx is not None:
            return self.dbx.files_delete('/' + filename)
