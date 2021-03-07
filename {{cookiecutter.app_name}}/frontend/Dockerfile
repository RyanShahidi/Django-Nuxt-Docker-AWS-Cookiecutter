FROM public.ecr.aws/bitnami/node:14.15.5

# create destination directory
WORKDIR /usr/src/app

# copy the app, note .dockerignore
COPY . /usr/src/app/

# expose 3000 on container
EXPOSE 3000

# set the browser base URL
ARG BROWSER_BASE_URL={{cookiecutter.website_url}}.com
ENV BROWSER_BASE_URL=$BROWSER_BASE_URL

#Set environment variables
ENV SENTRY_DISABLED=false

COPY ./start_prod.sh /usr/src/app/start_prod.sh
RUN chmod +x /usr/src/app/start_prod.sh

RUN npm rebuild node-sass
RUN npm config set unsafe-perm true
RUN npm config set save-prefix=''
RUN npm install
RUN npm install --save nuxt
RUN npm run build

# start the app
ENTRYPOINT [ "/usr/src/app/start_prod.sh" ]
