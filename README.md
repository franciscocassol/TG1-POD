# TG1-POD


### Objetivo
O objetivo deste trabalho é aplicar os conceitos de Programação Orientada a Objetos para implementar um sistema de streaming musical simplificado, inspirado em plataformas como o Spotify.

### Descrição do Projeto
O sistema permite que usuários criem contas, montem playlists, reproduzam músicas e acompanhem estatísticas de reprodução. Todos os dados de usuários, músicas, artistas e playlists são carregados de um arquivo de configuração no formato Markdown (dados.md).

Durante a execução, o sistema deve tratar erros, como a inclusão de músicas inexistentes em uma playlist, e registrar esses erros em um arquivo de log. Ao final, um relatório detalhado com análises do sistema é gerado.

### Funcionalidades e Estrutura

O projeto é organizado em um pacote Python chamado Streaming/, contendo as seguintes classes e arquivos principais:

* main.py: Arquivo principal responsável por iniciar o menu do sistema.
* Streaming/menu.py: Contém o menu de opções para usuários e gerencia a interação com o sistema. Possui métodos para criar usuários, listar mídias, e gerar o relatório.
* Streaming/le_arquivo.py: Responsável por ler o arquivo de configuração dados.md e gerar logs de erros.
* Streaming/arquivo_de_midia.py: Classe abstrata para representar arquivos de mídia com atributos e métodos comuns.
* Streaming/musica.py: Subclasse de ArquivoDeMidia para representar músicas.
* Streaming/podcast.py: Subclasse de ArquivoDeMidia para representar podcasts.
* Streaming/playlist.py: Classe para gerenciar playlists, com funcionalidades de adicionar, remover e concatenar mídias.
* Streaming/usuario.py: Classe para representar usuários, contendo seu histórico de reprodução e playlists criadas.
* Streaming/analises.py: Classe com métodos estáticos para gerar análises sobre os dados do sistema, como músicas mais reproduzidas e o usuário mais ativo.
* logs/: Pasta para armazenar os logs de erros.
* relatorios/: Pasta para armazenar o relatório de estatísticas.
* config/: Pasta para armazenar o arquivo de configuração dados.md.

### Inovação
A inovação implementada no projeto é a funcionalidade de "Match", que cria uma nova playlist com base nas preferências musicais de dois usuários. A lógica de "Match" considera as músicas em comum nos históricos de reprodução e a compatibilidade das avaliações que cada usuário deu a essas músicas.

### Como Executar
Para executar o programa, certifique-se de que está no diretório raiz do projeto e execute o seguinte comando:

python3 main.py
