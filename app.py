from dotenv import load_dotenv
load_dotenv()

import os
import requests
from helpers import create_prefixed_tags, get_all_flags, update_tags

API_KEY = os.environ.get('LD_API_KEY')
base_url = 'https://app.launchdarkly.com/api/v2'
headers = { 
    'Authorization': API_KEY, # Set up authentication using the API key from .env file
    'Content-Type': 'application/json'
}

# Request all projects in the account
projects_endpoint = base_url + '/projects'
p = requests.get(projects_endpoint, headers=headers)

# Get each project's key
all_projects = p.json()['items']
project_keys = [project['key'] for project in all_projects]

# Iterate over projects to get flags for each and update their tags
for project in project_keys:
    print(f'Project: {project}')
    all_flags = get_all_flags(project, base_url, headers)
    
    # Iterate over flags in each project and apply the prefix to all tags
    for flag in all_flags:
        print(f'Flag: {flag["key"]}')
        all_tags = flag['tags']
        all_tags_prefixed = create_prefixed_tags(all_tags, project)

        print(all_tags_prefixed)
        #update_tags(project, base_url, headers, flag['key'], all_tags_prefixed)