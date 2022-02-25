import bigIo

# start by organising projects by their score and completion time
# prioritise score (greedy)
# check we have enough people to assign to project if not enough skip
#   assignment, same skill level -> lower -> big boys
# check if enough people left to run another in parallel
# complete project(s)
# move to next n days
# hard deadline = deadline + score (past this is 0 dont bother)

# skills = {"skillname": [ordered workers], "skillname2": [ordered workers]}
#1. Use IO to input workers + max days + Project
projects = []
workers = []
workers, projects, skills = bigIo.read('a_an_example.in.txt')
# print(workers)
#3. sort the projects by score, then completion time if contention
projects.sort(reverse=True)
# print(projects)
# print(skills)

#3. work out the last completion time
latest_start = 0
for project in projects:
    latest_start = max(project.bestBefore + project.completionScore - project.duration, latest_start)
# print(latest_start)
#4. base for loop going through the days starting at day 0
remaining_projects = projects

in_progress_projects = []

solution = {}
projects_completed = 0

for day in range(latest_start+1):
    print(f"day: {day}")
    # print(f"skills: {skills}")
    #5. Start with highest scored task and assign members with minimum skills to match
    #6. (optional) if multiple people match, pick one with skill 0/1 below another skill so they level
    for project in in_progress_projects:
        if project.isFinished(day):
            print("finished projects", project.name)
            projects_completed += 1
            project.incrementWorkerSkills()
            solution[project.name] = project.workers
            for worker in project.workers:
                for skill in worker.skills:
                    if len(skills[skill])> 0:
                        for i, comparisonWorker in enumerate(skills[skill]):
                            if worker.skill> comparisonWorker.skill:
                                skills[skill].insert(i, worker)
                    else:
                        skills[skill].append(worker)
            in_progress_projects.remove(project)
    
    print(f"skills: {skills}")

    for project in remaining_projects:
        if not project.isTimeLeft(day):
            print(day, "no time", project.name)
            remaining_projects.remove(project)
        else:

            project_workers = []
            required_skills = project.skills
            possible_to_complete = True
            ###
            for skill_name, skill_level in required_skills.items():
                possible_workers = skills[skill_name]
                print(skill_name, skill_level, possible_workers)
                if len(possible_workers) > 0 and possible_workers[0].skills[skill_name] >= skill_level:
                    project_workers.append(possible_workers[0])
                else:
                    possible_to_complete = False
                    break
            if possible_to_complete:
                for worker in project_workers:
                    for skill in worker.skills:
                        skills[skill].remove(worker)
                project.addWorkers(project_workers)
                # print(f"selected project: {project.name}")
                remaining_projects.remove(project)
                in_progress_projects.append(project)
                project.startProject(day)
                print(in_progress_projects)
        ###
    
#9. Output to file
bigIo.output(solution)