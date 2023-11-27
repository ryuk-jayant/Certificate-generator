from django import forms
class StudentForm(forms.Form):
    # name=forms.CharField(initial="Name of candidate",max_length=20, required=True)
    # name.widget.attrs.update({'class':'m-3 py-3 px-10 bg-blue-400 rounded-lg text-gray-100'})
    # email=forms.EmailField(label="Email",initial="jayant@Example.com", max_length=50, required=True)
    # email.widget.attrs.update({"class":'m-3 py-3 px-10 bg-blue-400 rounded-lg text-gray-100'})
    file=forms.FileField(label="File", required=False)