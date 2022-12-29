FROM python:3

WORKDIR /

COPY . .

CMD [ "python", "./multiprocessor.py" ]

# HELPFUL COMMANDS:

# build
# docker build -t python_multiprocessing .

# run
# docker run -it --rm python_multiprocessing

# run with custom number of available cores
# docker run -it --rm --cpuset-cpus="0-7" python_multiprocessing

# update docker-machine to change allowed cores
# NOTE: setting up core usage with "--cpuset-cpus" cannot exceed --virtualbox-cpu-count
# docker-machine rm default
# docker-machine create -d virtualbox --virtualbox-cpu-count=8 --virtualbox-memory=8192 --virtualbox-disk-size=10000 default

# More info found here:
# https://stackoverflow.com/questions/47989418/multiprocessing-python-program-inside-docker