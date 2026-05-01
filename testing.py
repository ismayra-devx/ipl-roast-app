import google.generativeai as genai

genai.configure(api_key="AIzaSyDzy3uDwOYloP3BvKT8JYegj3w1fmJ-AWk")

for m in genai.list_models():
    print(m.name)