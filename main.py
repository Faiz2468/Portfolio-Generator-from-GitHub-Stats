import requests
from jinja2 import Template
from datetime import datetime

# --- user settings ---
USERNAME = "faiz2468"
NAME = "Faiz"
TITLE = "IoT student"
SKILLS = "Python | Cloud (AWS, GCP) | IoT | TradingView Strategies"
LINKEDIN = "https://linkedin.com/in/..."
TWITTER = "https://twitter.com/..."
THEME = "radical"  # choose theme from https://github.com/anuraghazra/github-readme-stats#themes

# --- github api urls ---
repos_url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100"

# get repo data
try:
    r = requests.get(repos_url)
    repos = r.json()
except:
    print("uh oh can't fetch repos lol")
    repos = []

# sort repos by stars, descending
repos_sorted = sorted(repos, key=lambda x: x.get("stargazers_count", 0), reverse=True)

# pick top 5 projects
projects = []
for repo in repos_sorted[:5]:
    projects.append({
        "name": repo.get("name", "??"),
        "description": repo.get("description", "no description yet lol")
    })

# generate timestamp
LAST_UPDATED = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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
    twitter=TWITTER,
    theme=THEME,
    last_updated=LAST_UPDATED
)

# save the new readme
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("done! README.md updated with your TOP repos, theme, and timestamp ✨")