from django.shortcuts import render
# from django import FileResponse
from django.conf import settings
import os

# Create your views here.



def home(request):
    
    return render(request, 'index.html')


# def download(request):
#     pdf_path = os.path.join(settings.STATIC_ROOT, '/static/images/Mon_CV.pdf')

#     # Open the PDF file in binary mode.
#     with open(pdf_path, 'rb') as pdf_file:
#         # Serve the PDF file as a downloadable file.
#         response = FileResponse(pdf_file, as_attachment=True, filename='Mon_CV.pdf')
#         return response