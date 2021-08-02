from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Viewer

import cv2 as cv
import random

def index(request):
    return render(request,"index.htm")

def input(request):
    viewer_instance = Viewer.objects.create(survey_age=request.POST.get("age"), survey_gender=request.POST.get("gender"))
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