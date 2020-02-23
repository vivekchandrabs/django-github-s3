# Github storage class for Django pluggable storage system.
#
# Author: Vivek Chandra B S <vivek.chandra.301096@gmail.com>
#
# License: Mozilla Public License Version 2.0
#
# Usage:
# 
# Add below settings.py:
# DEFAULT_FILE_STORAGE = "github_storages.backend.BackendStorages"
# GITHUB_HANDLE = 'Your Github Handle'
# ACCESS_TOKEN = "Your Github Access Token"
# GITHUB_REPO_NAME = "Your Github Repository Name"
# MEDIA_BUCKET_NAME = "Media Bucket Name"

import requests
import simplejson as json
import base64
import os
import posixpath
import random

from django.conf import settings
from django.core.files.storage import Storage
from django.utils.encoding import force_text
from django.conf import settings
from django.db import models

from github_storages.utils import get_url

class BackendStorages(Storage):
	""" Github Backend storage class for Django pluggable storage system."""

	def __init__(self):
		''' Get all the credentials from the settings.py file 
			and initialize them to global variables. 
		'''
		self.github_handle = settings.GITHUB_HANDLE
		self.token = settings.ACCESS_TOKEN
		self.repo_name = settings.GITHUB_REPO_NAME

		try:
			self.media_bucket = settings.MEDIA_BUCKET_NAME
		except:
			self.media_bucket = None

	def url(self, name):
		return name

	def save(self, name, content, max_length=None):
		''' Saves the file uploaded from the user side to github '''

		path_with_file_name = posixpath.basename(name).split("\\")
		name = path_with_file_name.pop()
		path = path_with_file_name
		
		return self._save(name, path, content)

	def _save(self, name, path, content):
		'''
		:Required:
			name || (name of file) || type string
			content || (content of the file)

		:Action:
			* Check for the available file name in the github.
			* If found then calls the upload_file_to_git function

		:Returns:
			* Download URL of the file

		'''
		while True:
			if self.exists(name, path):
				name = self.get_available_name(name)
			else:
				break

		response = self.upload_file_to_git(name, path, content)

		return response["content"]["download_url"]

	def exists(self, name, path):
		'''
		:Required:
			name || (name of the file) || type string

		:Action:
			* Gets the fetch url from the get_url method.
			* Fetchs the response from the git using requests library

		:Returns:
			* Returns True if File exists on github
			* Returns False if File does not exits on github

		'''

		fetch_url = get_url(name, path, self.media_bucket)
		response = requests.get(fetch_url)

		if response.status_code == 200:
			return True
		else:
			return False

	def get_available_name(self, name, max_length=None):
		'''
		:Required:
			name || (name of the file) || type string

		:Action:
		 	* Appends a random hash value to the file name

		 :Returns:
		 	* New file name
		'''

		random_hash = random.random() * 1000
		name = str(int(random_hash)) + name
		return name

	def upload_file_to_git(self, name, path, content):
		'''
		:Required:
			name || (name of the file) || type string
			content || Content of the file
		
		:Action:
			* Gets the upload_url from the get_url method
			* Constructs the payload.
			* Sends put request to the upload_url with payload and headers.

		:Returns
			* Content of the response obtained from the github.

		:Raise Errors:
			* If github returns 404 status_code.

		'''

		upload_url = get_url(name, path, self.media_bucket)

		headers ={"Authorization": f"token {self.token}"}
		
		payload = {}
		payload["message"] = name
		payload["committer"] = {}
		payload["committer"]["name"] = "Monalisa Octocat"
		payload["committer"]["email"] = "octocat@github.com"
		payload["content"] = self.convert_to_base64(content)

		response = requests.put(url= upload_url, data=json.dumps(payload), headers=headers)

		if response.status_code == 404:
			raise IOError(response.content)

		json_data = json.loads(response.content)
		return json_data

	def convert_to_base64(self, content):
		'''
		:Required:
			content || Content of the uploaded file

		:Action:
			* Converts the content of the file to base64 format.

		:Returns:
			base64 format string.
		'''

		my_string = base64.b64encode(content.read())
		return my_string

	def delete(self, name):
		'''
		:Required:
			name || (name of the file) || type string

		:Action: 
			* Gets the fetch url from the get_url method
			* Gets the response from the github for the particular content
			* Extracts the sha from the response

			* Constructs the payload along with the sha
			* Gets the delete url from the get_url methods.
			* Calls delete url with the delete method.

		:Returns:
			True upon proper deletion of the file.

		:Raise:
			If the file does not exists || status_code = 404
		'''

		image_path = self.url(name).split("/master/")[-1]

		path_with_file_name = image_path.split("/")
		name = path_with_file_name.pop()

		if path_with_file_name[0] == self.media_bucket:
			del path_with_file_name[0]

		path = path_with_file_name

		delete_url = get_url(name, path, self.media_bucket)
		headers = {"Authorization": f"token {self.token}"}

		fetch_url = get_url(name, path, self.media_bucket)
		response = requests.get(fetch_url)

		try:
			json_data = json.loads(response.content)
			sha = json_data["sha"]

		except:
			raise IOError(response.content)

		delete_url = get_url(name, path, self.media_bucket)
		headers = {"Authorization": f"token {self.token}"}

		payload = {}
		payload["message"] = name
		payload["committer"] = {}
		payload["committer"]["name"] = "Monalisa Octocat"
		payload["committer"]["email"] = "octocat@github.com"
		payload["sha"] = sha

		response = requests.delete(url=delete_url, data=json.dumps(payload), headers=headers)

		if response.status_code == 404:
			raise IOError(response.content)

		return 1


