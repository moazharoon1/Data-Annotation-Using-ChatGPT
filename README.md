# Data-Annotation-Using-ChatGPT
An interactive tool for sentiment analysis of tweets using LangChain OpenAI, using ChatGPT 3.5 Turbo.

This tool provides an interactive way to analyze the sentiment of tweets using LangChain OpenAI. It leverages the power of LangChain OpenAI models to understand the sentiment expressed in tweets regarding the COVID-19 pandemic. Users can annotate tweets with labels such as Positive, Extremely Positive, Negative, Extremely Negative, or Neutral, along with providing brief explanations for their chosen labels.

## Prerequisites
Before using this tool, you need to have:
- A paid OpenAI API key

## Installation
- Clone this repository to your local machine.
- Install the required dependencies:
```
pip install langchain-openai
```

## Usage
- Ensure you have your OpenAI API key ready.
- Run the script analyze_tweets.py to process the tweets with a given prompt and save the responses in CSV files.
- Follow the prompts provided and annotate the tweets accordingly, providing brief explanations for your chosen labels.
- Check the generated CSV files for the annotated tweets along with their sentiment labels and explanations.


## Prompt Variations
Three different prompt variations are provided for annotating the tweets:

- user_prompt_1: Basic prompt focusing on sentiment.
- user_prompt_2: Prompt considering sarcasm, humor, and figurative language.
- user_prompt_3: Comprehensive prompt with detailed instructions for annotation.

Happy sentiment analyzing!
