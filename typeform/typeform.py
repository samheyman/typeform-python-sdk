from .utils.client import Client
from .utils.errors import (NotAuthorizedException, NotFoundException, InvalidRequestException,
                     RateLimitException, UnknownException)
from .create.forms import Forms
from .create.form import Form
from .utils.errors import TypeFormException

class Typeform(Forms, Client, object):
    """TypeForm API client"""

    def __init__(self, personal_token):
        """Constructor for TypeForm API client"""
        self.client = Client(personal_token)
        self.forms = Forms(self.client)

    def form(self, form_id):
        return Form(self.client, form_id)
