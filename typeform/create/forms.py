# from .errors import NotFoundException
# from .form_response import FormResponses
from typeform.create.form_questions import FormQuestions
from typeform.utils.client import Client


class Forms(object):
    """TypeForm Form API client"""
    def __init__(self, client):
        """Constructor for TypeForm Form API client"""
        self.client = client
        print("{} created".format(self))

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
        return self.client._request('GET', '')

    # def __repr__(self):
    #     return (
    #         'Forms(total_items={total_items!r}, page_count={page_count!r}, items={items!r})'
    #         .format(total_items=self.total_items, page_count=self.page_count, items=self.items)
    #     )
