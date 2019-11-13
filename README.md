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
       
## About
django-github-s3 is a project to provide beginners a storage backend on github for free.

Since other simple-storage services reqires credit-card information to setup an account and get started. 
There is a lot of traction in between for the beginners. 

There django-github-s3 helps bigineers to store the media files on github with very less number of steps required in the initial setup.

Found a Bug? Something Unsupported?
Issues are tracked via GitHub issues at the project issue page.

## Contributing

 1. Check for open issues at the project issues page or open a new issues to start a discussion about a feature or bug
 2. Fork the django-github-s3 repository on GitHub to start making changes in your own branch.







