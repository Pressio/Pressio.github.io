FROM pressiomodelreduction/website_base:latest

WORKDIR /mysite

COPY content content/
COPY m.css m.css/
COPY pelicanconf.py ./pelicanconf.py
COPY Makefile .
COPY develop_server.sh ./develop_server.sh

# this is needed otherwise we get some weird errors
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

EXPOSE 8080:8080

CMD ["make", "devserver", "PORT=8080"]