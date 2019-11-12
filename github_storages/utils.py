import requests
import simplejson as json

from django.conf import settings

def get_url(name):
		url = "https://api.github.com/repos/"
		url += str(settings.GITHUB_HANDLE) + "/"
		url += str(settings.GITHUB_REPO_NAME) 
		url += "/contents/"
		url += str(name)

		return url

