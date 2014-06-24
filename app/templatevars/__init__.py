from .. import requests
from . bodyclass import BodyClass
from . pagetitle import PageTitle


def parse(request):
    return TemplateVariableParser().parse(request)


class TemplateVariableParser:

    def __init__(self):
        self.templatevars = {}

    def set(self, name, value):
        self.templatevars[name] = value

    def parse(self, request):
        self._parse_request(request)
        self._parse_templatevars()
        return self.templatevars

    def _parse_request(self, request):
        parsed_request = requests.parse(request)
        parsed_request['form'] = request.form
        self.templatevars.update(parsed_request)

    def _parse_templatevars(self):
        segments = self.templatevars.get('uri_segments')[:]
        self._set_page_title(segments)
        self._set_body_class(segments)

    def _set_page_title(self, segments):
        page_title = PageTitle().get(segments)
        self.set('page_title', page_title)

    def _set_body_class(self, segments):
        body_class = BodyClass().get(segments)
        self.set('body_class', body_class)