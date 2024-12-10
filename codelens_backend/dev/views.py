"""
Views для приложения.

Содержит View для страницы о нас и
страницы с формой для обработки запроса.
"""
from django.shortcuts import render
from django.views.generic import FormView, TemplateView

from codelens_backend.settings import BASE_DIR
from utils import example, file_management

from .forms import UploadPNGForm


class TestTesseractView(FormView):
    """View для отображения формы обработки изображения."""

    template_name = 'dev/mainpage/index.html'
    form_class = UploadPNGForm

    def form_valid(self, form):
        """
        Обрабатывает валидную форму.

        form: экземпляр формы с заполненными валидными данными
        return: HttpResponse с контекстом, в котором находится результат обработки:
        Текст, язык, наличие ошибок в синтаксисе и css таблица для подсветки
        """
        code_snippet_image = form.cleaned_data.get('file')

        snippet_file_name = (str(BASE_DIR) + '\\uploads\\temp\\' +
                             str(code_snippet_image))  # todo add random_postfix
        file_management.save_file(snippet_file_name, self.request.FILES.get('file'))

        html_result, code_style, expected_lang, valid\
            = example.process_code_snippet_image(snippet_file_name)

        file_management.delete_file(snippet_file_name)

        return render(self.request, self.template_name,
                      context={'form': form, 'result_text': html_result,
                               'code_style': code_style, 'lang': expected_lang,
                               'valid': valid})


class AboutPage(TemplateView):
    """View для отображения страницы 'О нас'."""

    template_name = "dev/aboutpage/index.html"
