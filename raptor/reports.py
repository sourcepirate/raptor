import os
from jinja2 import Template
from .transform import TrasformPipeline
from .registry import datasource_registry, transformation_registry

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


def get_section(**kwargs):
    name = kwargs.get("name")
    description = kwargs.get("description")
    datasource = get_datasource(**kwargs.get("datasource"))

    return Section(
        name=name,
        description=description,
        datasource=datasource,
        transform=kwargs.get("transform"),
    )


def get_datasource(**kwargs):
    try:
        datasourceClass = datasource_registry.get(kwargs.pop("type"))
        ds = datasourceClass(**kwargs)
        return ds
    except KeyError:
        print("Type not found for datasource!")
        return None


def get_transform(**kwargs):
    try:
        transformRegistry = transformation_registry.get(kwargs.pop("type"))
        ds = transformRegistry(**kwargs)
        return ds
    except KeyError:
        print("Type not found for datasource!")
        return None


class Section(object):
    def __init__(
        self, name=None, description=None, datasource=None, transform=None
    ):
        self.name = name
        self.description = description
        self.datasource = datasource
        transforms = []
        for rule in transform:
            tRule = get_transform(**rule)
            transforms.append(tRule)
        self.transform = TrasformPipeline(transforms)

    def render(self):

        df = self.datasource.get_data()
        transformed_df = self.transform.transform(df)
        return {
            "section_title": self.name,
            "section_description": self.description,
            "body": transformed_df.to_html(),
        }


class Reports(object):
    def __init__(
        self,
        title=None,
        template=None,
        sender=None,
        receivers=None,
        sections=None,
    ):

        self._title = title
        self._sender = sender
        self.template = template
        self._receivers = receivers
        self._sections = []
        if sections:
            for section in sections:
                self._sections.append(get_section(**section))

    def render(self):

        path = os.path.join(BASE_PATH, "templates", f"{self.template}.j2")
        template = Template(open(path).read())

        section_values = []
        for section in self._sections:
            section_values.append(section.render())

        return template.render(sections=section_values)
