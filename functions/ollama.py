"""Ollama configuration module"""

from openai import OpenAI


def system_prompt():
    """commands for the model, what it will have to do"""
    prompt = """
    I will give you the names of the files along with the extensions, your job is to classify these files into categories:

    <categories>
    musics - all music Extensions
    documents - anything that counts as a text file
    installations - all instalation files
    datas - various types of spreadsheets
    images - all image extensions
    videos - all video extensions
    archives - all archive extensions
    </categories>

    the output must be the category name only (THIS IS VERY IMPORTANT!!!)
    """

    return prompt


def set_ollama_client(ollama_url="http://localhost:11434/v1", ollama_api_key="ollama"):
    """set the openai client to use Ollama API."""
    client = OpenAI(
        base_url=ollama_url,
        api_key=ollama_api_key,
    )

    return client


def model_response(model: str, file_name: str, temperature=0.0):
    """Return the output from Ollama API."""
    prompt = system_prompt()
    client = set_ollama_client()
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": file_name},
        ],
    )

    return response.choices[0].message.content
