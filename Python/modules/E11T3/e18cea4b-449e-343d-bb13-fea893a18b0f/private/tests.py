#!/usr/bin/env python3
from unittest import TestCase
from git import Repo
from shutil import rmtree
import os
from private.utils import run, assert_commit_content

dir_base = os.getcwd()
dir_public = dir_base + "/public"
dir_shared_repo = dir_base + "/shared-repo"
dir_repo = dir_base + "/public/repo"

path_script = dir_public + "/script.sh"
path_setup = dir_base + "/private/setup.sh"

print("dir_base: {}".format(dir_base))
print("dir_public: {}".format(dir_public))
print("dir_shared_repo: {}".format(dir_shared_repo))
print("dir_repo: {}".format(dir_repo))
print("path_script: {}".format(path_script))
print("path_setup: {}".format(path_setup))

LAST_COMMIT_ID = None

class GitTest(TestCase):

    @classmethod
    def tearDownClass(cls):
        for d in ["shared-repo", "../shared-repo", "public/repo", "repo"]:
            try: rmtree(d)
            except: pass
        for f in ["a.txt", "b.txt"]:
            try: os.unlink(f)
            except: pass


    def test_00a_no_commit_message(self):
        with open(path_script, "r") as f:
            c = f.read()
            if "git commit\n" in c or c.endswith("git commit"):
                m = "@@The command 'git commit' must not be interactive. Use the '-m' flag to provide a message.@@"
                self.fail(m)

    def test_00b_no_url(self):
        with open(path_script, "r") as f:
            c = f.read()
            if "$REPO_URL" not in c:
                m = "@@You are not using the variable that points to the repository, make sure to use $REPO_URL.@@"
                self.fail(m)

    def test_00c_run_script(self):
        # first setup the repo...
        run(path_setup, dir_base)
        r = Repo(dir_shared_repo)
        global LAST_COMMIT_ID
        LAST_COMMIT_ID = r.head.commit.hexsha
        # ...and then run the student script
        os.chdir(dir_public)
        run(path_script, dir_public, {"REPO_URL": dir_shared_repo})

    def test_00d_wrong_folder(self):
        if os.path.exists(dir_base + "/public/shared-repo"):
            m = "@@You cloned the repository, but you did not specify the correct target directory 'repo'.@@"
            self.fail(m)

    def test_00f_folder_does_not_exist(self):
        if not os.path.exists(dir_repo):
            m = "@@The expected directory 'repo' does not exist.@@"
            self.fail(m)

    def test_00g_open_repo(self):
        try:
            Repo(dir_repo)
        except:
            m = "@@Failed to open the repository in directory 'repo'.@@"
            self.fail(m)

    def test_00h_correct_file_location(self):
        if os.path.exists(dir_public + "/c.txt"):
            m = "@@It seems that you did not change the directory and created files outside your repository clone.@@"
            self.fail(m)
        if not os.path.exists(dir_repo + "/c.txt"):
            m = "@@The expected file 'c.txt' does not exist.@@"
            self.fail(m)

    def test_01a_correct_branches(self):
        r = Repo(dir_repo)
        m = "@@Right now, 'master' is not the active branch in your repository.@@"
        self.assertEqual("master", r.active_branch.name, m)

        actual = sorted([h.name for h in r.heads])
        expected = ["master"]

        if not actual:
            m = "@@No branches exist so far. Are you sure that you cloned the other repository?@@"
            self.fail(m)

        m = "@@Apart from 'master', no other branches should exist.@@"
        self.assertEqual(expected, actual, m)

    def test_01a_no_untracked_files(self):
        r = Repo(dir_repo)
        has_staged_files = not not r.untracked_files
        m = "@@You have untracked files that are not yet added to the index.@@"
        assert not has_staged_files, m

    def test_01b_clean_working_dir(self):
        r = Repo(dir_repo)
        has_staged_files = r.is_dirty(index=False, working_tree=True)
        m = "@@You have open changes (in tracked files) that are not yet added to the index.@@"
        assert not has_staged_files, m

    def test_01c_clean_index(self):
        r = Repo(dir_repo)
        has_staged_files = r.is_dirty(index=True, working_tree=False)
        m = "@@The index contains staged files that are not yet committed.@@"
        assert not has_staged_files, m

    def test_01d_only_right_files_committed(self):
        r = Repo(dir_repo)
        c = r.head.commit

        if c.hexsha == LAST_COMMIT_ID:
            self.fail("@@HEAD is still pointing at the old commit.@@")

        actual = sorted(c.stats.files.keys())
        expected = ["c.txt"]

        if actual != expected:
            for a in actual:
                if a not in expected:
                    m = "@@The file '{}' should not have been added to the commit.@@".format(a)
                    self.fail(m)
            for e in expected:
                if e not in actual:
                    m = "@@The file '{}' is missing in the commit.@@".format(e)
                    self.fail(m)

    def test_01e_correct_num_of_commits(self):
        r = Repo(dir_repo)
        log = r.head.log()
        m = "@@Expecting exactly two commits in repository (1 new, 1 pre-existing), but {} were found.@@".format(len(log))
        self.assertEqual(2, len(log), m)

    def test_01f_old_commit_unchanged(self):
        r = Repo(dir_repo)
        prev = r.head.commit.parents[0]
        if prev.hexsha != LAST_COMMIT_ID:
            self.fail("@@It seems that the original commit has been replaced by a new one.@@")
        if prev.message != "Some changes that exist in the remote repository.\n":
            self.fail("@@It seems that the original commit message of the previous commit has changed.@@")

        assert_commit_content(r, prev, {"a.txt": ""}, "Previous commit")

    def test_01g_new_commit_correct_message(self):
        r = Repo(dir_repo)
        c = r.head.commit
        if c.message.lower().strip() != "add new file c.txt with some content":
            self.fail("@@Newest commit has incorrect commit message.@@")

    def test_01h_new_commit_correct_content(self):
        r = Repo(dir_repo)
        c = r.head.commit
        expected = {
            "c.txt": "ccc"
        }
        assert_commit_content(r, c, expected, "Incorrect result for newest commit")

    def test_02_commit_pushed(self):
        r = Repo(dir_repo)
        rs = Repo(dir_shared_repo)

        local = r.head.commit.hexsha
        remote = rs.head.commit.hexsha

        actual = r.head.commit.message.lower().strip()
        expected = "add new file c.txt with some content"
        has_correct_msg = actual == expected
        if not has_correct_msg:
            m = "@@Incorrect commit message or not yet pushed.@@"
            self.fail(m)
        if local != remote:
            m = "@@The local commit has not been pushed to the remote repository.@@"
            self.fail(m)


    def test_99_duplicate_01g_a(self): self.test_01g_new_commit_correct_message()
    def test_99_duplicate_01g_b(self): self.test_01g_new_commit_correct_message()
    def test_99_duplicate_01g_c(self): self.test_01g_new_commit_correct_message()
    def test_99_duplicate_01h_a(self): self.test_01h_new_commit_correct_content()
    def test_99_duplicate_01h_b(self): self.test_01h_new_commit_correct_content()
    def test_99_duplicate_01h_c(self): self.test_01h_new_commit_correct_content()
    def test_99_duplicate_02_a(self): self.test_02_commit_pushed()
    def test_99_duplicate_02_b(self): self.test_02_commit_pushed()
    def test_99_duplicate_02_c(self): self.test_02_commit_pushed()
