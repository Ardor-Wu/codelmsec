import os
import google.generativeai as gen

# Automatically configure with env var
gen.configure(api_key=os.environ["GOOGLE_API_KEY"])

# List available models and check if they support generateContent
for model in gen.list_models():
    supports_gen = 'generateContent' in model.supported_generation_methods
    print(f"{model.name} | generateContent: {supports_gen}")
