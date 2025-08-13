# Hey there 👋  
i'm {{ name }}, an {{ title }} chasing the Cloud ☁️  

![Profile Views](https://komarev.com/ghpvc/?username={{ username }}&color=blue)
![GitHub Trophies](https://github-profile-trophy.vercel.app/?username={{ username }}&theme={{ theme }})

![GitHub Stats](https://github-readme-stats.vercel.app/api?username={{ username }}&show_icons=true&theme={{ theme }})
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username={{ username }}&layout=compact&theme={{ theme }})

## 🔥 Streak
[![GitHub Streak](https://github-readme-streak-stats.herokuapp.com?user={{ username }}&theme={{ theme }})](https://git.io/streak-stats)

## 📌 Featured Projects
{% for project in projects %}
- **{{ project.name }}** – {{ project.description }}
{% endfor %}

## 💡 Skills
{{ skills }}

## 📫 Contact
[LinkedIn]({{ linkedin }}) | [Twitter]({{ twitter }})

---

_Last updated: {{ last_updated }}_