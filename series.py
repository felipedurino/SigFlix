import requests
import os
#class Serie:
def procurar_series(tv_show_titulo):
        os.system('cls')
        API_KEY = 'a2441588784028a04a0ac4785d0489d0'

        
        BASE_URL = 'https://api.themoviedb.org/3'

        procurar_url=  search_url = f'{BASE_URL}/search/tv?api_key={API_KEY}&query={tv_show_titulo}'
        response = requests.get(procurar_url)
        if response.status_code == 200:
            procurar_resultados = response.json()
            if procurar_resultados['results']:

                tv_show_id = procurar_resultados['results'][0]['id']

                tv_show_url = f'{BASE_URL}/tv/{tv_show_id}?api_key={API_KEY}&language=pt-BR'
                tv_show_response = requests.get(tv_show_url)
                if tv_show_response.status_code ==200:
                    tv_show_data= tv_show_response.json()
                    
                    name = tv_show_data['name']
                    overview = tv_show_data['overview']
                    first_air_date = tv_show_data['first_air_date']
                    poster_path = tv_show_data['poster_path']

                    atores_url = f'{BASE_URL}/tv/{tv_show_id}/credits?api_key={API_KEY}'
                    atores_response = requests.get(atores_url)
                    if atores_response.status_code == 200:
                        atores_data= atores_response.json()
                        cast = [actor['name']for actor in atores_data['cast'][:6]]


                    videos_url = f'{BASE_URL}/tv/{tv_show_id}/videos?api_key={API_KEY}'
                    videos_response = requests.get(videos_url)
                    if videos_response.status_code == 200:
                        videos_data = videos_response.json()
                        trailers = [video['key']for video in videos_data['results']if video['type']=='Trailer']
                        if trailers:
                            trailer_key = trailers[0]

                    print(f'Nome: {name}\n')
                    print(f'Descrição: {overview}\n')
                    print(f'Atores Principais: {", ".join(cast)}\n')
                    print(f'Data de Lançamento: {first_air_date }\n')
                    print(f'Poster: https://image.tmdb.org/t/p/w500{poster_path}\n')
                    if trailers:
                        print(f'Trailer: https://www.youtube.com/watch?v={trailer_key}\n')
                    else:
                        print('Trailer não encontrado.')
                else:
                    print('Detalhes da série não encontrados.')
            else:
                print('Série não encontrada.')
        else:
            print('Erro ao pesquisar série.')

    #tv_show_titulo = input('Isira o titulo da série: ')
    #procurar_series(tv_show_titulo)
