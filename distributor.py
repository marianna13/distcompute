
import random
import os
import datetime


class Client:
    def __init__(self, sample_list):
        now = str(datetime.datetime.now()).replace(' ', '-')
        output_dir = f'TRACKER/{now}'
        os.makedirs(output_dir)
        self.sample_list = sample_list
        self.tracker_dir = f'{output_dir}/tracker.txt'
        self.save(sample_list)

    def save(self, data):
        with open(self.tracker_dir, 'w') as f:
            for line in data:
                f.write(f"{line}\n")
    
    def delete(self, job_id):
        with open(self.tracker_dir, "r+") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                if i != job_id:
                    f.write(i)
            f.truncate()
        

    def get_job(self):
        job_id = random.choice(self.sample_list)
        self.sample_list.remove(job_id)
        return job_id

    def complete_job(self, job_id):
        self.delete(job_id)
    
    def alive(self):
        return len(self.sample_list) > 0
