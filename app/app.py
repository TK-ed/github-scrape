from fastapi import FastAPI
from app.scrape import scrape_test
app = FastAPI()

@app.get('/')
def root():
    return {"hello": "world!!"}

@app.post('/{name}')
def scrape(name: str):
    url = f'https://www.github.com/{name}'
    return scrape_test(url)

