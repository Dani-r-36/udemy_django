from django import forms
from .models import BlogPost
from .models import Comment

class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','image', 'slug', 'content', 'publish_date']

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title__iexact=title) #__iexact catches same regardless of casing
        if instance is not None:
            qs = qs.exclude(pk=instance.pk) #id = instance.id
        if qs.exists():
            raise forms.ValidationError("This title has already been used")
        return title
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']