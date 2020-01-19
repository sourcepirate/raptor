from .datasource import DataSource, FileSource, URLSource
from .transform import TransformMixin, GroupBy, Pivot


class BaseRegistry(object):
    def __init__(self, _type):
        self.__registry = {}
        self._type = _type

    def get(self, ds_type):
        return self.__registry.get(ds_type)

    def register(self, ds_type, dobj):
        if dobj == self._type:
            raise Exception("UnImplemented Register")
        self.__registry[ds_type] = dobj


class DataSourceRegistry(BaseRegistry):
    def __init__(self):
        super(DataSourceRegistry, self).__init__(DataSource)


class TransformRegistry(BaseRegistry):
    def __init__(self):
        super(TransformRegistry, self).__init__(TransformMixin)


datasource_registry = DataSourceRegistry()
datasource_registry.register("url", URLSource)
datasource_registry.register("file", FileSource)
transformation_registry = TransformRegistry()
transformation_registry.register("groupby", GroupBy)
transformation_registry.register("pivot", Pivot)
