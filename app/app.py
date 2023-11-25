from fastapi import FastAPI, status
from app.scrape import scrape_test, repos_scrape
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/', status_code=status.HTTP_200_OK)
def root():
    return {"error": "please enter your username (eg: https://tk-ed.cyclic.app/TK-ed) or explore the documentation (https://tk-ed.cyclic.app/docs) for all apis"}

@app.get('/{name}', status_code=status.HTTP_202_ACCEPTED)
def scrape(name: str):
    url = f'https://www.github.com/{name}'
    return scrape_test(url)
    
@app.get('/repos/{name}', status_code=status.HTTP_202_ACCEPTED)
def repo_scrape(name: str):
    url = f"https://www.github.com/{name}?tab=repositories"
    print(url)
    return repos_scrape(url, name)
    