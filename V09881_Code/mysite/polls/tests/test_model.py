from django.test import TestCase

from model_mommy import mommy


class TestQuestion(TestCase):
    def setUp(self):
        self.models = mommy.make('polls.Question')

    def test_str(self):
        #https://docs.djangoproject.com/en/2.0/topics/testing/tools/#assertions
        self.assertEquals(str(self.models), self.models.question_text)

    def test_question_and_date(self):
        self.assertTrue(self.models.question_text in self.models.question_and_date())


class TestChoice(TestCase):
    def setUp(self):
        self.models = mommy.make('polls.Choice')

    def test_str(self):
        self.assertEquals(str(self.models), self.models.choice_text)

    def test_add_vote(self):
        current_votes = self.models.votes
        self.models.add_vote()
        new_votes = current_votes + 1
        self.assertEquals(self.models.votes, new_votes)
