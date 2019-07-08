from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse

from posts.models import Post


class PostForm(forms.ModelForm):
    key = forms.CharField()

    class Meta:
        model = Post
        exclude = ('created',)

    def clean_key(self):
        if settings.POST_KEY != self.data.get('key'):
            raise ValidationError('Wrong key')


def create(request: WSGIRequest) -> JsonResponse:
    form = PostForm(request.GET or request.POST)
    if form.is_valid():
        post = form.save()
        return JsonResponse({'id': post.id}, status=201)
    else:
        return JsonResponse(form.errors, status=400)
