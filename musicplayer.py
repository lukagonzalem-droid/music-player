import flet as ft
import flet_audio as fta 

def main(page: ft.Page):
    page.title = "Music Player"
    page.window_width = 400
    page.window_height = 500
    playlist = [
        {"title": "CLOUD 9", "artist": "JUNNY, Levent Geiger", "album": "CLOUD 9", "file": "Songs/cloud9.mp3", "cover": "Covers/cloud9.jpeg"},
        {"title": "Left and Right", "artist": "Charlie Puth, Jung Kook", "album": "Left and Right", "file": "Songs/leftandright.mp3", "cover": "Covers/leftandright.jpeg"},
        {"title": "VeLDÁ", "artist": "Bad Bunny, Omar Courtz", "album": "DeBí TiRAR MáS FOToS", "file": "Songs/velda.mp3", "cover": "Covers/velda.jpeg"},
        {"title": "Si Tu Prescencia Conmigo No Va", "artist": "Oasis Ministry", "album": "Si Tu Prescencia Conmigo No Va", "file": "Songs/situpresenciaconmigonova.mp3", "cover": "Covers/situprescenciaconmigonova.jpeg"},
        {"title": "Quien Te Ve Adorando", "artist": "Dianette Mendez, Kemilly Santos", "album": "Quien Te Ve Adorando", "file": "Songs/quienteveadorando.mp3", "cover": "Covers/quienteveadorando.jpeg"},
    ]
    
    current_index = 0
    is_playing = False
    audio = fta.Audio(src = playlist[0]["file"], autoplay = False)
    page.services.append(audio)
    coverImage = ft.Image(src = playlist[0]["cover"], width = 200, height = 200)
    titleText = ft.Text(size = 18, weight = "bold")
    artistText = ft.Text()
    albumText = ft.Text()

    def update_labels():
        song = playlist[current_index]
        titleText.value = f"TITULO: {song['title']}"
        artistText.value = f"Artist: {song['artist']}"
        albumText.value = f"Album: {song['album']}"
        coverImage.src = song["cover"]
        page.update()  
    
    async def play_pause(e):
        nonlocal is_playing
        if is_playing:
            await audio.pause()
            playButton.text = "Play"
        else:
            await audio.play()
            playButton.text = "Pause"
        is_playing = not is_playing
        page.update()

    async def next_song(e):
        nonlocal current_index, is_playing
        current_index = (current_index + 1) % len(playlist)
        audio.src = playlist[current_index]["file"]
        update_labels()
        await audio.play()
        is_playing = True
        playButton.text = "Pause"
        page.update()

    async def prev_song(e):
        nonlocal current_index, is_playing
        current_index = (current_index - 1) % len(playlist)
        audio.src = playlist[current_index]["file"]
        update_labels()
        await audio.play()
        is_playing = True
        playButton.text = "Pause"
        page.update()

    playButton = ft.Button("Play", on_click = play_pause)
    nextButton = ft.Button("Next", on_click = next_song)
    prevButton = ft.Button("Previous", on_click = prev_song)

    page.add(
        ft.Column([coverImage, titleText, artistText, albumText, ft.Row([prevButton, playButton, nextButton],alignment = "center"),], horizontal_alignment = "center"))
    update_labels()

ft.app(target = main, assets_dir = ".")