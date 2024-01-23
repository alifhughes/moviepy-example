import moviepy.editor as mpy

thumbnail_url = 'https://i.discogs.com/PNNlR9ifpuN8VA_Nt4uDLJzI1lmCadmOz85oc8TRgvc/rs:fit/g:sm/q:90/h:600/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTExNjg4/Njg1LTE1MjA2OTM5/MTItNDg1NS5qcGVn.jpeg'
url_video_path = "https://17841.s3.eu-west-1.amazonaws.com/11688685/IddlM389klM.mp4"
audio_clip = mpy.AudioFileClip(url_video_path).subclip(10, 30)
image_clip = mpy.ImageClip(thumbnail_url)
video_clip = image_clip.set_audio(audio_clip)
video_clip.duration = audio_clip.duration
video_clip.fps = 30
clip_name = f"moviepy-test.mp4"
video_clip.write_videofile(
    clip_name,
    audio_codec="aac",
    verbose=False,
    logger=None,
)
print(f"Video {clip_name} saved")
audio_clip.close()
image_clip.close()
video_clip.close()
