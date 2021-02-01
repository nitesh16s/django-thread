import time
import threading
from django.contrib import messages
from django.shortcuts import redirect, render
from myapp.models import Uploads
from myapp.forms import UploadForm


def index(request):
    return render(request, 'myapp/index.html')


def upload1(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            images = request.FILES.getlist('image')
            start = time.time()
            for image in images:
                image = Uploads(image=image)
                image.save()
            end = time.time()
            print('without threading: ', end-start)
            messages.success(
                request, f'Images uploaded successfully in {end-start} secs.')
            return redirect('non_thread')
        else:
            messages.error(request, 'Error')
            return redirect('non_thread')
    else:
        form = UploadForm()
        return render(request, 'myapp/upload_form.html', {'form': form})


def upload2(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            images = request.FILES.getlist('image')

            start = time.time()

            # threading
            def upload(image):
                image = Uploads(image=image)
                image.save()

            allThreads = []
            for image in images:
                t = threading.Thread(target=upload, args=[image])
                t.start()
                allThreads.append(t)

            for thread in allThreads:
                thread.join()

            end = time.time()
            print('with threading: ', end-start)
            messages.success(
                request, f'Images uploaded successfully in {end-start} secs.')
            return redirect('with_thread')
        else:
            messages.error(request, 'Error')
            return redirect('with_thread')
    else:
        form = UploadForm()
        return render(request, 'myapp/upload_form.html', {'form': form})
