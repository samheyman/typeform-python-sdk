from typeform import Typeform


typeform = Typeform(personal_token='xgHiVsz2fK4p4Tgg947WEcJBhvt76yfsachrz1qMxZf')
# tf2 = typeform.Client(personal_token='xgHiVsz2fK4p4Tgg947WEcJBhvt76yfsachrz1qMxZf')

#    typeform.forms.form('asfa').get()

# Fetch all questions from the form
all_forms = typeform.forms.get()
my_form = typeform.form('tqOCMu').get()

# my_form = typeform.form('fYvzZN').delete()
my_responses = typeform.form('tqOCMu').responses.get()

# Fetch all responses to the form with default options
# responses = forms.get_responses()

# Fetch responses with specific options
#responses = form.get_responses(limit=10, since=1487863154)

print("Forms:")
print(all_forms)
print("Questions:")

for question in my_form['fields']:
    print("{}".format(question['title']))

print("Responses: {}".format(len(my_responses['items'])))

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

print("My responses")
# print(my_responses)
# for question in questions:
#     print("{} ({})".format(question.title, question.question_type))

# Print '<question>: <answer>' for all responses to this form
# for response in responses:
#     for answer in response.answers:
#         print('{question}: {answer}'.format(question=answer.question, answer=answer.answer))

# Fetch a specific response
#response = form.get_response('<response_token>')
