import requests
import time

# Gets all flags for a given project
def get_all_flags(project_key, base_url, headers):
    flags_endpoint = base_url + '/flags/' + project_key
    f = requests.get(flags_endpoint, headers=headers)
    
    all_flags = f.json()['items']
    return all_flags

# Apply project name as prefix to the flag name, returns a new list
def create_prefixed_tags(tag_list, project_key):
    separator = '-'
    return [project_key + separator + tag for tag in tag_list]

# Replace a flag's tags with their prefixed versions
def update_tags(project_key, base_url, headers, flag_key, new_flag_list):
    flag_endpoint = base_url + '/flags/' + project_key + '/' + flag_key
    
    # https://apidocs.launchdarkly.com/reference#updates
    data = [
        {
            'op': 'replace',
            'path': '/tags',
            'value': new_flag_list
        }
    ]
    
    f = requests.patch(flag_endpoint, headers=headers, json=data)
    
    # Wait 10s and retry if rate limited
    if f.status_code == 429:
        time.sleep(10)
        update_tags(project_key, base_url, headers, flag_key, new_flag_list)
    elif f.status_code == 200:
        print(f'Tags updated for flag: {flag_key}')
    else:
        print(f'Unable to prefix flag: {flag_key}')
        print(f.status_code)