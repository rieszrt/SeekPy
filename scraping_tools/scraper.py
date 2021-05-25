import requests
from bs4 import BeautifulSoup as soup
import re,json

class Scraper():
    '''
    Manages the scraping of Seek.
    '''
    def __init__(self):
        pass
    def __get_page(self, url):
        '''
        Scrape jobs from a page of jobs on seek.
        :param url: url with classification and page query
        :return: Beautiful Soup of a page full of jobs
        '''
        headers = {
            'authority': 'www.seek.com.au',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'sec-ch-ua-mobile': '?0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }
        response = requests.get(url, headers=headers)
        page_soup = soup(response.content, "html.parser")
        return page_soup

    def get_jobs(self, page, classification, subclassification):
        '''
        Uses regular expression to parse html code for the javasript object containing all the jobs.
        :param page: page number
        :param classification: classification as defined in config.py
        :param subclassification: subclassification as defined in config.py
        :return: returns List of Dictionaries, each representing a job.
        '''
        url = f"https://www.seek.com.au/jobs?classification={classification}%2C6251&page={page}&sortmode=ListedDate&subclassification={subclassification}"
        page_soup = self.__get_page(url)
        js_snippet = page_soup.find("script", {"data-automation": "server-state"}).string
        json_text = re.findall("window.SEEK_REDUX_DATA = ({.*?});", js_snippet)[0]
        # json_text = re.sub("undefined","null",json_text)
        json_text = re.sub(r'("\s*:\s*)undefined(\s*[,}])', '\\1null\\2', json_text)
        SEEK_REDUX_DATA = json.loads(json_text)
        jobs = SEEK_REDUX_DATA["results"]["results"]["jobs"]
        return jobs

    def get_job_detail(self, job_id):
        '''
        Gets the job description for a specific job
        :param job_id: job id
        :return: Job Descrtiption
        '''
        url = f"https://www.seek.com.au/job/{job_id}"
        page_soup = self.__get_page(url)
        jobAdDetails = page_soup.find('div', {'class': 'FYwKg WaMPc_4'})
        details = []
        for c in jobAdDetails.children:
            details.append({c.name: c.text})

        return details
