import requests
from jinja2 import Template

# user settings
USERNAME = "faiz2468"      # ur github username
NAME = "Faiz"              # ur name
TITLE = "IoT student"      # what u r
SKILLS = "Python | Cloud (AWS, GCP) | IoT | TradingView Strategies"
LINKEDIN = "https://linkedin.com/in/..." 
TWITTER = "https://twitter.com/..." 

# github api urls
repos_url = f"https://api.github.com/users/{USERNAME}/repos"

# get repo data
try:
    r = requests.get(repos_url)
    repos = r.json()
except:
    print("uh oh can't fetch repos lol")
    repos = []

# only pick some projects (max 3 just for looks)
projects = []
for repo in repos[:3]:
    projects.append({
        "name": repo.get("name", "??"),
        "description": repo.get("description", "no description yet lol")
    })

# read the template file
with open("template.md", "r", encoding="utf-8") as f:
    t = Template(f.read())

# render it with data
readme_content = t.render(
    name=NAME,
    title=TITLE,
    username=USERNAME,
    projects=projects,
    skills=SKILLS,
    linkedin=LINKEDIN,
    twitter=TWITTER
)

# save the new readme
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("done! README.md updated with ur cool stats ✨")