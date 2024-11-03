from Pytest_topics.conftest import cmd_opt


def test_argtest01(cmd_opt):
    # print(CmdOpt.readline())
    assert cmd_opt.readline().index("Text")