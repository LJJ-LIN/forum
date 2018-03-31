import sys
from django.views.debug import technical_500_response
from django.conf import settings
from django.http import HttpResponse
import logging
LOGGER = logging.getLogger('forum')
		

class LogExceptionMiddleware(object):

	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		try:
			response = self.get_response(request)
		except Exception as e:
			LOGGER.exception(e)
			return HttpResponse("出错了")
		return response

class UserBasedExceptionMiddleware(object):
	def process_exception(self, request, exception):
		if request.user.is_superuser or request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS:
			return technical_500_response(request, *sys.exc_info())
		