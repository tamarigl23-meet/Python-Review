def create_youtube_video(title, description):
	new_video = {"title":title, "description":description,"likes":0, "dislikes": 0, "comments": {"username": ""}}
	return new_video


def like_youtube(youtube_video):
	if "likes" in youtube_video:
		youtube_video["likes"] = youtube_video["likes"]+ 1

	return youtube_video


def dislike_youtube(youtube_video):
	if "likes" in new_video:
		youtube_video["dislikes"] = youtube_video["dislikes"]+ 1

	return youtube_video

new_youtube_video= {“Name”:Tamamri,”Age”:16}
