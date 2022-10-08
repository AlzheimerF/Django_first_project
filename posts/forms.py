from django import forms

class PostForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data  # dict {}
    #     print(cleaned_data)
    #     title = cleaned_data.get('title')
    #     print(title)
    #     if title.lower().strip() == 'tree':
    #         raise forms.ValidationError("This title already exist!")
    #     return title
    #
    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')
        print(title)
        if title and description:
            if title.lower().strip() == 'tree':
                self.add_error('title', "This title already exist!")
        # if 'hey' in description or 'hey' in title:
        #     self.add_error('description', "This desc. is not a correct !")
            if 'Python is not the best language' in description:
                self.add_error('description', "This is a bullshit ! ")
        return cleaned_data





