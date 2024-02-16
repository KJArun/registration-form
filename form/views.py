from django.shortcuts import render
from django.http import HttpResponse
from form.models import Responses
from django.core.files.storage import default_storage
import firebase_admin,datetime,os
from firebase_admin import storage 
from datetime import timedelta
import mimetypes 

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
        obj_name=str(obj.Name)
        file_extension = uploaded_file.name.split('.')[-1]
        obj_name_with_extension = f"{obj_name}.{file_extension}"
        
        uploaded_file.name=str(obj.Name)
        # Upload file to Firebase Storage
        bucket = storage.bucket()
        blob = bucket.blob(obj_name_with_extension)
        blob.upload_from_file(uploaded_file)
        one_year = timedelta(days=365)
        download_url = blob.generate_signed_url(expiration=one_year)
        mime_type, _ = mimetypes.guess_type(download_url)

        response = HttpResponse(download_url, content_type=mime_type)
        response['Content-Disposition'] = f'attachment; filename="{obj_name_with_extension}"'
        print(download_url)
        obj.Link=download_url
        obj.save()

        return render(request,'form.html',{'success':'Response submitted successfully'})
    return render(request,'form.html')
