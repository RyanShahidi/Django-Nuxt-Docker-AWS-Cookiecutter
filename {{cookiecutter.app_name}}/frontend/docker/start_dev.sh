#!/bin/bash

npm rebuild node-sass
npm config set save-prefix=''
npm install
npm install --save nuxt

# run the development server
npm run dev
