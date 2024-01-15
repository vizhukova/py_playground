import requests
import openai

URL = "https://api.openia.com/v1/chat/completions"

payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "system", "content": "Hi there!"}],
    "temperature": 1.0,
    "top_p": 1.0,
    "n": 1,
    "stream": False,
    "presence_penalty": 0,
    "frequency_penalty": 0,
}

# Temperature:
# Low Temperature (Close to 0):

# When the temperature is set to a low value (e.g., 0.2), the model tends to produce more focused and deterministic output.
# It's more likely to select the most probable word or phrase in a given context, resulting in more predictable and coherent responses.
# Moderate Temperature (Around 0.5 to 1.0):

# A moderate temperature (e.g., 0.5) strikes a balance between randomness and coherence.
# It allows for some variation in responses while still maintaining the relevance to the context.
# High Temperature (Above 1.0):

# When the temperature is set to a high value (e.g., 1.0 or higher), the model becomes more creative and generates more diverse but potentially less coherent text.
# It may introduce more randomness, which can lead to unusual or less contextually relevant responses.



# The top-p parameter helps you filter the vocabulary choices of the model based on the cumulative probability distribution of the word or token frequencies. It limits the generated text to the most relevant and probable options.

# Here's how top-p works:

# top-p is a value between 0 and 1 (e.g., 0.7).
# When you set a value for top-p, the model only considers the most likely tokens that make up that portion of the cumulative probability distribution. It progressively selects words or tokens until the cumulative probability reaches or exceeds the specified top-p value.
# It effectively filters out less probable and less relevant words, making the generated text more focused and coherent.
# Lower top-p values restrict the vocabulary more, leading to more deterministic output.
# Higher top-p values allow for a wider vocabulary selection and can lead to more diverse output.



#  the "n" value is typically associated with n-grams, which are contiguous sequences of n items (usually words or tokens) in a text. The "n" value represents the length of these sequences.

# For example:

# "unigram" or "1-gram" refers to single words or tokens.
# "bigram" or "2-gram" refers to sequences of two words or tokens.
# "trigram" or "3-gram" refers to sequences of three words or tokens.
# The choice of "n" affects the level of granularity when analyzing text. Different "n" values can be used in various natural language processing (NLP) tasks, such as text generation, language modeling, and text classification.

# the stream parameter is used to control whether the API response is generated all at once (stream set to False) or as a continuous stream (stream set to True) of messages.

# The presence_penalty and frequency_penalty parameters can be used to fine-tune the style and content of the generated responses. Depending on your application, you can adjust these parameters to make the responses more or less repetitive, use common or rare vocabulary, and control other aspects of the language model's output to better suit your specific requirements.

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai.api_key}"
}

response = requests.post(URL, headers=headers, json=payload, stream=False)

print(response)
print(response.content)