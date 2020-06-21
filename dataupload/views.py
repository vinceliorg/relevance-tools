from django.shortcuts import render
from .forms import UploadDocumentForm
from .savefile import handle_uploaded_file

def upload_doc(request):
    form = UploadDocumentForm()
    if request.method == 'POST':
        form = UploadDocumentForm(request.POST, request.FILES)
        print('saved files') 
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
    return render(request, 'dataupload/upload_doc.html', locals())

def data_mapping(reuqest,file_path):
    data=pd.read_csv(file_path, encoding = "ISO-8859-1")
    return HttpResponse("The column names are  %s." % data.column.value)

