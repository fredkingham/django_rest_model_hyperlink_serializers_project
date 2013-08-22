env.key_filename = "add.pem"
env.hosts = ["insert ip address"]
env.user = "remote-user"
REMOTE_DIR = "/home/ec2-user/figg_project"
LOCAL_DIR = "figg"
STATIC_DIR = "front_end/static"
PUBLIC_STATIC_DIR = os.path.join(STATIC_DIR, "public")
REMOTE = "%s/figg" % REMOTE_DIR
REMOTE_SETTINGS_DIR = "%s/figg" % REMOTE


class Project(object):
    def __init__(self, name):
        self.project_dir = "%s_project" % name
        self.application_dir = os.path.join(self.project_dir, name)
        self.front_end_dir = os.path.join(self.application_dir, "front_end")
        self.app_name = name


@task
def push_to_prod():
    with prefix("source /usr/local/bin/virtualenvwrapper.sh && workon figg"):
        with lcd(LOCAL_DIR):
            local("pip freeze > requirements.txt")
#    local('git commit -a -m "updating files"')
    local("git push origin master")

    with lcd(os.path.join(LOCAL_DIR, STATIC_DIR)):
            local("../node_modules/brunch/bin/brunch build -o")

    rsync_project(remote_dir=REMOTE_DIR, local_dir=LOCAL_DIR, delete=True)

    with cd(REMOTE_SETTINGS_DIR):
        sed("settings.py", "DEBUG = True", "DEBUG = False")
    with cd(REMOTE):
        run("~/.virtualenvs/figg/bin/python manage.py syncdb")

    execute(replace_js)

    with cd(REMOTE):
        with prefix("source /usr/bin/virtualenvwrapper.sh && workon figg"):
            run("pip install -r requirements.txt")

    sudo("service httpd restart")


@task
def replace_js():
    with cd(REMOTE):
        now = datetime.now()
        v = "-v%d%d%d" % (now.day, now.hour, now.minute)
        for ending in ["js", "css"]:
            site_base = run("find . -name 'site_base.html'")
            starter = run("find . -name 'starter.html'")
            output_static = run("find %s -name '*.%s'" % (PUBLIC_STATIC_DIR, ending))
            static_files = output_static.split("\n")

            for static_file in static_files:
                static_file = static_file.strip()
                new_file_name = static_file.replace(".%s" % ending, "%s.%s" % (v, ending))
                run("mv %s %s" % (static_file, new_file_name))
                original_name = os.path.basename(static_file)
                new_name = os.path.basename(new_file_name)
                sed(site_base, original_name, new_name)
                sed(starter, original_name, new_name)


@task
def sync_from_prod():
     with lcd(LOCAL_DIR):
       with cd(REMOTE):
           with prefix("source /usr/bin/virtualenvwrapper.sh && workon figg"):
               run("./manage.py dumpdata")
               get("dump.rdb")
               local("./manage.py flush")
               local("./manage.py loaddata")