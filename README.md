# Managing Security Across Multiple Environments with DevSecOps

## 🧭 Objective

This project demonstrates how to build a minimal DevSecOps pipeline that manages security across development and simulated production environments using open-source tools like **Semgrep** and **Trivy**.

---

## 🛠️ Environments Setup

- **Development Environment:** Localhost/Docker container running a simple web app.
- **Production Environment:** Simulated via another Docker container or port to demonstrate multi-environment configuration.

---

## ⚙️ CI/CD Workflow

A GitHub Actions pipeline is triggered on changes to `README.md` or the `docs/` folder. It performs:

1. **Code Checkout**  
2. **Docker Build**  
3. **SAST (Static Application Security Testing)** using **Semgrep**  
4. **Container Vulnerability Scanning** using **Trivy**

---

## 🔐 Security Tools Used

| Tool      | Purpose                         |
|-----------|----------------------------------|
| **Semgrep** | Static code analysis (SAST)       |
| **Trivy**   | Docker image + dependency scan   |

---

## 🛠️ Fix Example

- Upgraded `flask` to a secure version (`flask==2.3.3`)
- Removed unused dependencies from `requirements.txt`
- Reran both scans to ensure vulnerabilities were resolved ✅

---

## 🚀 How to Run Locally

```bash
# Build Docker image
docker build -t myapp:latest .

# Run container
docker run -p 5000:5000 myapp:latest

# Access the app at:
http://localhost:5000
