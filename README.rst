
Typeform Python SDK
===================

A Python library for `TypeForm's new APIs <https://developer.typeform.com/get-started/>`__ (Create and Responses).

Currently only access via personal token is supported. OAuth2 support will be added in a later version.

Prerequisites
-------------

You will need to open a Typeform account and create a form. Once you have done this make a note of:
- a personal token (accessible from My account)
- a form ID (from the form url)

Installation
------------

This SDK requires either Python 2.7+ or 3.4+. To install you can use pip as follows:

.. code:: sh

    pip install typeform

Make sure to add it to your `requirements.txt` file. 


Getting Started
---------------

.. code:: py

    import typeform

    typeform = Typeform(personal_token='<your_personal_token>')

    # Fetch all your forms
    forms = typeform.forms.get()

    # Fetch a specific form
    form = typeform.form('<your_form_id>').get()

    # Print '<question>: <answer>' for all questions in a given form
    form = typeform.form('<your_form_id>').get()
    for question in my_form['fields']:
        print("{}".format(question['title']))

    # Delete a specific form
    typeform.form('<your_form_id>').delete()
    Fetch all responses for a given form
    my_responses = typeform.form('afaj').responses.get()

    # Print the number of responses to the form
    print("Responses: {}".format(len(my_responses['items'])))

    # Print '<question>: <answer>' for all responses to a given form
    for question in my_form['fields']:
    id = question['id']
    print("Question: {}".format(question['title']))
    for item in my_responses['items']:
        if item['answers']:
            for answer in item['answers']:
                if answer['field']['id'] == id:
                    if answer['type'] == 'boolean':
                        print("{}".format(answer['boolean']))
                    else:
                        print("{}".format(answer['number']))

List of Supported Endpoints
---------------------------

- Retrieve forms
.. code:: py

   typeform.forms.get()

- Retrieve specific form

.. code:: py

   typeform.form('uQaHwT').get()

- Delete specific form

.. code:: py

   typeform.form('uQaHwT').delete()

- Get responses

.. code:: py

   typeform.form('uQaHwT').responses.get()


Author
------

`Sam Heyman <https://samheyman.com>`__