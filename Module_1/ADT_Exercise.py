from collections import Counter

job_skills = {
    "Data Scientist": ["Python", "SQL", "Machine Learning"],
    "Web Developer": ["HTML", "CSS", "JavaScript"],
    "Data Analyst": ["Excel", "SQL", "Data Visualization"],
    "Software Engineer": ["Python", "Java", "C++"],
    "Project Manager": ["Communication", "Leadership", "Organization"],
    "Data Engineerr": ["Python", "SQL", "Big Data"],
}


all_skills = sum(job_skills.values(), [])
skill_counts = Counter(all_skills)
print(skill_counts.most_common(3))
