from django import forms

from furryFunnies.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image_url', 'content']

        labels = {
            'title': 'Title:',
            'image_url': 'Post Image URL:',
            'content': 'Content:',

        }


class PostAddForm(PostBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['placeholder'] = 'Put an attractive and unique title...'
        self.fields['title'].error_messages.update({
            'unique': 'Oops! That title is already taken. How about something fresh and fun?',
        })

        self.fields['image_url'].widget.attrs['helptext'] = 'Share your funniest furry photo URL!'

        self.fields['content'].widget.attrs[
            'placeholder'] = 'Share some interesting facts about your adorable pets...'

    # widgets = {
    #     'image': forms.TextInput(attrs={'helptext': 'Share your funniest furry photo URL!'}),
    #     'content': forms.Textarea(attrs={'placeholder': 'Share some interesting facts about your adorable pets...'}),
    # }
    # labels = {
    #     'title': 'Title:',
    #     'image': 'Post Image URL:',
    #     'content': 'Content:',
    #
    # }
    # error_messages = {
    #     'title': {
    #         'unique': 'Oops! That title is already taken. How about something fresh and fun?',
    #     }
    # }

