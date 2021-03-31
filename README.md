<h1 id="top" align="center">CvMatchingTemplate</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/draylon/cvmatchingtemplate?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/draylon/cvmatchingtemplate?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/draylon/cvmatchingtemplate?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/draylon/cvmatchingtemplate?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/draylon/cvmatchingtemplate?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/draylon/cvmatchingtemplate?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/draylon/cvmatchingtemplate?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  CvMatchingTemplate 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/draylon" target="_blank">Author</a>
</p>

<br>

## :dart: Enunciado ##

  1) Faça um vídeo caseiro de 10 segundos (300 quadros) com sua webcam, exibindo o deslocamento lento de um objeto (bem enquadrado na cena) sobre um cenário de fundo constante e câmera fixada/estática, sem autofoco (função de foco automático desligada)

  2) Separe os quadros utilizando, por exemplo, o software gratuito Irfanview

  3) Salve esses quadros como imagens em tons de cinza.

  4) Utilize uma amostra da primeira imagem im1 para obter um template (recorte) do objeto a ser rastreado. Utilize cvMatchTemplate verificando qual o melhor método para o seu caso (melhor rastreio). Tente justificar o uso do método escolhido. Quais as características deste método?

  5) Construa um vídeo de saída com os frames identificando o objeto rastreado

  6) Execute os mesmos passos para uma sequência de quadros com uma cena mais complexa (o seu mascote se movendo em um cenário de fundo com mais informações visuais).


## :boom: Entrega ##

Relatório contendo algum embasamento teórico, descrevendo a\
metodologia do experimento, resultados, análise, conclusão e\
bibliografia. Insira ilustrações no relatório e anexe os \
códigos-fonte utilizados.

## :sparkles: Features ##

:heavy_check_mark: Feature 1;\
:heavy_check_mark: Feature 2;\
:heavy_check_mark: Feature 3;

## :rocket: Technologies ##

The following tools were used in this project:

- [Python 3](https://python.org/)
- [Chocolatey](https://https://chocolatey.org/) ( Optional )
- [FFMpeg](https://www.ffmpeg.org/)
- [OpenCV Python](https://pypi.org/project/opencv-python/)
- [Pipreqs](https://pypi.org/project/pipreqs/) Python requirements generator

## :white_check_mark: Requirements ##

 - Before starting :checkered_flag:, you need to have [Git](https://git-scm.com).
 - Without Chocolatey, manually installation of [FFMpeg](https://www.ffmpeg.org/) is required.


## :checkered_flag: Starting ##

```bash

# Install ffmpeg through chocolatey
choco install ffmpeg

# Download Video repository from google Drive folder:
https://drive.google.com/drive/folders/1dPAoJhukNkaB7EjhVzsSNqE6yRCUNg91?usp=sharing

# Clone this project
$ git clone https://github.com/draylon/cvmatchingtemplate

# Access
$ cd cvmatchingtemplate

# Install dependencies
$ pip3 install -r requirements.txt

# Criar imagens apartir de vídeo
$ ffmpeg -i <arquivo_entrada>.mp4 -vf fps=1 <arquivo_saida>%d.png

# Run the project
$ py -3 main.py src/<arquivo_saida>

```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/draylon" target="_blank">𝓜!𝓻𝓪𝓬𝓵𝓮𝓐𝓾𝓻𝓪</a>

&#xa0;

<a href="#top">Back to top</a>
