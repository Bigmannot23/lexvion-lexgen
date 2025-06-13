
# Lexgen CLI – Vertical AI Agent Engine

[![PyPI](https://img.shields.io/pypi/v/lexgen?color=brightgreen&label=install%20lexgen)](https://pypi.org/project/lexgen/)  
![Release](https://img.shields.io/badge/release-v0.1.0-blue?style=flat-square)

Lexgen is a CLI-first agent operating system.  
It deploys, logs, and monetizes vertical AI agents from YAML.

---

## 🚀 Features

- Run agents via CLI: `lexgen --template agent.yaml`
- Create new YAML templates
- Log to Airtable and alert on SLA errors
- CLI-native, vertical-ready

---

## 📦 Install

**TestPyPI**
```bash
pip install -i https://test.pypi.org/simple lexgen
```

**Production PyPI** (once uploaded live)
```bash
pip install lexgen
```

---

## 🧪 Demo

Run the included agent:
```bash
lexgen --template brief-agent.yaml
```

Output will appear in `/outputs/` or CLI log.

---

## 📄 YAML Agent Template

```yaml
agent: brief-agent
vertical: legal
task: summarize + format legal brief
format: docx
billing_unit: brief
```

---

## 📚 Docs  
https://lexvion.github.io/lexgen

## 📬 Contact  
alex@lexvionsol.com
