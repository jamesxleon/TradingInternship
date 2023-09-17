from local_settings import secret_key
import openai

prompt = 'Tell me a slogan for a home security company'
open.api_key = secret_key

output = openai.Completion.create(
	model = 'text-davinci-003',
	prompt = prompt,
	max_tokens = 200,
	temperature = 0
)

print(output) #This is a JSON object

output_text = output['choices'][0]['text']

