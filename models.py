from dataclasses import dataclass

class Project:
    name: str
    duration: int
    completionScore: int
    bestBefore: int
    roles: int
    skills: dict[str, int]

    def __init__(self, name, duration, completionScore, bestBefore, roles, skills):
        self.name = name
        self.duration = duration
        self.completionScore = completionScore
        self.bestBefore = bestBefore
        self.roles = roles
        self.skills = skills
        self.workers = []
        self.projectStartTime = 0
        self.isStarted = False
    
    def calcScore(self,dayCompleted) -> int:
        score = max(0, self.completionScore + min(0, self.bestBefore - dayCompleted))
        return score

    def __eq__(self, other):
        return self.completionScore == other.completionScore and self.duration == other.duration

    def __lt__(self, other):
        return self.completionScore < other.completionScore or (self.completionScore == other.completionScore and self.duration > other.duration)

    def __gt__(self, other):
        return self.completionScore > other.completionScore or (self.completionScore == other.completionScore and self.duration < other.duration)
        
    def __repr__(self):
        return f"Project(name: {self.name}, duration: {self.duration}, score: {self.completionScore}, bestBefore: {self.bestBefore}, roles: {self.roles}, skills: {self.skills}, workers: {self.workers})"

    def addWorkers(self, workers):
        self.workers = workers
    
    def isTimeLeft(self, currentDay):
        return currentDay + self.duration <= self.bestBefore + self.completionScore
    
    def startProject(self, currentDay):
        self.projectStartTime = currentDay
        self.isStarted = True
    
    def isFinished(self, currentDay):
        # print(f"checking is finished name: {self.name } start: {self.projectStartTime} , duration: {self.duration}, current day: {currentDay}, started: {self.isStarted}")
        return self.isStarted and currentDay >= self.projectStartTime + self.duration

    def incrementWorkerSkills(self):
        for skill in self.skills:
            for worker in self.workers:
                if skill in worker.skills and (worker.skills[skill]== self.skills[skill] or worker.skills[skill] == self.skills[skill] -1):
                    worker.skills[skill] += 1



class Worker:
    name: str
    skills: dict[str, int]

    def __init__(self,name, skills):
        self.skills = skills
        self.name = name
    
    def __repr__(self):
        return f"Worker(name: {self.name} , skills: {self.skills})"

