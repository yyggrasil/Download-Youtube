from pytube import YouTube

# processo de pegar o link e autentificar para liberear videos bloqueados para contas anônimas
video = YouTube(
    input("Digite o link do video a ser baixado: "),
    use_oauth=False,
    allow_oauth_cache=True
)

# indentifica no terminal o video que está sendo baixado para confirmar se esta certo
print("baixando:", video.title)

# acha a maior resolução do mp4
stream = video.streams.get_highest_resolution()

#download na pasta de videos
stream.download("/home/yggdrasil/Documents/codigos/gravador/videos")
