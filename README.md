# 🚀 SEO Auditor CLI Tool

[![Docker Pulls](https://img.shields.io/docker/pulls/robertcalvindev/seo-auditor.svg)](https://hub.docker.com/r/robertcalvindev/seo-auditor)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://hub.docker.com/r/robertcalvindev/seo-auditor)

## ⭐ About
Production-grade SEO audit CLI tool that crawls websites, analyzes SEO structure, and generates professional CSV/HTML reports. Includes optional email reporting and Docker support.

---

## 🔎 Features
- Recursive internal crawling
- Page status codes & load time capture
- Title and meta length validation
- Missing ALT detection on images
- Broken link reporting
- Duplicate title/meta detection
- CSV & HTML report generation
- Optional SMTP email report delivery

---

## ✅ Local CLI Usage

### Clone the repository:
```bash
git clone https://github.com/robert-calvin-dev/seo-auditor.git
cd seo-auditor
```

### Set up virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run locally:
```bash
python -m seo_auditor.cli https://example.com
```

### With email (requires smtp.json in `seo_auditor/config/`):
```bash
python -m seo_auditor.cli https://example.com --email
```

---

## 🐳 Docker Usage
```bash
docker pull robertcalvindev/seo-auditor:latest
```

### Basic run:
```bash
docker run --rm -v "$(pwd)/reports:/app/reports" robertcalvindev/seo-auditor https://example.com
```

### With email:
```bash
docker run --rm \
  -v "$(pwd)/reports:/app/reports" \
  -v "$(pwd)/smtp.json:/app/seo_auditor/config/smtp.json" \
  robertcalvindev/seo-auditor https://example.com --email
```

---

## 📧 SMTP Configuration Example (smtp.json):
```json
{
  "smtp_server": "smtp.yourprovider.com",
  "smtp_port": 587,
  "sender": "you@example.com",
  "password": "your-app-password",
  "recipient": "recipient@example.com"
}
```

---

## 📝 License
This project is licensed under the MIT License.

---

## 🙌 Maintainer
**Robert Mitchell** — AI & Web Developer / Prompt Engineer

- [Docker Hub Repository](https://hub.docker.com/repository/docker/robertcalvindev/seo-auditor/general)
- [GitHub Repository](https://github.com/robert-calvin-dev/seo-auditor)
