
from django.http import JsonResponse, HttpResponse
from PIL import Image
from django.conf.urls.static import static
import io #this handles input and output stream. handling files like object in memory
import os



# Json response
def Say_something(request):
  return JsonResponse({"message":"hello from the server!"})

# HTML response

def html_func(request):
    return HttpResponse("<h1>Welcome to my backend server...</h2>")
  
def xml_func(request):
    return HttpResponse("<message>This is xml data</message>",content_type="application/xml")
    
def txt_func(request):
    return HttpResponse("This is a text file")

def csv_func(request):
    response = HttpResponse(content_type="text/csv")
    response["content-Disposition"] = 'atachment; filename="premier_league_table.csv"'
    
    sheet ='''
        pos, club,           pts
        1,   arsenal,         85
        2,   chelsea,         72
        3,   machester united,70
    '''
    response.write(sheet)
    return response

def img_func(request):
    img = Image.open("media/picture.webp")
    
    desired_size = (1000, 800) # desire size
    
    img.thumbnail(desired_size, Image.Resampling.LANCZOS) # it impliments desired size
    
    output_buffer = io.BytesIO()  # create an in-memory to hold data of an image after conversion,avoiding saving a temporary file to disk.
    
    # saves the image in the memory buffer in JPEG formmat
    img.save(output_buffer, format="WEBP")
    
    # retrive the accumulated image data from the buffer
    image_data = output_buffer.getvalue()
    
    response = HttpResponse(image_data,content_type="picture/webp")
    return response


def pdf_func(request):
    pdf_path = os.path("media", "the_story_of_the_boy.pdf")
    
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_content = pdf_file.read()
    except FileNotFoundError:
        return HttpResponse("file not found", status=500)


    return HttpResponse(pdf_content, content_type="application/pdf")

def Vid_func(request):
    vid_path = os.path.join("media", "video.mp4")
    
    try:
        with open(vid_path, 'rb') as vid_file:
            return HttpResponse(vid_file.read(), content_type="video/mp4")
    except FileNotFoundError:
        return HttpResponse("File not found", status=500)