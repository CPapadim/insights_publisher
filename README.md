# kr_publisher

Publish helper for airbnb/knowledge-repo

```
usage: publisher [-h] [--notebook_path NOTEBOOK_PATH]
                 [--report_path REPORT_PATH] [--repo REPO]
                 {preview,add,publish,index} ...

Publish a Jupyter notebook to Knowledge Repo and link to its git remote and
commit ID.

positional arguments:
  {preview,add,publish,index}
                        sub-commands
    preview             Preview post.
    add                 Submit post for review
    publish             Publish post
    index               Refresh the index to make new posts discoverable

optional arguments:
  -h, --help            show this help message and exit

general arguments:
  --notebook_path NOTEBOOK_PATH
                        The path to the Jupyter notebook to publish.
  --report_path REPORT_PATH
                        The path to which to publish the report.
  --repo REPO           The knowledge repository uri.

```

Ties publishing to version control.

When attempting to publish a file, the file must be part of a git repo.

Publisher will then pull the file from the git remote master branch and publish it.  If the git remote is different from the user's local repo, warnings will be issued to instruct the user to push any changes that should show up in the report to the remote repo.

Also adds a cell containing a link to the remote repo, the specific commit for the publication, and the specific file in the commit.

Only supports .ipynb formats!


## Usage:

```
Add a post:  

$ publisher --repo "uri/or/path/to/repo" --notebook_path /path/to/notebook.ipynb --report_path path/to/project/and/report.kp add
```
```
Update a post:

$ publisher --repo "uri/or/path/to/repo" --notebook_path /path/to/notebook.ipynb --report_path path/to/project/and/report.kp add --update
```
```
Preview: 

$ publisher --repo "uri/or/path/to/repo" --report_path path/to/project/and/report.kp preview --host www.repohost.com --port 443 --protocol https
```

```
Publish: 

$ publisher --repo "uri/or/path/to/repo" --report_path path/to/project/and/report.kp publish
```


Publisher also allows manual indexing without re-indexing already indexed posts.  This should work with stock Knowledge Repo, but is designed for a custom version that that also has functionality to skip setting up indexing timers, for one-time indexing after post publication. 

```
Manually Update Index:

$ publisher --repo "uri/or/path/to/repo" index --config path/to/config.py
```



