# Antigravity Online Exam Portal

A premium, glassmorphism-inspired Online Examination platform built with Django.

## Features
- **Modern UI/UX**: Stunning dark mode with Teal/Indigo accents and glassmorphism effects.
- **Course & Lesson Management**: Easily manage courses and their associated lessons via the Django Admin.
- **Online Assessments**: Professional quiz interface with real-time score calculation.
- **Python 3.14 Compatible**: Optimized for the latest Python environments using Django 6.x.

## Tech Stack
- **Backend**: Django 6.0.4
- **Frontend**: Bootstrap 5.3 + Custom Glassmorphism CSS
- **Styling**: Google Fonts (Outfit)

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Start Development Server**:
   ```bash
   python manage.py runserver
   ```

4. **Populate Sample Data** (Optional):
   ```bash
   python populate_data.py
   ```

Access the admin panel at `/admin/` with credentials `admin` / `adminpass`.
