from django.shortcuts import render
from django.template import RequestContext
from testapp.forms import UploadFileForm
from PIL import Image, ImageOps,ImageFilter
from django.http import HttpResponse
from django.template import loader
import os
from django.conf import settings


def applyfilter(filename, preset):
	#gets file
	inputfile = '/home/mcolbert/cis4517/courseProject/photoapp/testapp/media/documents/' + filename

	f=filename.split('.')
	outputfilename = f[0] +'-'+ preset + '.jpg'
	
	outputfile = '/home/mcolbert/cis4517/courseProject/photoapp/testapp/static/output/' + outputfilename

	im = Image.open(inputfile)
	if preset=='gray':
		im = ImageOps.grayscale(im)

	if preset=='edge':
		im = ImageOps.grayscale(im)
		im = im.filter(ImageFilter.FIND_EDGES)

	if preset=='poster':
		im = ImageOps.posterize(im,3)

	if preset=='solar':
		im = ImageOps.solarize(im, threshold=80) 

	if preset=='blur':
		im = im.filter(ImageFilter.BLUR)
	
	if preset=='sepia':
		sepia = []
		r, g, b = (239, 224, 185)
		for i in range(255):
			sepia.extend([int(r*i/255), int(g*i/255), int(b*i/255)] )
		im = im.convert("L")
		im.putpalette(sepia)
		im = im.convert("RGB")

	im.save(outputfile)
	return outputfilename

def handle_uploaded_file(f,preset):
	#opens file or creates it for writing
	uploadfilename='/home/mcolbert/cis4517/courseProject/photoapp/testapp/media/documents/'+ f.name #'testapp/media/' + f.name #os.path.join(settings.MEDIA_ROOT, 'documents', f.name)  # Assuming 'documents' is your subdirectory  ##old line: 
	
	#saves the file to server
	with open(uploadfilename, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

	outputfilename=applyfilter(f.name, preset)
	return outputfilename

def home(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			preset=request.POST['preset']
			outputfilename = handle_uploaded_file(request.FILES['myfilefield'],preset)
			return render(request, 'testapp/process.html', {'outputfilename': outputfilename})
		else:
			print(form.errors)
	else:
		form = UploadFileForm() 
		return render(request, 'testapp/index.html', {'form': form} )






