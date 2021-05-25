# %%
from scraping_tools.scraper import Scraper
from scraping_tools.task import Task
from scraping_tools.writer import Writer
from scraping_tools.multicall import Multicall
from scraping_tools.filter import Filter
import scraping_tools.config as config
import json

def get_newJobs():
    # interests = ["Banking & Financial Services", "Consulting & Strategy",
    #              "Government & Defence", "Information & Communication Technology", "Insurance & Superannuation",
    #              "Marketing & Communications", "Science & Technology"]

    scraper = Scraper()
    writer = Writer()
    filter = Filter()
    task = Task(writer, scraper, filter)
    multicall = Multicall(task)

    for classification in config.job_classes:
        for subClassification in classification['subClassifications']:
            multicall.multicall_jobs(classification['id'],subClassification['id'])


get_newJobs()