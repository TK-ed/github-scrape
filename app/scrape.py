from bs4 import BeautifulSoup
from fastapi import HTTPException, status
import requests


def scrape_test(data: str):
    page = requests.get(data)
    if not page:
        # return {"error": "The page doesnt exist or theres an issue with your connection"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Something's fishy here!!")
    soup = BeautifulSoup(page.text, 'lxml')

    # User_name
    try:
        user_name = soup.find(
            'span', class_='p-nickname vcard-username d-block').text.replace('\n', '').strip()
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Something's fishy here!!")

    # Followers and Following
    try:
        followers = soup.find('span', class_='text-bold color-fg-default').text
        following = soup.find_all('span', class_='text-bold color-fg-default')
        for i in following[1]:
            following = i.text
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Something's fishy here!!")

    # Repositories
    try:
        total_repos = soup.find('span', class_='Counter').text
        popu_repos = soup.find(
            'div', class_='js-pinned-items-reorder-container')
        popular_repos = []
        for i in popu_repos.find_all("span", class_="repo"):
            repo = i.text.strip()
            popular_repos.append(repo)
        contributions = soup.find(
            'h2', class_='f4 text-normal mb-2').text.replace('\n', '').strip().split()[0]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Something's fishy here!!")

    # Bio
    # try:
    #     bio = soup.find_all('ul').split()
    #     print(bio)
    # except Exception as e:
    #     print(e)
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        #                     detail="Something's fishy here!!")

    return {'username': user_name, 'followers': followers, 'following': following, 'total_repos': total_repos, 'popular-repos': popular_repos, 'contributions': contributions}
