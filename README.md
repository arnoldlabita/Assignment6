# 📸 Photo Album Management System

A production‑ready Django application for managing photo albums with role‑based access control (RBAC), cloud storage integration, and PostgreSQL database support. Deployed on [Render](https://render.com).

---

## 🚀 Features
- **Class‑Based Views (CBVs)** for clean, maintainable CRUD operations.
- **Role‑Based Access Control (RBAC)** using Django’s authentication system:
  - Standard users can create and manage their own albums.
  - Album Admins can manage all albums.
- **Cloudinary Integration** for media storage (no local media files in production).
- **PostgreSQL Database** provisioned via Render.
- **Whitenoise** for efficient static file serving in production.
- **Bootstrap 5 Templates** for a professional UI.

---

## 🛠 Tech Stack
- **Backend:** Django (Python)
- **Database:** PostgreSQL (Render)
- **Media Storage:** Cloudinary
- **Deployment:** Render
- **Frontend:** Bootstrap 5

---

## ⚙️ Installation (Local Development)

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/photo_album_system.git
   cd photo_album_system
