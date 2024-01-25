FROM r-base:latest

RUN apt-get -y update
RUN apt-get -y install python3 python3-pip

RUN R -e "install.packages(c('later','promises','rlang'))"
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y file
RUN R -e "install.packages('shiny')"

RUN R -e "library(shiny)" 