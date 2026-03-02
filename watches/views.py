def watch_detail(request, pk):
from django.shortcuts import render, redirect, get_object_or_404
from .models import Watch
from .forms import WatchForm


def watch_list(request):
    """View to display list of watches"""
    watches = Watch.objects.all()
    context = {
        'watches': watches
    }
    return render(request, 'watches/watch_list.html', context)


def watch_detail(request, pk):
    """View to display watch details"""
    watch = get_object_or_404(Watch, pk=pk)
    context = {
        'watch': watch
    }
    return render(request, 'watches/watch_detail.html', context)


def add_watch(request):
    """Add a new watch via a simple form"""
    if request.method == 'POST':
        form = WatchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('watches:watch_list')
    else:
        form = WatchForm()
    return render(request, 'watches/watch_add.html', {'form': form})
