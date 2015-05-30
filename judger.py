from io import StringIO
from nose.core import TextTestRunner, TestProgram
from nose.config import Config
import re

class EmbedTestProgram(TestProgram):

    def runTests(self):
        """Run Tests. Returns true on success, false on failure, and sets
        self.success to the same value.
        """
        if self.testRunner is None:
            self.testRunner = TextTestRunner(
                stream=self.config.stream,
                verbosity=self.config.verbosity,
                config=self.config
            )
        plug_runner = self.config.plugins.prepareTestRunner(self.testRunner)
        if plug_runner is not None:
            self.testRunner = plug_runner
        self.result = self.testRunner.run(self.test)
        self.success = self.result.wasSuccessful()


def run_judge(q_pth, ans_text, module_name='judger'):
    buf = StringIO()
    nose_config = Config()
    nose_config.verbosity = 2
    nose_config.stream = buf
    q_tests_obj = read_question_case(q_pth)
    ans_obj = read_user_answer(ans_text)
    exec(q_tests_obj, globals())
    exec(ans_obj, globals())
    test_prog = EmbedTestProgram(
        defaultTest=module_name,
        argv=[''], exit=False, config=nose_config,
    )
    all_test_functions = [f for f in globals().keys() if f.startswith('test_')]
    # print(all_test_functions)
    for f in all_test_functions:
        del globals()[f]

    return test_prog, buf.getvalue()


def read_question_case(q_pth):
    with open(q_pth) as f:
        full_code_text = f.read()
    code_obj = compile(full_code_text, '<string>', 'exec')
    return code_obj

def read_user_answer(ans_text):
    code_obj = compile(ans_text, '<string>', 'exec')
    return code_obj
