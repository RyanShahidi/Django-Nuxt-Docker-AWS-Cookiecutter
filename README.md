# Django Nuxt Cookiecutter
A cookiecutter project for easy development of a Django backend with Nuxt frontend and possible deployment to AWS Elastic Beanstalk. Services are managed utilizing docker-compose. Note, this project is not guaranteed to be secure and might have several unsecure configurations for production. Additionally, this project has not been tested at large scale and might not be stable in high traffic environments. 

### Utilizes
__________
* Django
* Django rest framework
* Nuxt
* Buefy
* Docker - Managed with Docker compose
* Nginx
* Postgres

### Features
_____
* A custom user model pre-configured on the backend with the auth module set-up on the frontend.
* Django rest framework integration
* Djoser account auth configuration
* Buildspec files for easy deployment using codepipeline
* Dockerrun.aws.json file for easy deployment to elastic beanstalk. Configured for t2.micro EC2 instance, update memory allocation as needed. 
* Buefy for the component library

# Set-up
To walk through set-up of this project we will create a sample application called Jarvis. This application will only be hosted locally, but the steps for projects that will eventually go to production are the same. 

### 1) Downloading repo
___

In the terminal, navigate to the directory where you would like to host your project. Make sure you have cookiecutter installed: 

```
pip install cookiecutter
``` 

After cookiecutter is installed, clone the repo:

```
cookiecutter https://github.com/RyanShahidi/Django-Nuxt-Docker-AWS-Cookiecutter
```

This will ask for two questions, the app name for the default app name and the website url. As we will only be hosting this locally, we do not need to enter a real url. Configuration for the test-app would be:

```
app_name [The default app name]: Jarvis
website_url [Website url without www or .com. Ex: enter 'example' for 'www.example.com']: example
```

If this app was going to be used for production and hosted at, for example, google.com, you would only enter 'google' for the website url. If your app uses a domain name ending that is not '.com', search through the generated files and update the url accordingly.

### 2) Initial configuration
___
By default, the cookiecutter app includes the two environment files that are used by your app. These were not initially included in the .gitignore file to allow them to be created during generation and, subsequently, the .gitignore file must be updated. In the .gitignore file, add the following info to prevent these files from being in the git history:

```
# Custom project files
.env.dev
.env.prod
```
After adding these to the gitignore, it is highly suggested to start a git repo to track your changes. The app can now be built and run using docker-compose. A more detailed overview of different commands and the project structure is in the generated README file. 

### 3) Common Error
___
If you receive the following error when building or running your docker container:

```
standard_init_linux.go:190: exec user process caused "no such file or directory"
```
This is likely an End of Line Sequence error, with the docker files in the CRLF format instead of LF format. Go through all of the Dockerfiles, docker-compose, and entrypoint files (Ends in .sh) and change them from CRLF -> LF. This is easily completed in Visual Studio Code, with the End of Line Sequence noted in the bottom right of the screen. 

### 4) Deploying to AWS
___
When your app is ready for deployment to AWS, follow the instructions in [the wiki](https://github.com/RyanShahidi/Django-Nuxt-Docker-AWS-Cookiecutter/wiki) for configuration and deployment. Note that these instructions are currently incomplete and possibly out-of-date, but should provide you with enough information to deploy the app.