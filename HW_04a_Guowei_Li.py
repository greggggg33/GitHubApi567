import json
import requests
import unittest
#author: Guowei Li
"""You should write a function that will take as input a GitHub user ID. 
The output from the function will be a list of the names of the repositories that the user has, along with the number of commits that are in each of the listed repositories."""
def getNumOfCommits(ID: str):
    userID = ID
    repo = "https://api.github.com/users/" + userID + "/repos" #convert User ID into a GitHub API that shows all the repos"
    repoUrl = requests.get(repo)
    repoDic = json.loads(repoUrl.text) #create a python dictionary that contains all the repos
    myDic = {}
    for repo in repoDic:
        repoName = repo["name"] #get the name of the repo
        commits = "https://api.github.com/repos/" + userID + "/" + repoName + "/commits" # get the GitHub API that have all the commits details
        commitsUrl = requests.get(commits)
        commitsDic = json.loads(commitsUrl.text)
        numOfCommits = len(commitsDic) #get the number of commits of this repo
        myDic[repoName] = numOfCommits
    print("For User ID: " + userID)
    for repo in myDic:
        print("Repo: " + repo + "Number of commits: " + str(myDic[repo])) #Output a list of the names of the repositories that the user has, along with the number of commits that are in each of the listed repositories.
    return myDic

class TestGetNumOfCommits(unittest.TestCase):
    def test_get_commits(self):
        self.assertEqual(getNumOfCommits("greggggg33"),{'GitHubApi567': 12, 'greggggg33': 2, 'SSW-555-Project': 3, 'SSW567-Triangle': 13, 'Student-Repository': 3, 'SW-567': 4})

if __name__ == "__main__":
    unittest.main()