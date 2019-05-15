from django.test import TestCase
from django.test import RequestFactory

from model_mommy import mommy

from polls.views import VoteView
from polls.models import Choice


class TestVoteView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.question_model = mommy.make('polls.Question')
        self.choice_models = mommy.make(
            'polls.Choice',
            question=self.question_model,
            _quantity=3)

    def test_get_queryset(self):
        choice = self.choice_models[0]
        view = VoteView()
        queryset = view.get_queryset(choice.pk)
        self.assertEquals(queryset.choice_text, choice.choice_text)

    def test_post_votes(self):
        choice = self.choice_models[1]
        votes = choice.votes + 1
        request = self.factory.post(
            '/some-fake/url/',
            data={'choice': choice.id}
        )
        view = VoteView.as_view()
        response = view(request, pk=choice.question.id)
        new_votes = Choice.objects.get(pk=choice.id).votes
        self.assertEquals(votes, new_votes)

    def test_post_redirects_on_fail(self):
        choice = self.choice_models[2]
        request = self.factory.post(
            '/some-fake/url/',
            data={'choice': 500}
        )
        view = VoteView.as_view()
        response = view(request, pk=choice.question.id)
        self.assertEquals(response.status_code, 302)
