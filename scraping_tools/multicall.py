import threading


class Multicall():
    '''
    Given a task Object, Multicall runs multiple threads of it's add jobs method.
    '''
    def __init__(self, task):
        self.task = task
        self.threads = []
        self.batchSize = 50  # seek doesn't show more than page 200

    def __complete_tasks(self):
        '''
        Completes and joins threads in batches
        :return: None
        '''
        print('new batch')
        [t.start() for t in self.threads]
        [t.join() for t in self.threads]
        self.threads = []

    def multicall_jobs(self, classification, subClassification):
        '''
        Creates a list of threading tasks, each scraping a specific page of a classification and outputing it to jobs/
        :return: None
        '''
        self.terminate = False
        print(f"Starting scraping of ({classification},{subClassification})")
        for page in range(1,self.batchSize):
            self.threads.append(threading.Thread(target=self.task.add_jobs, args=(page,classification,subClassification)))
        self.__complete_tasks()