# CategorEase
Easy categorisation of downloads with a bit of artificial intelligence magic.

The project was created to play with local models using [Ollama](https://ollama.com) and to practice the ability to use models for various simple tasks.

## How does it work?

The script is designed to categorise downloaded files into one of 7 categories :

- musics
- documents
- installations
- datas
- images
- videos
- archives

and then move the file to the appropriate directory.

https://github.com/growdelan/CategorEase/assets/34998212/aae3e4a9-13b8-43d4-a66a-2ab596a72ecb



# Installation
For the script to work correctly you need to install [Ollama](https://ollama.com) and download the correct model, in the example we use [llama3:8B](https://llama.meta.com/llama3/) as the model:

```
ollama pull llama3
```

once this has been done, the script can be run.
