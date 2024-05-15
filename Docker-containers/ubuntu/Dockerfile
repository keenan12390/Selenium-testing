# FROM ubuntu:22.04

# ARG USER_ID

# RUN apt update
# # RUN apt upgrade
# RUN apt install python3 -y
# RUN apt -get install pip

# # RUN su root -c python3 --version
# RUN whoami

# RUN echo $PATH
# RUN python3 --version
# RUN pip install toolium
# RUN pip install behave

# # RUN behave


FROM ubuntu:22.04
 
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y software-properties-common 
RUN apt-get install -y wget
RUN apt-get install -y build-essential
RUN apt-get install -y software-properties-common
RUN wget https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tar.xz \ 
&&  tar -xf Python-3.11.1.tar.xz \ 
&&  cd Python-3.11.1 \  
&&  ./configure --enable-optimizations \ 
&&  make altinstall \   
&&  apt install python3.11


# RUN wget https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tar.xz && \    
#     tar -xf Python-3.11.1.tar.xz && \     
#     cd Python-3.11.1 && \     
#     ./configure --enable-optimizations && \     
#     make altinstall
 
# RUN apt-get install -y python3-pip && \     
#     pip3 install behave toolium

    # python3.11 \
    # python3-pip
 
# RUN pip3 install behave toolium


# RUN apt-get update && \
#     apt-get install -y \
#     software-properties-common wget && \
#     add-apt-repository ppa:deadsnakes/ppa && \
#     apt-get update && \
#     apt-get install -y \
#     python3.11 \
#     python3.11-dev \
#     python3.11-distutils
 
# RUN python3.11 -m ensurepip && \
#     python3.11 -m pip install --upgrade pip && \
#     pip3.11 install behave toolium

# RUN apt-get update && \
#     DEBIAN_FRONTEND=noninteractive apt-get install -y \
#     build-essential \
#     wget \
#     software-properties-common
 
# RUN wget https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tar.xz && \
#     tar -xf Python-3.11.1.tar.xz && \
#     cd Python-3.11.1 && \
#     ./configure --enable-optimizations && \
#     make altinstall
 
# RUN /usr/local/bin/python3.11 -m ensurepip && \
#     /usr/local/bin/python3.11 -m pip install --upgrade pip setuptools
 
# RUN /usr/local/bin/python3.11 -m pip install behave toolium


# RUN apt-get update -y \
#     && apt-get upgrade -y \
#     && apt-get -y install build-essential \
#         zlib1g-dev \
#         libncurses5-dev \
#         libgdbm-dev \ 
#         libnss3-dev \
#         libssl-dev \
#         libreadline-dev \
#         libffi-dev \
#         libsqlite3-dev \
#         libbz2-dev \
#         wget \
#     && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get purge -y imagemagick imagemagick-6-common 

# RUN cd /usr/src \
#     && wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz \
#     && tar -xzf Python-3.11.0.tgz \
#     && cd Python-3.11.0 \
#     && ./configure --enable-optimizations \
#     && make altinstall

# RUN update-alternatives --install /usr/bin/python python /usr/local/bin/python3.11 1

# ARG DEBIAN_FRONTEND=noninteractive
# ENV TZ=Europe/Minsk
# RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# RUN apt install software-properties-common -y
# RUN add-apt-repository ppa:deadsnakes/ppa
# RUN apt-get update -y
# RUN apt install python3.11 python3-pip -y

# USER root

# RUN apt-get update && \
#     apt-get install -y --no-install-recommends software-properties-common && \
#     apt-get install -y --no-install-recommends gpg-agent && \
#     add-apt-repository -y ppa:deadsnakes/ppa && \
#     apt-get install -y --no-install-recommends $PYTHON_VERSION && \
#     apt-get install -y --no-install-recommends $PYTHON_VERSION-venv && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

# RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1


# WORKDIR /app
# COPY . .
# RUN apt-get update && DEBIAN_FRONTEND=noninteractive \
#     apt-get install -y python3.10 python3-pip

# RUN curl -sSL https://install.python-poetry.org | python3 - --preview
# RUN pip3 install --upgrade requests
# RUN ln -fs /usr/bin/python3 /usr/bin/python

# WORKDIR /app
# COPY . .
# RUN apt-get update && DEBIAN_FRONTEND=noninteractive \
#     apt-get install -y python3.10 python3-pip

# RUN curl -sSL https://install.python-poetry.org | python3 - --preview
# RUN pip3 install --upgrade requests
# RUN ln -fs /usr/bin/python3 /usr/bin/python

# CMD ["python3", "--version"]