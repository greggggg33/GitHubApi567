import GitHubApi
import unittest
from unittest import mock

class TestGetNumOfCommits(unittest.TestCase):
    @mock.patch('GitHubApi.getNumOfCommits')
    def test_get_commits_A(self, mockedReq):
        mockedReq.return_value = {"GitHubApi567": 15, "greggggg33": 2, "SSW-555-Project": 3, "SSW567-Triangle": 24, "SSW567-Student-Repository": 4, "SSW-567": 5}
        self.assertEqual(GitHubApi.getNumOfCommits("greggggg33"), 
        {"GitHubApi567": 15, "greggggg33": 2, "SSW-555-Project": 3, "SSW567-Triangle": 24, "SSW567-Student-Repository": 4, "SSW-567": 5})
        self.assertEqual(len(GitHubApi.getNumOfCommits("greggggg33")), 6)
        self.assertIn("GitHubApi567", GitHubApi.getNumOfCommits("greggggg33"))
    
    @mock.patch('GitHubApi.getNumOfCommits')
    def test_get_commits_B(self, mockedReq):
        mockedReq.return_value = {"RepoA": 13, "RepoB": 203}
        self.assertEqual(GitHubApi.getNumOfCommits("greggggg33").get("RepoA"), 13)
        self.assertEqual(len(GitHubApi.getNumOfCommits("greggggg33")), 2)

if __name__ == "__main__":
    print('------------ Running Unit Tests ------------')
    unittest.main()