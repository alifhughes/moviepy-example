# Movie py error example

Commands to run:
```bash
python -m venv venv
python -m pip install -r requirements.txt
python moviepy-test.py # Works! should get log line "Video moviepy-test.mp4 saved" and a video in the local directory

# Not working example with docker IndexError, OSError
docker build --tag 'moviepy-test' . -f Dockerfile.moviepy
docker run moviepy-test
```
