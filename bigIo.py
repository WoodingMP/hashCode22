
from models import Worker
from models import Project

def read(fname):
    fp = open(fname,'r')
    workers, projects = fp.readline().strip("\n").split(" ")
    workers = int(workers)
    projects = int(projects)
    # print("workers")
    workers_list = []
    projects_list = []
    skills_list = {}

    for i in range(workers):
        w, skills = fp.readline().strip("\n").split(" ")
        # print(f"Worker: {w}")
        skills_dict = {}
        for j in range(int(skills)):
            skill, level = fp.readline().strip("\n").split(" ")
            skills_dict[skill] = int(level)
            if skill not in skills_list:
                skills_list[skill] = []
            # print(f"skill: {fp.readline()}")
        worker = Worker(w, skills_dict)

        for skill in skills_dict:
            skills_list[skill].append(worker)

        workers_list.append(worker)
    
    # print(f"workers: {workers_list}")
    for i in range(projects):
        # x = fp.readline().split(" ")
        # print(x)
        name, days, score, best, roles = fp.readline().strip("\n").split(" ")
        # print(name, days, score, best, roles)
        skills_dict = {}
        for j in range(int(roles)):
            skill, level = fp.readline().strip("\n").split(" ")
            skills_dict[skill] = int(level)
            if skill not in skills_list:
                skills_list[skill] = []
            else:
                skills_list[skill].sort(key=lambda x: x.skills[skill], reverse=True)
            # print(f"skill: {fp.readline()}")
        project = Project(name, int(days), int(score), int(best), int(roles), skills_dict)
        projects_list.append(project)
    # print("projects")
    # stuff = line.split()
    # for q in data["Libs"]:
    #     q.display()
    return workers_list, projects_list, skills_list

# read('a_an_example.in.txt')


def output(solution):
    # dict
    f = open("solution.txt", "w")
    f.write(str(len(solution)))
    f.write("\n")
    for project in solution:
        f.write(project + "\n")
        workers = ""
        for worker in solution[project]:
            workers += worker.name + " "
        f.write(workers)
        f.write("\n")
    f.close()
    # for k, v in solution.items():
        
# 3 3
# Anna 1
# C++ 2
# Bob 2
# HTML 5
# CSS 5
# Maria 1
# Python 3
# Logging 5 10 5 1
# C++ 3
# WebServer 7 10 7 2
# HTML 3
# C++ 2
# WebChat 10 20 20 2
# Python 3
# HTML 3
