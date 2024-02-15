import requests
import os
import creds
#class Filme:
def procurar_filme(nome_filme):
        os.system('cls')
    
        

        
        BASE_URL = 'https://api.themoviedb.org/3'

    
        procurar_url = f'{BASE_URL}/search/movie?api_key={creds.API_KEY}&query={nome_filme}'
        response = requests.get(procurar_url)
        if response.status_code == 200:
            search_results = response.json()
            if search_results['results']:
                
                movie_id = search_results['results'][0]['id']
                
            
                movie_url = f'{BASE_URL}/movie/{movie_id}?api_key={API_KEY}&language=pt-BR'
                movie_response = requests.get(movie_url)
                if movie_response.status_code == 200:
                    movie_data = movie_response.json()
                    
                    title = movie_data['title']
                    overview = movie_data['overview']
                    release_date = movie_data['release_date']
                    poster_path = movie_data['poster_path']
                    
                    
                    credits_url = f'{BASE_URL}/movie/{movie_id}/credits?api_key={API_KEY}'
                    credits_response = requests.get(credits_url)
                    if credits_response.status_code == 200:
                        credits_data = credits_response.json()
                        cast = [actor['name'] for actor in credits_data['cast'][:6]]  # Obtém os 5 principais atores
                        
                
                    videos_url = f'{BASE_URL}/movie/{movie_id}/videos?api_key={API_KEY}'
                    videos_response = requests.get(videos_url)
                    if videos_response.status_code == 200:
                        videos_data = videos_response.json()
                        trailers = [video['key'] for video in videos_data['results'] if video['type'] == 'Trailer']
                        if trailers:
                            trailer_key = trailers[0]  
                        
                    
                    print(f'Título: {title}\n')
                    print(f'Descrição: {overview}\n')
                    print(f'Atores Principais: {", ".join(cast)}\n')
                    print(f'Data de Lançamento: {release_date}\n')

                    movie_url = f'{BASE_URL}/movie/{movie_id}?api_key={API_KEY}'
                    movie_response = requests.get(movie_url)
                    if movie_response.status_code == 200:
                        movie_data = movie_response.json()
                        if 'awards' in movie_data and movie_data['awards']:
                            awards = movie_data['awards']
                            print(f'Prêmios de "{nome_filme}": {awards}')
                        else:
                            print(f'O filme {nome_filme} não recebeu prêmio\n')

                    print(f'Poster: https://image.tmdb.org/t/p/w500{poster_path}\n')
                    if trailers:
                        print(f'Trailer: https://www.youtube.com/watch?v={trailer_key}')
                    else:
                        print('Trailer não encontrado.')
                else:
                    print('Detalhes do filme não encontrados.')
            else:
                print('Filme não encontrado.')
        else:
            print('Erro ao pesquisar filme.')



        #nome_filme = input('COLOQUE O NOME DO FILME: ')
        #procurar_filme(nome_filme)
