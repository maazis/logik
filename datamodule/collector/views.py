from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.views import View
from .models import Viewer

import cv2 as cv
import random
# import boto3 from botocore.exceptions import NoCredentialsError

def index(request):
    return render(request,"index.htm")

def input(request):
    if request.method=="POST":
        Viewer.objects.create(survey_age=request.POST.get("age"), survey_gender=request.POST.get("gender") ,survey_name=request.POST.get("name"))   
        return redirect('index/')
    return render(request, 'input.htm')


def camera(request):
    runCamera()
    return render(request,"camera.htm")


def runCamera():
    cap = cv.VideoCapture(0)

    fourcc = cv.VideoWriter_fourcc(*'MJPG') 
    out = cv.VideoWriter('output'+str(random.randint(0,30))+'.avi', fourcc, 20.0, (640, 480))

    while cap.isOpened():
        ret , frame = cap.read()
        if ret==True:
            cv.imshow("frame",frame)
        
            out.write(frame)

            if cv.waitKey(25) & 0xFF == ord('q'):
                break
                
        else:
            break

    cap.release()
    out.release()
    cv.destroyAllWindows()

ACCESS_KEY = 'AKIAW2LZ5RUN5LRRQE4W'
SECRET_KEY = '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'    

def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False