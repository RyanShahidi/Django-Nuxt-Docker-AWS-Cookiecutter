FROM public.ecr.aws/nginx/nginx:1.19.7-alpine
COPY ./dev.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]