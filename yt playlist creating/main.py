from ytmusicapi import YTMusic
yt=YTMusic("browser.json")
song_names=["Infinity",
            "Heat Waves",
            "After Hours"]
playlist_id=yt.create_playlist("cool songs",
                               "made from code")
print(playlist_id)
for song in song_names:
    search_results=yt.search(song,filter="songs")
    if search_results:
        video_id=search_results[0]["videoId"]
        yt.add_playlist_items(playlist_id,[video_id])
    print(f"added: {song}")
else :
    print(f"could not found: {song}")
