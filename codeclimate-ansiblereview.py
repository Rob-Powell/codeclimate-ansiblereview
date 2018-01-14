#!/bin/python
import yaml
import subprocess

try:
    with open('.codeclimate.yml', 'r') as f:
        doc = yaml.load(f)
except:
    pass
else:
    try:
        standardsrepozip = doc['engines']['ansiblereview']['config']['rules_zip']
    except:
        pass
    try:
        workdir = doc['engines']['ansiblereview']['config']['work_dir']
    except:
        pass
    try:
        standards = doc['engines']['ansiblereview']['config']['standards_dir']
    except:
        pass
    try:
        lint = doc['engines']['ansiblereview']['config']['lint_dir']
    except:
        pass
    try:
        searchmethod = doc['engines']['ansiblereview']['config']['search_method']
    except:
        searchcommand = "git ls-files"
    else:
        if searchmethod == "find":
            searchcommand = "find . -type f"
        else:
            searchcommand = "git ls-files"
    try:
        debug = doc['engines']['ansiblereview']['config']['debug']
    except:
        debug = ""
    else:
        debug = " -vv"


cmd = searchcommand + " | xargs /usr/src/app/ansible-review/bin/ansible-review -t -w " + workdir + " -g " + standardsrepozip + " -d " + standards + " -r " + lint + debug
ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
output = ps.communicate()[0]
print output
