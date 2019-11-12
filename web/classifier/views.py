import hashlib
from django.shortcuts import render
from django.views import View


class HomeView(View):
    """Render order confirmation data and associated tools.
    """
    template_name = 'index.html'

    def get(self, request, word=None):
        hashable = 'Hellow Werld'
        if word:
            hashable = word
        unique_hash = hashlib.md5(hashable.encode('utf-8')).hexdigest()
        ctx = {
            'stuff': [
                {'name': 'Hellow', 'value': 'Werld'},
                {'name': 'hashed hellow werld', 'value': unique_hash},
            ]
        }
        return render(request, self.template_name, ctx)

