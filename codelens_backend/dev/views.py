from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from codelens_backend.settings import BASE_DIR
from dulwich.contrib.test_release_robot import BASEDIR

from .forms import UploadPNGForm

from utils import file_management, example

class TestTesseractView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = UploadPNGForm()
        return render(request, 'dev/test-tesseract.html',
                      context={'form': form })

    def post(self, request: HttpRequest) -> HttpResponse:
        form = UploadPNGForm(request.POST, request.FILES)
        result = None
        if form.is_valid():
            png = form.cleaned_data.get('file')

            name = str(BASE_DIR) +  '\\uploads\\temp\\' + str(png)  # todo add random_postfix
            file_management.save_file(name, request.FILES.get('file'))

            html_result, code_style = example.test_method(name)

            file_management.delete_file(name)
        return render(request, 'dev/test-tesseract.html',
                      context={'form': form, 'result_text': html_result, 'code_style': code_style } )