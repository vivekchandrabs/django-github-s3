from django.conf import settings

def get_url(name, media_bucket):
	'''
	Helper function to construct the url of the file.
	'''
	if media_bucket == None:
		url = "https://api.github.com/repos/"
		url += str(settings.GITHUB_HANDLE) + "/"
		url += str(settings.GITHUB_REPO_NAME) 
		url += "/contents/"
		url += str(name)

		return url

	else:
		url = "https://api.github.com/repos/"
		url += str(settings.GITHUB_HANDLE) + "/"
		url += str(settings.GITHUB_REPO_NAME) 
		url += "/contents/"
		url += str(media_bucket) + "/"
		url += str(name)

		return url
