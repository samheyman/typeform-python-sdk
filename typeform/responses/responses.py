# from .typeform import Client
# from .errors import NotFoundException
# from .form_response import FormResponses
from typeform.create.form_questions import FormQuestions
from typeform.create.form_questions import FormQuestions
from typeform.utils.client import Client

class Responses(object):
    """TypeForm Form API client"""
    def __init__(self, client, form_id):
        """Constructor for TypeForm Form API client"""
        self.client = client
        self.form_id = form_id

    def get(self):
        """Get all responses for this TypeForm Form"""
        return self.client._request('GET', '/' + self.form_id + '/responses')

        raise NotFoundException('Typeform client could not find form {form_id!r}'.format(form_id=form_id))
