from django.conf import settings

def get_url(name):
	'''
	Helper function to construct the url of the file.
	'''

		url = "https://api.github.com/repos/"
		url += str(settings.GITHUB_HANDLE) + "/"
		url += str(settings.GITHUB_REPO_NAME) 
		url += "/contents/"
		url += str(name)

		return url

