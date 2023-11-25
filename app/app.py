from fastapi import FastAPI, status
from app.scrape import scrape_test, repos_scrape
app = FastAPI()

@app.get('/', status_code=status.HTTP_403_FORBIDDEN)
def root():
    return {"error": "please enter your username (eg: https://tk-ed.cyclic.app/TK-ed)"}

@app.get('/{name}', status_code=status.HTTP_202_ACCEPTED)
def scrape(name: str):
    url = f'https://www.github.com/{name}'
    return scrape_test(url)

@app.get('/repos/{name}')
def repo_scrape(name: str):
    url = f"https://www.github.com/{name}?tab=repositories"
    print(url)
    return repos_scrape(url, name)