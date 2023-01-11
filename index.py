from pytube import YouTube

video = input('Olá, bem vindo ao donwloader, por favor, coloque o link do video que deseja baixar: ')
visualizacao = input("Deseja saber a contagem de visualizações do video? s/n ")

link = YouTube(video)

print(f'Baixando: {link.title}')
if visualizacao == 's':
    print("Visualizações: " + str(link.views))

stream = link.streams.get_audio_only()
if stream.download():
    print('Video baixado com sucesso!')
