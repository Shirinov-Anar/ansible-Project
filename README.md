# Ansible-Project

An automation repository built with **Ansible**, designed to deploy a MySQL database server and a Dockerized Flask web application across separate hosts. This project demonstrates full infrastructure automation, including DB setup, remote access configuration, Docker deployment, and environment variable management with Ansible Vault.

---

## Project Structure

.
├── ansible.cfg # Ansible configuration file
├── app/ # Flask web application code
│ ├── app.py
│ └── requirements.txt
├── Dockerfile # Dockerfile to build Flask app image
├── group_vars/ # Group-specific variables
│ ├── db.yml
│ └── web.yml
├── hosts # Inventory file with DB and web hosts
├── playbooks/ # Main playbooks
│ ├── db.yml
│ ├── site.yml
│ └── web.yml
├── roles/ # Ansible roles
│ ├── database/
│ │ ├── tasks/main.yml
│ │ ├── handlers/main.yml
│ │ ├── templates/my.cnf.j2
│ │ └── vars/main.yml
│ └── webapp/
│ ├── tasks/main.yml
│ ├── templates/config.j2
│ └── vars/main.yml
└── vault.yml # Encrypted secrets managed by Ansible Vault


---

## What It Does

### Database (DB) host `[db]`
- Installs MySQL server if not already present
- Ensures MySQL service is running and enabled on boot
- Configures MySQL to listen on `0.0.0.0` to allow remote connections from the web server
- Opens MySQL port `3306` in the firewall
- Creates a MySQL user with privileges for remote access from the web server

### Web host `[web]`
- Installs Docker and Python Docker libraries on the web server
- Copies the Flask application and Dockerfile to the remote host
- Renders `/tmp/config.env` from the `roles/webapp/templates/config.j2` template using variables from Ansible Vault
- Builds a Docker image for the web application
- Runs the Docker container with environment variables from `/tmp/config.env` and exposes the application on the defined port

---

## Prerequisites

1. Two servers (can be VMs):
   - One for MySQL DB (e.g., `192.168.1.73`)
   - One for Flask web app (e.g., `192.168.1.69`)
2. Control machine (your local computer) with:
   - Ansible installed (`ansible >= 2.10`)
   - Python 3
3. SSH access to both servers
4. Git installed to clone the repository

---

## Inventory Setup

Edit `hosts` file to include your target servers:

```ini
[web]
192.168.1.69

[db]
192.168.1.73
#Replace IPs with your actual server addresses

##Vault File

Create or edit vault.yml to store sensitive credentials:

vault_db_host: 192.168.1.73
vault_db_name: mydb
vault_db_user: appuser
vault_db_password: mysecretpassword
vault_web_host: 192.168.1.69
vault_app_name: myapp
vault_app_port: 5000
vault_docker_image: myapp_image
vault_docker_container: myapp_container
