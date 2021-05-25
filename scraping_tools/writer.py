import json
import threading
from datetime import date

class Writer():
    '''
    Manages the writing of jobs to jobs/ using threading Lock to prevent conflicts.
    '''
    def __init__(self):
        self.lock = threading.Lock()
        today = date.today()
        # Month abbreviation, day and year
        self.file_date = today.strftime("%b-%d-%Y")

    def write_job(self, newJob, classification, subClassification):
        '''
        Writes a job to jobs/{CURRENT_DAY}.json where CURRENT_DAY follows the format %b-%d-%Y
        :param newJob: Dictinary of a new job
        :param classification: classification as defined in config.py
        :param subClassification: classification as defined in config.py
        :return: None
        '''
        #Add to jobs
        with open(f"jobs/{self.file_date}.json", "a") as f:
            f.write('\n' +
                    json.dumps(
                        {"classification": classification,
                         "subClassification": subClassification,
                         "data": newJob}
                    )
                    )

    def append_jobs(self, newJobs, classification, subClassification):
        try:
            self.lock.acquire()
            for job in newJobs:
                self.write_job(job,classification,subClassification)
        except:
            pass
        finally:
            self.lock.release()

    def append_details(self, data, job_id):
        if data and \
                not (job_id in self.seenJobs):
            try:
                self.lock.acquire()
                with open("details.json", "a") as f:
                    f.write(
                        json.dumps(
                            {"job_id": job_id,
                             "data": data}
                        )
                    )
            except:
                pass
            finally:
                self.lock.release()