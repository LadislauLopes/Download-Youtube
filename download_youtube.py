import re
import tkinter as tk

from pytube import Playlist, YouTube


def Download_video(url):
    try:
        YouTube(url).streams.get_highest_resolution().download('Output')
    except:
        print(f"Falha a baixar o video")
    
def Download_Playlist_video(url):
    playlist = Playlist(url)
   
    for video in playlist.videos:
        try:
            video.streams.get_highest_resolution().download('Output')
            print(f'video {video.title} foi baixado')
        except:
            # Código para lidar com o erro de restrição de idade
            print(f"Falha a baixar o video {video.title}")

def Download_Playlist_Music(url):

    playlist = Playlist(url)
    YOUTUBE_STREAM_AUDIO = '140'
    # this fixes the empty playlist.videos list
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    # physically downloading the audio track
    for video in playlist.videos:
        try:
            audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
            audioStream.download('Output')
        except:
            print(f"Falha a baixar o audio {video.title}")

def Download_Music(url):
    try:
        YouTube(url).streams.get_audio_only().download('Output')
    except:
        print('Falha a baixar o audio')
        
def comeca():
    url= url_entry.get()
    escolha = nivel_var.get()
    
    if escolha== "1":
        Download_video(url)
    elif escolha=="2":
        Download_Playlist_video(url)
    elif escolha=="3":
        Download_Music(url)
    elif escolha=="4":
        Download_Playlist_Music(url)
    


janela = tk.Tk()
janela.title("Download de Vídeo/Áudio do Youtube")

# Defina o tamanho inicial da janela (largura x altura)
janela.geometry("350x300")
janela.resizable(False,False)
# Rótulo e campo de entrada para a URL
url_label = tk.Label(janela, text="URL:", font=("Arial", 12))
url_label.grid(row=0, column=0, padx=10, pady=5)

url_entry = tk.Entry(janela, font=("Arial", 10))
url_entry.grid(row=0, column=1, padx=10, pady=5)

# Rótulo para seleção de nível
nivel_label = tk.Label(janela, text="Selecione o tipo de download:", font=("Arial", 12))
nivel_label.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Radio buttons
nivel_var = tk.StringVar()
nivel_var.set("1")

nivel1_radio = tk.Radiobutton(janela, text="1. Vídeo", variable=nivel_var, value="1")
nivel1_radio.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

nivel2_radio = tk.Radiobutton(janela, text="2. Playlist de Vídeos", variable=nivel_var, value="2")
nivel2_radio.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

nivel3_radio = tk.Radiobutton(janela, text="3. Áudio", variable=nivel_var, value="3")
nivel3_radio.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

nivel4_radio = tk.Radiobutton(janela, text="4. Playlist de Áudio", variable=nivel_var, value="4")
nivel4_radio.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

# Botão para iniciar o download
botao_iniciar = tk.Button(janela, text="Iniciar Download", command=comeca, bg="blue", fg="white")
botao_iniciar.grid(row=6, column=0, columnspan=2, padx=0, pady=10)

credits_label = tk.Label(janela, text="Made by Ladislau Lopes", font=("Verdana", 8))
credits_label.grid(row=7, column=0, columnspan=2, padx=0, pady=10)

# Inicie a interface
janela.mainloop()