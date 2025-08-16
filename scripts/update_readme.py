import random
from jinja2 import Template

# 1. 定义每日问候语列表
greetings = [
    "Hello! Have a productive day! 🌞",
    "Keep coding and stay awesome! 💻",
    "New day, new opportunities! 🚀",
    "Keep pushing forward! 🔥",
    "Time to create something amazing! ✨"
]

# 2. 读取模板
with open("README_TEMPLATE.md", "r", encoding="utf-8") as f:
    template_content = f.read()

template = Template(template_content)

# 3. 随机选择问候语
greeting_today = random.choice(greetings)

# 4. 渲染模板
rendered = template.render(greeting=greeting_today)

# 5. 写入 README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(rendered)

print("README.md updated with today's greeting.")
