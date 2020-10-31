from django import forms


class ToDoForm(forms.Form):
    text = forms.CharField(max_length=40,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Enter todo e.g. Complete Django',
                                      'aria-label': 'Todo', 'aria-describedby': 'add-btn'}
                           ))
