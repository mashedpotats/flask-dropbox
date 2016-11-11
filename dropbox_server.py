import datetime

import dropbox
from dropbox.files import DeleteError


class DropboxServer:
    def __init__(self, token=None):
        self.dbx = dropbox.Dropbox(token)

    def write(self, filename, data):
        return self.dbx.files_upload(data, '/' + filename)

    def read(self):
        entries = []
        epoch = datetime.datetime.utcfromtimestamp(0)
        for entry in self.dbx.files_list_folder('').entries:  # retrieving names
            entrydict = {
                'modified': (entry.client_modified - epoch).total_seconds() * 1000,
                'name': entry.name,
                'size': entry.size
            }

            entries.append(entrydict)
        return entries  # return the array

    def delete(self, filename):
        try:
            self.dbx.files_delete('/' + filename)  # delete
            return 200
        except DeleteError:
            return 404

    def get_dropbox(self):
        return self.dbx
