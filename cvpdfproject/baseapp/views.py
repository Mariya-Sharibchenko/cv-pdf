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

    data = {
		'first_name': 'MyName',
		'last_name': 'MyNameLast',
		'job_title': 'DevOps Engineer',
		'phone': '100393903',
		'email': 'mkfld@jfk.com',
		'image': 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8dXNlciUyMHByb2ZpbGV8ZW58MHx8MHx8&w=1000&q=80',
		'cv_experience': [{
			'company': 'MyCompany',
			'job_title': 'DevOps Engineer',
			'start_date': '20.10.2020',
			'end_date': '20.10.2022',
			'projects': [{
				'project_name': 'MyProj1',
				'technologies': [
					{'technology': 'DevOps Engineer'},
					{'technology': 'fjdk'},
					{'technology': 'Python'},
					{'technology': 'DevOps Engineer'},
					{'technology': 'fjdk'},
					{'technology': 'Python'},
					{'technology': 'DevOps Engineer'},
					{'technology': 'fjdk'},
					{'technology': 'Python'}
				],
				'description': 'project description',
				'summary': 'project summary',
			},
			{
				'project_name': 'MyProj2',
				'technologies': [{'technology': 'DevOps Engineer'}, {'technology': 'fjdk'}, {'technology': 'Python'}],
				'description': 'project description',
				'summary': 'http://djfbg.jxp',
			}],
		},
		{
			'projects': [
				{'project_name': 'MyProj1'},
				{
					'project_name': 'MyProj2',
					'technologies': [{'technology': 'DevOps Engineer'}, {'technology': 'fjdk'}, {'technology': 'Python'}],
					'description': 'project description',
					'summary': 'http://djfbg.jxp',
				}
			],
		}],
		'cv_languages': [{
			'language': {'language': 'eng'},
			'language_level': 'A1-elementary'
		},
		{
			'language': {'language': 'rus'},
			'language_level': 'native'
		}],
		'skills': [
			{'skill_name': 'test'},
			{'skill_name': 'test'},
			{'skill_name': 'test'},
			{'skill_name': 'test'}
		],
		'tools': [
			{'tools_name': 'test'},
			{'tools_name': 'test'},
			{'tools_name': 'test'},
			{'tools_name': 'test'}
		],
		'social_media': {'name': 'LinkedIn'},
		'additional_info': 'Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
	}

    html = loader.render_to_string('cv.html', {'data': data})
    output = pdfkit.from_string(html, output_path=False, options=options)
    response = HttpResponse(content_type="application/pdf")
    response.write(output)
    return response


class InvoiceView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "cv.html")