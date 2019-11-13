# django-github-s3

### Installation
Installing from PyPi:
        
        $ pip install django-github-s3
        
Once the installation is done, setup the following in the settings.py file.

       DEFAULT_FILE_STORAGE = "github_storages.backend.BackendStorages"
       GITHUB_HANDLE = "Your Github Handle"
       ACCESS_TOKEN = "Your Github Access Token"
       GITHUB_REPO_NAME = "Your New Github Repository Name"


If you are using ImageField or FileField then do not specify upload_to parameters
      
       photo = models.ImageField(upload_to="pics/", null=True, blank=True)

Set it to just:
        
       photo = models.ImageField(null=True, blank=True)








