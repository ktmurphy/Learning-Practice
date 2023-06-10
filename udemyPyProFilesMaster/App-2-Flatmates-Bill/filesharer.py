import filestack
class FileSharer():
    
    def __init__(self, filepath, api_key = 'A7kSwE3PJS1Ohv73mVAfRz'):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = filestack.Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url