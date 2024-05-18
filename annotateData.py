import csv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize LangChain OpenAI model
llm = ChatOpenAI(openai_api_key="")  # Replace YOUR_API_KEY with your actual API key

# Define a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("user", "{input}")
])

# Define an output parser
output_parser = StrOutputParser()

# Add the output parser to the chain
chain = prompt | llm | output_parser

import json
def process_tweet(tweet, prompt):
    response = chain.invoke({"input": prompt.format(tweet=tweet) + """
                             Note give the output in the form {"label":"your_label","reason":"your justification"}"""})
    response_dict = json.loads(response)
    return response_dict

# Function to process the first 5 tweets with a given prompt and save responses in a CSV file

def process_first_5_tweets_with_prompt(prompt, output_file):
    with open('Corona_NLP_test.csv', mode='r') as file:
        reader = csv.DictReader(file)
        with open(output_file, mode='w', newline='') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(['tweet', 'sentiment_label', 'sentiment_reason'])  # Updated header
            for i, row in enumerate(reader):
                if i >= 5:
                    break
                tweet = row['OriginalTweet']
                response = process_tweet(tweet, prompt)
                sentiment_label = response["label"]
                sentiment_reason = response["reason"]
                writer.writerow([tweet, sentiment_label, sentiment_reason])  # Write sentiment and explanation to separate columns

user_prompt_1 = "**Focus on the sentiment expressed in the tweet, considering the context of the COVID-19 pandemic.**\nHere is the tweet: '{tweet}'. Annotate the tweet with one of the following labels: Positive, Extremely Positive, Negative, Extremely Negative, Neutral. **Provide a brief explanation for your chosen label.**"
user_prompt_2 = "Focus on the sentiment expressed in the tweet, considering the context of the COVID-19 pandemic (2020).\nHere is the tweet: '{tweet}'. Annotate the tweet with one of the following labels: Positive, Extremely Positive, Negative, Extremely Negative, Neutral. Consider sarcasm, humor, or other forms of figurative language that might influence the true meaning. Briefly explain your reasoning for the chosen label (3-4 lines)."
user_prompt_3 = """**Focus on the sentiment expressed in the tweet, considering the context of the COVID-19 pandemic (2020).**

**Here is the tweet:** '{tweet}'

**Annotate the tweet with one of the following labels:**

**Positive** Tweet expresses a hopeful, optimistic, or supportive view of the situation.
**Extremely Positive** Tweet conveys a strong feeling of joy, relief, or gratitude related to the pandemic.
**Negative** Tweet expresses frustration, disappointment, or criticism surrounding the pandemic.
**Extremely Negative** Tweet conveys strong feelings of anger, fear, or despair related to the pandemic.

**Consider sarcasm, humor, or other forms of figurative language that might influence the true meaning.**

**Provide a brief explanation for your chosen label (3-4 lines):**

* If the tweet is positive, explain why it's optimistic and mention keywords supporting your decision.
* If the tweet is extremely positive, explain the strong positive emotions and mention keywords. 
* If the tweet is negative, explain the frustration, disappointment, or criticism and mention keywords.
* If the tweet is extremely negative, explain the strong negative emotions (anger, fear, despair) and mention keywords.
* If the tweet is neutral, explain why it doesn't express a clear positive or negative sentiment. 
* If the tweet is uncertain, explain why the sentiment is unclear and mention any signs of sarcasm, humor, etc. 

**Remember:**

* Start explanations with lowercase letters and use proper grammar/punctuation.
* Keep explanations concise and informative.
"""

# Process tweets with each prompt and save responses in separate CSV files
process_first_5_tweets_with_prompt(user_prompt_1, 'prompt1_responses.csv')
process_first_5_tweets_with_prompt(user_prompt_2, 'prompt2_responses.csv')
process_first_5_tweets_with_prompt(user_prompt_3, 'prompt3_responses.csv')
