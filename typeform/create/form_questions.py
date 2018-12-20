class FormQuestion(object):
    """TypeForm form question object"""
    __slots__ = ['_question_id', '_title', '_question_type']

    def __init__(self, id=None, title=None, type=None, ref=None, properties=None, validations=None):
        """Constructor for TypeForm form question"""
        self._question_id = id
        self._question_type = type
        self._title = title

    # @property
    # def field_id(self):
    #     """The field_id of the question"""
    #     return self._field_id

    # @property
    # def group(self):
    #     """The field_id of the question"""
    #     return self._group

    # @property
    # def _question_ref(self):
    #     """The id of the question"""
    #     return self._question_id

    @property
    def question_type(self):
        """The question type"""
        return self._question_type

    @property
    def title(self):
        """The question asked by this question"""
        return self._title

    def __repr__(self):
        return (
            'FormQuestion(question_id={question_id!r}, title={title!r}, question_type={question_type!r})'
            .format(question_id=self._question_id, title=self._title, question_type=self._question_type)
        )

class FormQuestions(object):
    """TypeForm form questions collection object"""
    __slots__ = ['_questions']

    def __init__(self, questions=None):
        """Constructor for TypeForm for responses collection object"""

        # Convert our questions input into a list of FormQuestion objects
        self._questions = []
        if questions:
            print("Number of questions: {}".format(len(questions)))
            self._questions = [
                FormQuestion(**question) for question in questions
            ]

    def get_question(self, id):
        """Get a specific question by id"""
        if not self.questions:
            return None

        for question in self.questions:
            if question.id == id:
                return question

    @property
    def stats(self):
        """Get the stats for the results"""
        return self._stats

    @property
    def questions(self):
        """The questions asked by this form"""
        return self._questions

    def __getitem__(self, idx):
        """Get a specific question by index"""
        return self.questions[idx]

    def __len__(self):
        """The number of questions"""
        return len(self.questions)

    def __iter__(self):
        """Iterator over the questions"""
        return iter(self.questions)

    def __repr__(self):
        return (
            'FormQuestions(questions={questions!r}'
            .format(questions=len(self.questions))
        )