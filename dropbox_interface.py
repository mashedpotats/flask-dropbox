# TODO Possibly change from using non-classes since I can only save JSON values to sessions. Any advice is welcome.

import dropbox


def get_content(token, path):
    dbx = dropbox.Dropbox(token)
    print 'received', token, path
    return str(dbx.files_list_folder(path).entries)