from pytube import YouTube

# processo de pegar o link e autentificar para liberear videos bloqueados para contas anônimas
link = input("Digite o link do video a ser baixado: ")
video = YouTube(
    link,
    use_oauth=True,
    allow_oauth_cache=True
)

# indentifica no terminal o video que está sendo baixado para confirmar se esta certo
print("baixando:", video.title)

# acha a maior resolução do mp4
stream = video.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().last()

#download na pasta de videos
stream.download("videos")

print("concluído")
