#!/usr/bin/env python3
import os, subprocess

def run(path_cmd, working_dir, vars={}):
    os.chmod(path_cmd, 0o755)
    os.chdir(working_dir)

    if vars:
        cmd = as_prefix(vars) + " " + path_cmd
    else:
        cmd = path_cmd

    print("executing '{}'...".format(cmd))
    out = subprocess.Popen(cmd,
                           cwd=working_dir,
                           shell=True,
                           stdout=2,
                           stderr=2)
    stdout, stderr = out.communicate()  # must be first thing to do

    if stdout:
        stdout = stdout.decode("UTF-8")
        print(stdout)

    if stderr:
        stderr = stderr.decode("UTF-8")
        print(stderr)

    if out.returncode != 0:
        script_name = os.path.realpath(path_cmd)
        m = "@@Failed to execute '{}'. (return code = {})@@".format(script_name, out.returncode)
        raise AssertionError(m)


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
        actual_content = normalize(r.git.show('{}:{}'.format(commit.hexsha, f)))
        expected_content = normalize(expected[f])
        m = "@@{}: Unexpected file content in '{}'.@@".format(prefix, f)
        assert expected_content == actual_content, m

def normalize(s):
    s = s.lower().strip()
    s = s.replace("'", "\"")
    return s