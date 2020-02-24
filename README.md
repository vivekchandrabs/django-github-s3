# django-github-s3

### Installation
Installing from PyPi:
        
        $ pip install django-github-s3
        
Once the installation is done, setup the following in the settings.py file.

Include the following package in the INSTALLED_APPS
       
       INSTALLED_APPS = [
            ....
            'github_storages',
       ]

After including the package setup the following in the settings.py

       DEFAULT_FILE_STORAGE = "github_storages.backend.BackendStorages"
       GITHUB_HANDLE = "Your Github Handle"
       ACCESS_TOKEN = "Your Github Access Token"
       GITHUB_REPO_NAME = "Your New Github Public Repository Name"
       MEDIA_BUCKET_NAME = "Your media bucket name"

For Example:

       DEFAULT_FILE_STORAGE = "github_storages.backend.BackendStorages"
       GITHUB_HANDLE = "vivekchandrabs"
       ACCESS_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
       GITHUB_REPO_NAME = "Example-Test-Repo"
       MEDIA_BUCKET_NAME = "media"
        
**Here is a video on how to get the [GitHub Access Token](https://www.loom.com/share/1ac9b95756e242c290e2329683737c2f)**


If you are using ImageField or FileField upload_to parameter can be specified for better organization of files.
      
       photo = models.ImageField(upload_to="pics/", null=True, blank=True)
       
## About
django-github-s3 is a project to provide beginners a storage backend on github for free.

Since other simple-storage-services requires credit-card information to setup an account and get started. 
There is a lot of traction in between for the beginners. 

Therefore django-github-s3 helps beginners to store the media files on github with very less number of steps required in the initial setup.

## Found a Bug? Something Unsupported?
Issues are tracked via GitHub issues at the [project issue page](https://github.com/vivekchandrabs/django-github-s3/issues).

## Contributing
 1. [Check for open issues](https://github.com/vivekchandrabs/django-github-s3/issues) at the project issues page or open a new issues to start a discussion about a feature or bug
 2. Fork the [django-github-s3 repository on GitHub](https://github.com/vivekchandrabs/django-github-s3) to start making changes in your own branch.
 
## Warning !!!
The github repository that you have to create should be public. Storing any confidential information is not recommended.

## Thanks To:

* [Vidyadhar Sharma](https://github.com/justvidyadhar) for guiding me throughout this project.
* [Speckbit Exploratories](https://www.speckbit.com) for giving me this opportunity.






