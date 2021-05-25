# Seek jobs Python Library

A Python library to Data scrape and interact with Seek. 

## Data Scraping
Classes used for data scraping are contained in scraping_tools. 

### Setup
To install the requirements run:

    pip install -r requirements.txt

### Scrape all jobs
    python3 main.py

### Reading the data
New Jobs are saved in the *jobs/* directory as json objects with the date they were scraped on.
However, there may be blank rows so read the data like this:
    
    import json

    for row in open("jobs/May-21-2021.json") as f:
        if row.strip():
            job = json.loads(row.strip())
            print(job)

### Jobs Json format
The jobs each row contain

```json
{
  {"classification": 1200, "subClassification": 6140, 
    "data": {
      "id": 52334494, 
      "listingDate": "2021-05-20T05:37:24Z", 
      "title": "Administration Officer", 
      "teaser": "We are seeking a highly organised and professional Admin Officer to provide general administration support to our team.", 
      "bulletPoints": [], 
      "advertiser": {"id": "20748186", "description": "Japara Healthcare"}, 
      "logo": {"id": "", "description": null}, 
      "isPremium": false, 
      "isStandOut": false, 
      "location": "Melbourne", 
      "locationId": 1002, 
      "area": "Bayside & South Eastern Suburbs", 
      "areaId": 5070, 
      "suburbId": 18085, 
      "workType": "Full Time", 
      "classification": {"id": "6251", "description": "Administration & Office Support"}, 
      "subClassification": {"id": "6252", "description": "Administrative Assistants"}, 
      "salary": "", "companyProfileStructuredDataId": 2403, 
      "companyName": "Japara Healthcare", 
      "locationWhereValue": "All Melbourne VIC", 
      "areaWhereValue": "Bayside & South Eastern Suburbs Melbourne VIC", 
      "suburbWhereValue": "Brighton VIC 3186", 
      "automaticInclusion": false, 
      "displayType": "standard", 
      "tracking": "ewogICJ0b2tlbiI6ICIwMDk3Yjc1Ni1hMjRhLTRjNzQtYWMyNC1hMjhmNDRiZGQ2MWZfMSIKfQ==", 
      "templateFileName": "ptmpl_1.htm", "roleId": "administration-officer", 
      "solMetadata": {"searchRequestToken": "eab4083a-26ba-41f2-b73f-cea1bfb56cd5",
        "jobId": "52334494", "section": "MAIN", "sectionRank": 1, 
        "jobAdType": "ORGANIC", "tags": {"mordor:flights": "mordor_73"}}, 
      "branding": null, "isPrivateAdvertiser": false}}
}
```




## Mechanism
The most important class is the **Task** which defines a scraping, writing and filtering operation.


**Task** takes a **Scraper**, a **Filter** and a **Writer** Object which it uses to:
1. **Scrape** jobs from Seek
2. **Filter** Scraped jobs for duplicates in existing database
3. **Write** to the jobs/ directory

respectively.

**Multicall** runs Task in parallel, so multiple pages can be scraped at once. On Seek, any query for page>200 results in 
a blank page.

### Writer
Manages the writing of scraped jobs to *jobs/*.

### Filter
Prevents the addition of duplicate jobs into *jobs/*.

### Scraper
Scrapes jobs from Seek website using Beautiful Soup

### Task
A Task object with: **Writer**, **Filter** and **Scraper** with a single add_job method that deligates jobs to the other classes.

### Multicall
Runs **Tasks** Object's add_job method in parallel for faster scraping.

### config.py
Contains the classification and subclassification codes used by Seek in queries.
