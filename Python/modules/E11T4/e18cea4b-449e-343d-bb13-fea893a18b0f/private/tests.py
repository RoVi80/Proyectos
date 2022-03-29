#!/usr/bin/env python3
from unittest import TestCase
from git import Repo
from shutil import rmtree
import os
from private.utils import run, assert_commit_content, normalize

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
            if "git merge feature_x\n" in c or c.endswith("git merge feature_x"):
                m = "@@The command 'git merge' must not be interactive. Use the '-m' flag to provide a message.@@"
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

    def test_01a_correct_branches(self):
        r = Repo(dir_repo)
        actual = sorted([h.name for h in r.heads])

        if not actual:
            m = "@@No branches exist so far. Are you sure that you cloned the other repository?@@"
            self.fail(m)

        if "master" not in actual:
            m = "@@The 'master' branch cannot be found.@@"
            self.fail(m)

        if "feature_x" not in actual:
            m = "@@The 'feature_x' branch cannot be found.@@"
            self.fail(m)

        if len(actual) > 2:
            m = "@@Expected two branches, 'feature_x' and 'master', but additional branches could be found.@@"
            self.fail(m)

        if r.active_branch.name != "master":
            m = "@@After running the script, 'master' should be the active branch, but it is not.@@"
            self.fail(m)


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
        expected = ["hello.py"]

        if actual != expected:
            for a in actual:
                if a not in expected:
                    m = "@@The latest commit should not contain the file '{}'. Did you forget to merge?@@".format(a)
                    self.fail(m)
            for e in expected:
                if e not in actual:
                    m = "@@The latest commit should contain the file '{}', but it is missing.@@".format(e)
                    self.fail(m)

    def test_01e_correct_num_of_commits(self):
        r = Repo(dir_repo)
        cs = list(r.iter_commits('master', max_count=10))
        m = "@@Three new commits expected, but {} new found.@@".format(len(cs)-1)
        self.assertEqual(4, len(cs), m)

    def test_01f_old_commit_unchanged(self):
        r = Repo(dir_repo)
        if normalize(r.head.commit.message) != normalize("Merge 'feature_x'"):
            m = "@@Latest commit is not a merge commit or does not have the right commit message.@@"
            self.fail(m)

        prev = r.head.commit.parents[0].parents[0]
        if prev.hexsha != LAST_COMMIT_ID:
            self.fail("@@It seems that the original commit has been replaced by a new one.@@")
        if normalize(prev.message) != normalize("Some code that exist in the remote repository."):
            self.fail("@@It seems that the original commit message of the previous commit has changed.@@")

        assert_commit_content(r, prev, {"a.txt": ""}, "Original commit from remote")

    def test_01g_new_commits_correct_message(self):
        r = Repo(dir_repo)
        c = r.head.commit
        if c.message.lower().strip() != "merge \"feature_x\"":
            self.fail("@@Newest commit has incorrect commit message.@@")

        if len(c.parents) != 2:
            m = "@@The most recent (merge) commit should have two parents, which is not the case.@@"
            self.fail(m)

        msg0 = normalize(c.parents[0].message)
        msg1 = normalize(c.parents[1].message)

        msg_bye = "add \"good bye\" comment"
        if msg0 != msg_bye and msg1 != msg_bye:
            m = "@@One of the two parents of the merge commit should be the 'Good Bye' one.@@"
            self.fail(m)

        msg_hello = "add \"hello world\" example"
        if msg0 != msg_hello and msg1 != msg_hello:
            m = "@@One of the two parents of the merge commit should be the 'Hello World' one.@@"
            self.fail(m)

        pp_id = c.parents[0].parents[0].hexsha
        if pp_id != LAST_COMMIT_ID:
            m = "@@The parent-parent of the merge commit should be the last commit that exists on the remote.@@"
            self.fail(m)

    def test_01h_new_commits_correct_content(self):
        r = Repo(dir_repo)
        c = r.head.commit

        content_hello = {
            "hello.py": "print(\"Hello World!\")"
        }
        content_bye = {
            "bye.py": "# Good Bye"
        }
        assert_commit_content(r, c, content_hello)

        if len(c.parents) != 2:
            m = "@@The most recent (merge) commit should have two parents, which is not the case.@@"
            self.fail(m)

        msg_bye = normalize("add \"good bye\" comment")
        msg_hello = normalize("add \"hello world\" example")

        c0 = c.parents[0]
        c0_msg = normalize(c0.message)
        if c0_msg == msg_bye:
            assert_commit_content(r, c0, content_bye, "'Good bye' commit")
        elif c0_msg == msg_hello:
            assert_commit_content(r, c0, content_hello, "'Hello world' commit")
        else:
            m = "@@A parent of the merge commit is neither the 'Good bye', nor the 'Hello world' commits.@@"
            self.fail(m)

        c1 = c.parents[1]
        c1_msg = normalize(c1.message)
        if c1_msg == msg_bye:
            assert_commit_content(r, c1, content_bye, "'Good bye' commit")
        elif c1_msg == msg_hello:
            assert_commit_content(r, c1, content_hello, "'Hello world' commit")
        else:
            m = "@@A parent of the merge commit is neither the 'Good bye', nor the 'Hello world' commits.@@"
            self.fail(m)

        pp_sha = c.parents[0].parents[0].hexsha
        if pp_sha != LAST_COMMIT_ID:
            m = "@@The parent-parent of the merge commit should be the latest commit that exists on the remote.@@"
            self.fail(m)

    def test_02a_commit_pushed(self):
        r = Repo(dir_repo)
        rs = Repo(dir_shared_repo)

        local = r.head.commit.hexsha
        remote = rs.head.commit.hexsha

        actual = normalize(r.head.commit.message.lower().strip())
        expected = normalize("Merge \"feature_x\"")
        has_correct_msg = actual == expected
        if not has_correct_msg:
            m = "@@Latest local commit has incorrect commit message.@@"
            self.fail(m)
        if local != remote:
            m = "@@The latest local commit has not been pushed to the remote repository.@@"
            self.fail(m)

    def test_02b_feature_pushed(self):
        r = Repo(dir_repo)
        rs = Repo(dir_shared_repo)

        hs = sorted([h.name for h in rs.heads])

        if len(hs) != 2:
            m = "@@The remote repository should have exactly 2 branches, which is not the case.@@"
            self.fail(m)

        if "master" not in hs:
            m = "@@The remote repository does not have a 'master' branch. Did you delete it?@@"
            self.fail(m)

        if "feature_x" not in hs:
            m = "@@The remote repository does not have a 'feature_x' branch. Did you push it?@@"
            self.fail(m)

        for branch in ["master", "feature_x"]:
            hl = r.heads[branch].commit.hexsha
            hr = rs.heads[branch].commit.hexsha
            if hl != hr:
                m = "@@The branch '{}' points to a different commit on the remote.@@".format(branch)
                self.fail(m)

    def test_99_duplicate_01g_a(self): self.test_01g_new_commits_correct_message()
    def test_99_duplicate_01g_c(self): self.test_01g_new_commits_correct_message()
    def test_99_duplicate_01h_a(self): self.test_01h_new_commits_correct_content()
    def test_99_duplicate_01h_c(self): self.test_01h_new_commits_correct_content()
    def test_99_duplicate_02_b(self): self.test_02a_commit_pushed()
    def test_99_duplicate_02_c(self): self.test_02a_commit_pushed()
    def test_99_duplicate_02_b(self): self.test_02b_feature_pushed()
    def test_99_duplicate_02_c(self): self.test_02b_feature_pushed()
