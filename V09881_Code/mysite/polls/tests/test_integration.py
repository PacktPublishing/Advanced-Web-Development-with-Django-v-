from django.test import TestCase
from django.test import Client

from django.urls import reverse

from model_mommy import mommy


class TestVoteViewIntegration(TestCase):
    def setUp(self):
        self.client = Client()
        self.question_model = mommy.make('polls.Question')
        self.choice_models = mommy.make(
            'polls.Choice',
            question=self.question_model,
            _quantity=3)

    def test_post_success(self):
        choice = self.choice_models[0]
        response = self.client.post(
            reverse(
                'polls:vote_result',
                kwargs={'pk': choice.question.id}
            ),
            {'choice': choice.id},
            follow=True
        )
        self.assertIn(302, response.redirect_chain[0])
        self.assertTemplateUsed(response, 'polls/results.html')

    def test_post_failure(self):
        choice = self.choice_models[0]
        response = self.client.post(
            reverse(
                'polls:vote_result',
                kwargs={'pk': choice.question.id}
            ),
            follow=True
        )
        self.assertIn(302, response.redirect_chain[0])
        self.assertTemplateUsed(response, 'polls/detail.html')
