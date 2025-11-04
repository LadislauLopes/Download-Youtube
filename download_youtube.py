import os
import re
import tkinter as tk
from pytubefix import Playlist, YouTube  


os.makedirs('Video_Output', exist_ok=True)
os.makedirs('Audio_Output', exist_ok=True)

def Download_video(url):
    try:
        yt = YouTube(url)
        yt.streams.get_highest_resolution().download('Video_Output')
        print(f"✅ Vídeo '{yt.title}' baixado com sucesso!")
    except Exception as e:
        print(f"❌ Falha ao baixar o vídeo: {e}")
    
def Download_Playlist_video(url):
    playlist = Playlist(url)
    print(f"🔗 Playlist detectada: {playlist.title}")
    for video in playlist.videos:
        try:
            video.streams.get_highest_resolution().download('Video_Output')
            print(f"✅ Vídeo '{video.title}' foi baixado")
        except Exception as e:
            print(f"❌ Falha ao baixar o vídeo '{video.title}': {e}")

def Download_Playlist_Music(url):
    playlist = Playlist(url)
    print(f"🔗 Playlist detectada: {playlist.title}")
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    for video in playlist.videos:
        try:
            yt = YouTube(video.watch_url)
            stream = yt.streams.filter(only_audio=True).first()
            stream.download('Audio_Output')
            print(f"🎵 Áudio '{yt.title}' baixado com sucesso!")
        except Exception as e:
            print(f"❌ Falha ao baixar o áudio '{yt.title}': {e}")

def Download_Music(url):
    try:
        yt = YouTube(url)
        yt.streams.filter(only_audio=True).first().download('Audio_Output')
        print(f"🎵 Áudio '{yt.title}' baixado com sucesso!")
    except Exception as e:
        print(f"❌ Falha ao baixar o áudio: {e}")
        
def convert_to_mp3():
    input_folder = 'Audio_Output'
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4") or filename.endswith(".m4a"):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.splitext(input_file)[0] + ".mp3"

            try:
                os.rename(input_file, output_file)
                print(f"🎧 Renomeado: {filename} → {os.path.basename(output_file)}")
            except Exception as e:
                print(f"❌ Erro ao renomear {filename}: {e}")

def comeca():
    url = url_entry.get().strip()
    escolha = nivel_var.get()
    
    if not url:
        print("❗ Digite uma URL válida.")
        return

    print(f"🔽 Iniciando download ({escolha})...")

    if escolha == "1":
        Download_video(url)
    elif escolha == "2":
        Download_Playlist_video(url)
    elif escolha == "3":
        Download_Music(url)
    elif escolha == "4":
        Download_Playlist_Music(url)

    convert_to_mp3()


janela = tk.Tk()
janela.title("Download de Vídeo/Áudio do YouTube (pytubefix)")
janela.geometry("350x300")
janela.resizable(False, False)

url_label = tk.Label(janela, text="URL:", font=("Arial", 12))
url_label.grid(row=0, column=0, padx=10, pady=5)

url_entry = tk.Entry(janela, font=("Arial", 10))
url_entry.grid(row=0, column=1, padx=10, pady=5)

nivel_label = tk.Label(janela, text="Selecione o tipo de download:", font=("Arial", 12))
nivel_label.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

nivel_var = tk.StringVar(value="1")
tk.Radiobutton(janela, text="1. Vídeo", variable=nivel_var, value="1").grid(row=2, column=0, columnspan=2, sticky=tk.W, padx=10)
tk.Radiobutton(janela, text="2. Playlist de Vídeos", variable=nivel_var, value="2").grid(row=3, column=0, columnspan=2, sticky=tk.W, padx=10)
tk.Radiobutton(janela, text="3. Áudio", variable=nivel_var, value="3").grid(row=4, column=0, columnspan=2, sticky=tk.W, padx=10)
tk.Radiobutton(janela, text="4. Playlist de Áudio", variable=nivel_var, value="4").grid(row=5, column=0, columnspan=2, sticky=tk.W, padx=10)

botao_iniciar = tk.Button(janela, text="Iniciar Download", command=comeca, bg="blue", fg="white")
botao_iniciar.grid(row=6, column=0, columnspan=2, pady=10)

credits_label = tk.Label(janela, text="Made by Ladislau Lopes", font=("Verdana", 8))
credits_label.grid(row=7, column=0, columnspan=2, pady=10)

janela.mainloop()
