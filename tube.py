from pytube import YouTube
url = YouTube('https://www.youtube.com/watch?v=MRyLC2M1K2w')
stream = url.streams.first()
stream.download()