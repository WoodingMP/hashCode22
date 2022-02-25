from dataclasses import dataclass

@dataclass
class Project:
    name: str
    duration: int
    completionScore: int
    bestBefore: int
    roles: int
    skills: dict[str, int]
    score: int

    def __init__(self, name:str, duration:int, completionScore:int, bestBefore:int, roles:int):
        self.name = name
        self.duration = duration
        self.completionScore = completionScore
        self.bestBefore = bestBefore
        self.roles = roles
    
    def calcScore(self,dayCompleted) -> int:
        score = max(0, self.completionScore + min(0, self.bestBefore - dayCompleted))
        return score

    pass

p = Project("Logging", 5, 10, 5, 1)
print (p.calcScore(16))