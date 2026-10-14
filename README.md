# 💼 Django Simple Job Portal

A modern web-based job portal application built with **Django**. Designed to connect job seekers with employers, this platform enables companies to post job openings and manage applications while allowing candidates to browse, search, and apply for opportunities seamlessly.

---

## 🌟 Features

- **Job Postings & Management:** Employers can post, edit, and delete job listings with detailed requirements and skill tags.
- **Job Search & Filtering:** Applicants can search for open positions by job title, category, location, or required skills.
- **Application Workflow:** Job seekers can submit applications with resume/CV details and track application status.
- **User Authentication & Role-Based Access:** Separate access flows and dashboards for Job Seekers and Employers/Admins.
- **Admin Dashboard:** Full control over users, job listings, skills database, and submitted applications via the Django Admin panel.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, JavaScript, Tailwind CSS / Bootstrap
- **Database:** SQLite (Development) / PostgreSQL (Production ready)
- **Deployment:** PythonAnywhere / Render / Vercel

---

## 📁 Project Structure

```text
Django-simple-Job-Portal/
│
├── core/                   # Main project settings and configurations
├── jobs/                   # App managing job listings, categories, and search
├── applications/           # App handling application submissions and statuses
├── accounts/               # App managing user authentication and profiles
├── templates/              # HTML templates (job lists, details, dashboard)
├── static/                 # Static assets (CSS, JS, images)
├── db.sqlite3              # Local SQLite database
├── manage.py               # Django command-line utility
└── requirements.txt        # Project dependencies
