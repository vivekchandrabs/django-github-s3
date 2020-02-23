from django.conf import settings

def get_url(name, path, media_bucket):
	'''
	Helper function to construct the url of the file.
	'''
	url = "https://api.github.com/repos/"
	url += str(settings.GITHUB_HANDLE) + "/"
	url += str(settings.GITHUB_REPO_NAME) 
	url += "/contents/"

	if media_bucket == None:
		url += str(name)
	else:
		url += str(media_bucket) + "/"

	if len(path) != 0:
		for folder_name in path:
			url += str(folder_name) + "/"

	url += str(name)

	return url
