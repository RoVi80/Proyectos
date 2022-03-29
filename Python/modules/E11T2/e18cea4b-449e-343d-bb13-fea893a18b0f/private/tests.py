#!/usr/bin/env python3
from unittest import TestCase
from git import Repo
from shutil import rmtree
from os import walk
import os, subprocess

os.chdir("public")
base_dir = os.getcwd()
path_script = base_dir + "/script.sh"
print("base_dir: {}".format(base_dir))
print("script_location: {}".format(path_script))


class GitTest(TestCase):

    @classmethod
    def tearDownClass(cls):
        try: rmtree(".git")
        except: pass
        for f in ["a.txt", "b.txt"]:
            try: os.unlink(f)
            except: pass

    def test_0a_no_commit_message(self):
        with open(path_script, "r") as f:
            c = f.read()
            if "git commit\n" in c or c.endswith("git commit"):
                m = "@@The command 'git commit' must not be interactive. Use the '-m' flag to provide a message.@@"
                self.fail(m)

    def test_0b_run_script(self):
        os.chmod(path_script, 0o755)

        vars = {}
        cmd = as_prefix(vars) + " " + path_script
        print("executing '{}'...".format(cmd))
        out = subprocess.Popen(cmd,
                               cwd=base_dir,
                               shell=True,
                               stdout=2,
                               stderr=2)
        stdout, _ = out.communicate()  # must be first thing to do

        if stdout:
            stdout = stdout.decode("UTF-8")
            print(stdout)

        if out.returncode != 0:
            m = "@@Script execution failed (return code = {}).@@".format(out.returncode)
            raise AssertionError(m)

    def test_1a_git_init(self):
        try:
            Repo(base_dir)
        except:
            self.fail("@@Failed to open the repository. Did you init? Did you accidentally switch to another folder?@@")

    def test_1b_no_weird_files(self):
        expected_dirs = [".git", "__pycache__"]
        expected_files = ["a.txt", "b.txt", "script.sh", "tests.py", "__init__.py"]
        for r, ds, fs in walk(base_dir):
            for d in ds:
                if d not in expected_dirs:
                    m = "@@Folder contains unexpected directory '{}'.@@".format(d)
                    self.fail(m)
            for f in fs:
                if f not in expected_files:
                    m = "@@Folder contains unexpected file '{}'.@@".format(f)
                    self.fail(m)
            break # first level is enough

    def test_2a_correct_branches(self):
        r = Repo(base_dir)
        m = "@@Right now, 'master' is not the active branch.@@"
        self.assertEqual("master", r.active_branch.name, m)

        actual = sorted([h.name for h in r.heads])
        expected = ["master"]

        if not actual:
            m = "@@No branches exist so far. Did you commit anything?@@"
            self.fail(m)

        m = "@@Apart from 'master', no other branches should exist.@@"
        self.assertEqual(expected, actual, m)

    def test_2b_correct_tracking(self):
        r = Repo(base_dir)
        c = r.head.commit
        actual = list(reversed(sorted(r.git.execute(['git', 'ls-tree', '--name-only', c.hexsha, "."]).split())))
        expected = ["a.txt", "b.txt"]

        if actual != expected:
            for a in actual:
                if a not in expected:
                    m = "@@The file '{}' should not have been added.@@".format(a)
                    self.fail(m)
            for e in expected:
                if e not in actual:
                    m = "@@The file '{}' has not been added yet.@@".format(e)
                    self.fail(m)

    def test_2c_dirty_working_tree(self):
        r = Repo(base_dir)
        has_staged_files = r.is_dirty(index=False, working_tree=True)
        m = "@@You have open changes (in tracked files) that are not yet added to the index.@@"
        assert not has_staged_files, m

    def test_2d_dirty_index(self):
        r = Repo(base_dir)
        has_staged_files = r.is_dirty(index=True, working_tree=False)
        m = "@@The index contains staged files that are not yet committed.@@"
        assert not has_staged_files, m

    def test_3_two_commits(self):
        r = Repo(base_dir)
        log = r.head.log()
        m = "@@Two commits expected, but {} found.@@".format(len(log))
        self.assertEqual(2, len(log), m)

    def test_4a_first_commit_message(self):
        r = Repo(base_dir)
        log = r.head.log()
        actual = log[-2].message.lower().strip()
        expected = "commit (initial): add files a.txt and b.txt"
        m = "@@First commit does not have the expected commit message.@@"
        self.assertEqual(expected, actual, m)

    def test_4b_first_commit_content(self):
        r = Repo(base_dir)
        commit = r.head.commit.parents[0]
        expected = {
            "a.txt": "aaa",
            "b.txt": "bbb",
        }
        assert_commit_content(r, commit, expected, "Incorrect result for first commit")

    def test_5a_second_commit_message(self):
        r = Repo(base_dir)
        log = r.head.log()
        actual = log[-1].message.lower().strip()
        expected = "commit: add second line to b.txt"
        m = "@@Second commit does not have the expected commit message.@@"
        self.assertEqual(expected, actual, m)

    def test_6b_second_commit_content(self):
        r = Repo(base_dir)
        commit = r.head.commit
        expected = {
            "b.txt": "bbb\nb2",
        }
        assert_commit_content(r, commit, expected, "Incorrect result for second commit")


def as_prefix(vars):
    mappings = ['{}="{}"'.format(k, vars[k]) for k in vars.keys()]
    prefix = " ".join(mappings)
    return prefix


def assert_file_content(path, content):
    if not os.path.exists(path) or not os.path.isfile(path):
        m = "@@The file '{}. does not exist.@@".format(path)
        raise AssertionError(m)

    with open(path, "r") as f:
        c = f.read().lower().strip()
        m = "@@The file '{}' has unexpected contents.@@".format(path)
        assert c == content, m


def assert_commit_content(r, commit, expected, prefix="Unexpected"):

        actual_files = sorted(commit.stats.files.keys())
        expected_files = sorted(expected.keys())
        m = "@@{}: Expected to find the files {} in the commit, but found {}.@@"
        m = m.format(prefix, expected_files, actual_files)
        assert expected_files == actual_files, m

        for f in expected.keys():
            actual_content = r.git.show('{}:{}'.format(commit.hexsha, f))
            expected_content = expected[f]
            m = "@@{}: Unexpected file content in '{}'.@@".format(prefix, f)
            assert expected_content == actual_content, m
