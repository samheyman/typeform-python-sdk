# from .typeform import Client
# from .errors import NotFoundException
# from .form_response import FormResponses
from .form_questions import FormQuestions
from typeform.create.form_questions import FormQuestions
from typeform.utils.client import Client
from .responses import Responses

class Form(object):
    """TypeForm Form API client"""
    def __init__(self, client, form_id):
        """Constructor for TypeForm Form API client"""
        self.client = client
        self.form_id = form_id
        self.responses = Responses(client, form_id)

    def _get_params(self, **kwargs):
        """Helper to normalize query string parameters for our request"""
        params = dict()

        # Boolean params
        for name in ('completed', ):
            value = kwargs.get(name)
            if value is not None:
                params[name] = 'true' if value else 'false'

        # Number params
        for name in ('limit', 'since', 'offset', 'until'):
            value = kwargs.get(name)
            if value is not None:
                params[name] = int(value)

        # Order by
        if 'order_by' in kwargs:
            order_by = kwargs['order_by']
            if order_by is not None:
                if ',' in order_by:
                    params['order_by[]'] = order_by
                else:
                    params['order_by'] = order_by

        # Token
        if 'token' in kwargs:
            params['token'] = kwargs['token']

        return params

    def get(self):
        """Get the requested TypeForm Form"""
        return self.client._request('GET', '/' + self.form_id)

        raise NotFoundException('Typeform client could not find form {form_id!r}'.format(form_id=form_id))

    def delete(self):
        """Get all questions for this TypeForm Form"""
        return self.client._request('DELETE', '/' + self.form_id)

        raise NotFoundException('Typeform client could not find form {form_id!r}'.format(form_id=form_id))

    def get_responses(self, token=None, completed=None, since=None, until=None, offset=None, limit=None, order_by=None):
        """Get a list of responses for this TypeForm Form"""
        params = self._get_params(
            completed=completed,
            limit=limit,
            offset=offset,
            order_by=order_by,
            since=since,
            until=until,
            token=token,
        )

        resp = self._request('GET', 'responses', params=params)
        print("Responses: {}".format(resp))
        return FormResponses(stats=resp.get('stats'), responses=resp.get('responses'), questions=resp.get('questions'))
        raise NotFoundException('Typeform client could not retrieve answers for form {form_id!r}'.format(form_id=form_id))

    def get_response(self, token):
        """Get a specific response for this TypeForm Form"""
        responses = self.get_responses(token=token)
        # Check truthy *and* length since this is a class, not a list
        if responses and len(responses) == 1:
            return responses[0]

        raise NotFoundException('typeform client could not find response with token {token!r}'.format(token=token))

    # def __repr__(self):
    #     return (
    #         'Forms(total_items={total_items!r}, page_count={page_count!r}, items={items!r})'
    #         .format(total_items=self.total_items, page_count=self.page_count, items=self.items)
    #     )
