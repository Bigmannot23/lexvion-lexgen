Lexgen CLI – Vertical AI Agent Engine

Lexgen is a CLI-first agent operating system.
It deploys, logs, and monetizes vertical AI agents from YAML.

⸻

🚀 Features
	•	Run agents via CLI: lexgen run --template agent.yaml
	•	Create new templates: lexgen template --init agent-name
	•	Track execution: push run logs to Airtable, alert on error/SLA
	•	Built-in agent registry + output folder system

⸻

📦 Install

pip install -i https://test.pypi.org/simple lexgen


⸻

📄 YAML Agent Example

agent: brief-agent
vertical: legal
task: summarize + format legal brief
format: docx
billing_unit: brief


⸻

📚 Docs

🔗 https://lexvion.github.io/lexgen

⸻

👥 Contributing

Want to add a new agent? See CONTRIBUTING.md

⸻

📬 Contact

alex@lexvionsol.com
www.lexvionsol.com/demo
