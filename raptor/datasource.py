import pandas as pd


class DataSource(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def get_data(self):
        raise NotImplementedError


class URLSource(DataSource):
    def get_data(self):
        url = self.kwargs.get("url")
        return pd.read_csv(url)


class FileSource(DataSource):
    def get_data(self):
        fd = self.kwargs.get("file")
        return pd.read_csv(fd)
