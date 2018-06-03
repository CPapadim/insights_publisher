# kr_publisher

Publish helper for airbnb/knowledge-repo

```
Publish a Jupyter notebook to Knowledge Repo and link to its git remote and
commit ID.

optional arguments:
  -h, --help            show this help message and exit

required arguments:
  --notebook_path NOTEBOOK_PATH
                        The path to the Jupyter notebook to publish.
  --report_path REPORT_PATH
                        The path to which to publish the report.
  --repo REPO           The repo or database to pass to the `$ knowledge_repo`
                        call.
```

Ties publishing to version control.

When attempting to publish a file, the file must be part of a git repo.

Publisher will then pull the file from the git remote master branch and publish it.  If the git remote is different from the user's local repo, warnings will be issued to instruct the user to push any changes that should show up in the report to the remote repo.

Also adds a cell containing a link to the remote repo, the specific commit for the publication, and the specific file in the commit.

Only supports .ipynb formats!


## Usage:

```
$ ./publisher --notebook_path /path/to/notebook.ipynb --report_path path/to/project/and/report --repo path/to/knowledge_repo/storage
```


