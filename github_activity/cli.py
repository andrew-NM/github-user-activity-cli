import sys
import requests
import json

def help():
    print("Usage:")
    print("  python main.py <username>")
    
def display_activities(repos: dict):
    for repo_id, events in repos.items():
        repo_name = events.pop("name")
        for event, value in events.items():
            if value:
                if event == "PushEvent":
                    print(f"- Pushed {value} commits to {repo_name}")
                elif event == "IssuesEvent":
                    print(f"- Opened a new issue in {repo_name}")
                elif event == "WatchEvent":
                    print(f"- Starred {repo_name}")
                elif event == "IssueCommentEvent":
                    print(f"- Commented on issue in {repo_name}")
                else:
                    print(f"- Pulled {value} requests from {repo_name}")

def fetch_user(username):
    api_response = requests.get(f"https://api.github.com/users/{username}/events")
    activities = json.loads(api_response.text)
    repos = {}
    if api_response.status_code == 404:
        print("There is no user with this username")
    else:
        for activity in activities:
            repo_id, repo_name = activity["repo"]["id"], activity["repo"]["name"]
            event = activity["type"]
            if repo_id not in repos:
                repos[repo_id] = {
                    "name": None,
                    "PushEvent": 0,
                    "IssuesEvent": 0,
                    "IssueCommentEvent": 0,
                    "PullRequestEvent": 0,
                    "WatchEvent": 0
                }   
                repos[repo_id]["name"] = repo_name
            if event in repos[repo_id]:
                repos[repo_id][event] += 1
        display_activities(repos)

def main():
    if len(sys.argv) < 2:
        help()
    elif len(sys.argv) == 2:
        fetch_user(sys.argv[1])
    else:
        print("Invalid command!")
        help()
