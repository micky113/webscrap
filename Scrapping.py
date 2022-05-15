from bs4 import BeautifulSoup
import requests
import time
print("mention skill u are unfamiliar with")
unfam_skill=input('>')
print(f'filtering out {unfam_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35')
    soup = BeautifulSoup(html_text.text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        posted = job.find('span', class_='sim-posted').text
        if 'today' in posted:
            compname = job.find('h3', class_='joblist-comp-name').text.replace(" ", "")
            skills = job.find('span', class_='srp-skills').text.replace(" ", "")
            more_info = job.header.h2.a['href']
            if unfam_skill not in skills:
                with open('posts/{index}.txt','w')as f:
                    f.write(f"Company name: {compname.strip()}\n")
                    f.write(f"Skill req: {skills.strip()}\n")
                    f.write(f"More info: {more_info}")
                print(f'File Saved: {index}')

if __name__=='__main__':
    while True:
        find_jobs()
        time_wait =0.10
        print(f'waiting {time_wait}minutes...')
        time.sleep(time_wait * 2)
