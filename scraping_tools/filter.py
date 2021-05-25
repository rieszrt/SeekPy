class Filter():
    '''
    Controls flow of new jobs. Checks to make sure all new jobs added have not been seen.
    '''
    def __init__(self):
        self.read_seenJobs()


    def filter_batchJobs(self,batchJobs):
        '''
        Efficiently filters the batched jobs with seen jobs using Intersection of sets.
        :param batchJobs: Batch jobs output from Scraper
        :return: Unseen Jobs
        '''
        #Create a dictionary, use strings
        batchJobs_dict = {}
        for job in batchJobs:
            batchJobs_dict[job['id']] = job
        idSet = set(batchJobs_dict.keys())
        newJobIds = idSet-self.seenJobs
        newJobs = [batchJobs_dict[i] for i in newJobIds]
        self.addSeenJobs(newJobIds)
        print(f"{len(batchJobs)} batch jobs, {len(newJobs)} new jobs")
        return newJobs

    def addSeenJobs(self,newJobIds):
        '''
        Add unseen job Ids to seenJobs
        :param newJobIds:
        :return: None
        '''
        with open('scraping_tools/seenJobs.json',"a") as f:
            for _id in newJobIds:
                f.write('\n'+str(_id))
                self.seenJobs.add(_id)

    def read_seenJobs(self):
        '''
        Load scraping_tools/seenJobs.json as attribute
        :return: None
        '''
        self.seenJobs = set()
        for row in open('scraping_tools/seenJobs.json'):
            if row.strip():
                self.seenJobs.add(int(row.strip()))