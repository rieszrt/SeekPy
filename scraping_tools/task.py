class Task():
    '''
    A well defined scraping task.
    '''
    def __init__(self,writer,scraper,filter):
        '''
        Creates a task
        :param writer: Writer Object - Manages the output of scraped jobs to the jobs/ directory
        :param scraper: Sraper Object - Manages of scraping data from Seek
        :param filter: Filter Object - Manages the removal of seen jobs from being duplicated
        '''
        self.writer = writer
        self.scraper = scraper
        self.filter = filter

    def add_jobs(self, page, classification, subClassification):
        '''
        Scrapes jobs on page `page` under classification and writes it to jobs/
        :param page: page number
        :param classification: classification as defined in config.py
        :param subClassification: subclassification as defined in config.py
        :return:
        '''
        jobs = self.scraper.get_jobs(page, classification, subClassification)
        newJobs = self.filter.filter_batchJobs(jobs)
        self.writer.append_jobs(newJobs, classification, subClassification)

