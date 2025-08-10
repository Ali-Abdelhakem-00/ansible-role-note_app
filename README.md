# ansible-role-note_app

## Description
This Ansible role deploys a Flask-based note-taking web application with a SQLite database on an AWS EC2 instance.

## Requirements
- Python 3
- Flask
- SQLite

## Role Variables
No special variables required.

## Example Playbook
```yaml
- hosts: web
  roles:
    - note_app
