# Feature Flag Tag Prefixer

This script allows users to prefix all feature-flag-level tags with the key of the project they belong to. It is not maintained or officially endorsed by LaunchDarkly; it only serves as an example of how one might accomplish this if they wanted to. You are ultimately responsible for any API calls made using one of your keys.

> The actions taken by this script are NOT easily reversible!!! Before running it, take care to read and understand how it works.

## Instructions

1. Copy the `.env.example` file to `.env` and provide an API key with "Writer" level access.
2. Install the script's dependencies from `requirements.txt`.
3. Run `app.py`

By default, this will simply print out a list of all flags in all projects, with the prefixed tags that would be applied. You can output this list to a file for easier inspection (`python3 app.py > results.txt`).

If you review the list and are sure you would like to apply those changes to your live account, you can uncomment line 35 in `app.py` - this line contains the code that will make the API requests to replace your existing tags with the new ones.
