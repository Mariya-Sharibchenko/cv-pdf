from django.shortcuts import render

# Create your views here.
import pdfkit
from django.http import HttpResponse
from django.template import loader
from django.views.generic.base import View
from django.shortcuts import render


def create_pdf(request):
    options = {
        'page-size': 'A4',
        'disable-smart-shrinking': '',
        'margin-left': '0',
        'margin-right': '0',
        'margin-bottom': '25mm',
        'margin-top': '11mm',
        'footer-html': '/Users/mari-shari/PycharmProjects/CV_pdf/cvpdfproject/templates/footer.html',
        'header-html': '/Users/mari-shari/PycharmProjects/CV_pdf/cvpdfproject/templates/header.html',
        'print-media-type': '',
    }

    html = loader.render_to_string('cv.html', {})
    output = pdfkit.from_string(html, output_path=False, options=options)
    response = HttpResponse(content_type="application/pdf")
    response.write(output)
    return response


class InvoiceView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "cv.html")