import requests
from common.models import *
from common.responses import *

from rest_framework.views import APIView
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, reverse


class URLMaps(APIView):

	def get(self, request, surl, *args, **kwargs):

		try:
			identifier = int(surl.strip(), 16)
			url_map = URLMap.objects.filter(identifier=identifier).last()
			if not url_map:
				return HttpResponseNotFound('Page not found')

			return HttpResponseRedirect(url_map.url)
		except Exception as e:
			print(e)
			return HttpResponseNotFound('Page not found')


	def post(self, request, *args, **kwargs):

		try:
			url = request.POST.get('url')
			if not url or not url.strip():
				return bad_request(message='Please provide a url to shorten')
			url = url.strip()

			try:
				url_response = requests.get(url)
			except Exception as e:
				return bad_request(message='The URL provided is invalid')

			last_url_map = URLMap.objects.last()
			base_identifier = 1000
			if last_url_map:
				base_identifier = last_url_map.identifier

			url_map = URLMap.objects.create(identifier=base_identifier+1, url=url)

			return success({'short_url': request.build_absolute_uri(reverse('common:redirect-to-long-url', args=(hex(url_map.identifier),)))})

		except Exception as e:
			print(e)
			return exception(message='We could not create a shortened url')
