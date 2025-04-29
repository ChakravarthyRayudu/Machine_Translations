import deepl
from config import API_KEY

auth_key = API_KEY  
print(auth_key)
translator = deepl.Translator(auth_key)

result = translator.translate_text("Hello, world!", target_lang="FR")
print(result.text)  
