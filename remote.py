from github import Github
import os, time

g = Github("USERNAME", "PASSWORD")
reponame = input("Please name your new repository (lowercase and use - for spaces):")
user = g.get_user()
repo = user.create_repo(reponame)
repo.create_file("README.md", "Create Repository", "Readme for %s" % reponame)


try:
    os.mkdir(reponame)
except OSError:
    print("Creation of the file has failed")
else:
    print("File %s successfully created" % reponame)
time.sleep(3)

os.chdir("PATH" + reponame)
file_name = "README.md"
f = open(file_name, "a+")  # open file in append mode
f.write("Readme for %s" % reponame)
f.close()
