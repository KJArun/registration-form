from django.shortcuts import render
from form.models import Responses
from django.core.files.storage import default_storage
import firebase_admin,datetime
from firebase_admin import storage 

def index(request):
    if request.method=="POST" and request.FILES['file']:
        obj=Responses()
        obj.Name=request.POST['name']
        obj.Email=request.POST['email']
        obj.Phone=request.POST['contact']
        obj.Department=request.POST['department']
        obj.Year=request.POST['year']
        obj.Title=request.POST['title']

        uploaded_file = request.FILES['file']
        uploaded_file.name=str(obj.Email)
        # Upload file to Firebase Storage
        bucket = storage.bucket()
        blob = bucket.blob(str(obj.Email))
        blob.upload_from_file(uploaded_file)
        download_url = blob.generate_signed_url(expiration=datetime.timedelta(days=1))
        obj.Link=download_url
        print(download_url)
        obj.save()
        return render(request,'form.html',{'success':'Response submitted successfully'})
    return render(request,'form.html')
