# GitHub Activity CLI

A simple command-line tool that displays recent GitHub activity for a given user.
It fetches public events from the GitHub API and summarizes actions such as commits,
issues, stars, and pull requests per repository.

This project is inspired by the roadmap.sh backend project:
https://roadmap.sh/projects/github-user-activity

---

## Features

- Fetch recent public GitHub activity for any user
- Group activities by repository
- Display readable summaries such as:
  - Commits pushed
  - Issues opened
  - Comments on issues
  - Pull requests
  - Stars
- Installable as a global CLI command

---

## Installation

### Clone the repository

```bash
git clone https://github.com/andrew-NM/Task-Tracker-CLI.git
cd Task-Tracker-CLI
```
### Install locally (editable mode)

```bash
pip install -e .
```
---

## Usage

```bash
github-activity <username>
```
---

## Example
```bash
github-activity kamranahmedse
```
### output
```text
- Pushed 1 commit to andrew-NM/github-user-activity-cli
- Pushed 13 commits to andrew-NM/Task-Tracker-CLI
```
---

## Project Structure
```text
github_activity/
├── github_activity/
│   ├── __init__.py
│   └── cli.py
├── pyproject.toml
└── README.md
```
---

## Dependencies
* Python 3.8+
* requests
All dependencies are automatically installed via pip.

---

## Notes

* The tool uses GitHub’s public events API.

* Only supported event types are counted:

    * PushEvent

    * IssuesEvent

    * IssueCommentEvent

    * PullRequestEvent

    * WatchEvent

* Other event types are safely ignored.

* GitHub API rate limits may apply for unauthenticated request.

---

## License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.