

# class for memory list
class MemoryList:

    def __init__(self, memory_size: int, job=None, job_size=0, status=None, internal_fragmentation=0):
        self.memory_size = memory_size
        self.job = job
        self.job_size = job_size
        self.status = status
        self.internal_fragmentation = internal_fragmentation

# class for jobs done by device
class Jobs:

    def __init__(self, name, size):
        self.name = name
        self.size = size

# jobs
J1 = Jobs('JOB 1', 10000)
J2 = Jobs('JOB 2', 20000)
J3 = Jobs('JOB 3', 30000)
J4 = Jobs('JOB 4', 10000)

# memory lists
ML1 = MemoryList(30000)
ML2 = MemoryList(15000)
ML3 = MemoryList(50000)
ML4 = MemoryList(20000)

ALL_JOBS = [J1, J2, J3, J4]
ALL_MEMORY_ROWS = [ML1, ML2, ML3, ML4]
WAITING_JOBS = []

MEMORY_SIZES = []
for i,memory in enumerate(ALL_MEMORY_ROWS):
    MEMORY_SIZES.append((memory.memory_size, i))
MEMORY_SIZES.sort()
print(MEMORY_SIZES)

for k in MEMORY_SIZES:
    for job in ALL_JOBS:
            if job.size <= k[0]:
                if memory.status == 'BUSY!':
                    pass
                else:
                    ALL_MEMORY_ROWS[k[1]].job = job.name
                    ALL_MEMORY_ROWS[k[1]].job_size = job.size
                    ALL_MEMORY_ROWS[k[1]].status = 'BUSY!'
                    ALL_MEMORY_ROWS[k[1]].internal_fragmentation = memory.memory_size - job.size
                    ALL_JOBS.remove(job)

'''
for memory in ALL_MEMORY_ROWS:
    for i,job in enumerate(ALL_JOBS):
            if job.size <= memory.si:
                if memory.status == 'BUSY!':
                    pass
                else:
                    memory.job = job.name
                    memory.job_size = job.size
                    memory.status = 'BUSY!'
                    memory.internal_fragmentation = memory.memory_size-job.size
                    ALL_JOBS.remove(job)
            else:
                WAITING_JOBS.append(job)
'''

print('Memory Size\tJob\tJob Size\tStatus\tInternal Fragmentation')
for memory in ALL_MEMORY_ROWS:
    print(f'{memory.memory_size}\t\t{memory.job}\t{memory.job_size}\t{memory.status}\t{memory.internal_fragmentation}')





