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

	def __init__(self):
		self.github_handle = settings.GITHUB_HANDLE
		self.token = settings.ACCESS_TOKEN
		self.repo_name = settings.GITHUB_REPO_NAME
		self.location = "/"

	def url(self, name):
		return name

	def save(self, name, content, max_length=None):
		name = posixpath.basename(name).split("\\")[-1]
		
		return self._save(name, content)

	def _save(self, name, content):
		while True:
			if self.exists(name):
				name = self.get_available_name(name)
			else:
				break

		response = self.upload_file_to_git(name, content)

		return response["content"]["download_url"]

	def exists(self, name):
		fetch_url = get_url(name)
		response = requests.get(fetch_url)

		if response.status_code == 200:
			return True
		else:
			return False

	def get_available_name(self, content, max_length=None):
		random_hash = random.random() * 1000
		content = str(int(random_hash)) + content
		return content

	def upload_file_to_git(self, name, content):
		upload_url = get_url(name)

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
		my_string = base64.b64encode(content.read())
		return my_string

	def delete(self, name):
		name = posixpath.basename(name).split("\\")[-1]
		delete_url = get_url(name)
		headers = {"Authorization": f"token {self.token}"}

		fetch_url = get_url(name)
		response = requests.get(fetch_url)

		try:
			json_data = json.loads(response.content)
			sha = json_data["sha"]

		except:
			raise IOError(response.content)

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


