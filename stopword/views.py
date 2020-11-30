from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from .models import StopWord
from .forms import AddStopWordForm
from .serializers import StopWordSerializer

def add_stopword(request):
    if request.method == 'POST':
        form = AddStopWordForm(request.POST)
        if form.is_valid():
            stopword = form.save()
            print(StopWord.objects.all())
            return redirect('stopword:add_stopword')
    else:
        form = AddStopWordForm()
    return render(request, 'stopword/stopword_form.html', {'form': form,})

class StopWordViewset(ModelViewSet):
    
    queryset = StopWord.objects.all().order_by('-id')
    serializer_class = StopWordSerializer