import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AvrKKyMhXupFKm3xis9ZZDU1eJFuZYN8Fjy8a8XdcvqrMPce2eC9YYG7LlNoTaAz10QvBrormWUnUhP8xRM8Fom_-TEkkBfW40DRUTApbv3EdkRqL3vWn9hCw9SM-JlICpbHIpo'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to DropBox: ")

    transferDate.upload_file(file_from, file_to)
    print("file has been moved and to dropbox")

main()