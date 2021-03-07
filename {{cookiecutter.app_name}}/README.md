# Code for {{cookiecutter.app_name}}

This codebase is configured to use Django for the backend and Nuxt for the frontend. It can be developed locally using the docker-compose.yml, and has configuration for easy deployment to AWS Elastic Beanstalk. Heavily used terminal commands are placed below. 

## Building and starting containers locally

Make sure you are in the same directory as the docker-compose.yml file. 

Building the containers:
```
docker-compose -f docker-compose.yml build
```

Starting the containers:
```
docker-compose -f docker-compose.yml up
```

## Backend package management

It is recommended to manage packages in an anaconda virtual environment for the easiest to use experience. To open the anaconda environment, open an anaconda prompt terminal. 

Creating the environment:
```
conda create --name {{cookiecutter.app_name}}
```

Activating the environment:
```
conda activate {{cookiecutter.app_name}}
```

For backend files, this is easily managed using pip. To add the newly installed packages to your app, navigate into the backend directory and run the following command:
```
pip freeze > requirements.txt
```

## Frontend package management

Frontend files are easily managed using npm and does not generally require a virtual environment. To install a new package, cd into the frontend directory and the requirements files automatically updates. 

## Project Overview
### General Overview
    .
    ├── backend                        # Django Backend configuration
    ├── frontend                       # Nuxt Frontend configuration
    ├── nginx                          # NGINX configuration
    ├── .env.dev                       # Environment variables for development
    ├── .env.prod                      # Environment variables for production, reference only
    ├── buildspec-backend.yml          # AWS Codebuild instructions for building backend
    ├── buildspec-frontend.yml         # AWS Codebuild instructions for building frontend
    ├── buildspec-nginx.yml            # AWS Codebuild instructions for building nginx
    ├── docker-compose-prod.yaml       # Template docker-compose file for production environment
    ├── docker-compose.yml             # docker-compose file for developing locally
    ├── Dockerrun.aws.json             # Configuration for containers in elastic beanstalk
    └── README.md

### Backend General Overview
    .
    ├── ...
    ├── backend                    
    │   ├── apps                # Where all of your generated Django apps are stored
    |   |   ├── accounts        # Pre-configured app for custom user with Djoser integration
    |   |   └── core            # The core app for your project
    │   ├── backend
    |   |   └── settings.py  
    │   ├── custom_storages.py  # Configuration for using s3 for staticfiles with django-storages
    │   ├── Dockerfile          # The production dockerfile
    │   ├── Dockerfile.dev      # The development dockerfile
    │   ├── entrypoint-dev.sh   # Entrypoint for development
    │   ├── entrypoint-prod.sh  # Entrypoint for production       
    │   └── requirements.txt    # The backend requirements, managed by virtualenv            
    └── ...

### Frontend General Overview
    .
    ├── ...
    ├── frontend                    
    │   ├── docker               # Development docker configuration
    |   |   ├── Dockerfile.dev   # The development dockerfile
    |   |   └── start_dev.sh     # Entrypoint for development
    │   ├── Dockerfile           # The production dockerfile
    │   ├── start_prod.sh        # Entrypoint for production
    │   ├── nuxt.config.js       # Nuxt configuration files      
    │   └── package.json         # The frontend requirements          
    └── ...

### NGINX General Overview
    .
    ├── ...
    ├── nginx                    
    │   ├── dev                
    |   |   ├── dev.conf        # Development NGINX settings
    |   |   └── Dockerfile      # Development Dockerfile
    │   └── prod                
    |       ├── prod.conf       # Production NGINX settings
    |       └── Dockerfile      # Production Dockerfile      
    └── ...