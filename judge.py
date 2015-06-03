from io import StringIO
from nose.core import TextTestRunner, TestProgram
from nose.config import Config

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


def run_judge(q_pth, ans_text, module_name='judge'):
    """Judge the submiited answer by nose test

    Inject code into **runtime environment** and delete injected answers.
    It's super hacky becuase I guess the web server will somehow reuse
    a pool of processes.
    """
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
    for f in all_test_functions:
        del globals()[f]

    return test_prog, buf.getvalue()


def read_question_case(q_pth):
    with q_pth.open() as f:
        full_code_text = f.read()
    code_obj = compile(full_code_text, '<string>', 'exec')
    return code_obj

def read_user_answer(ans_text):
    code_obj = compile(ans_text, '<string>', 'exec')
    return code_obj


def read_question(q_pth):
    doc_string = []
    answer_example = []
    with q_pth.open() as f:
        # read doc string
        for line in f:
            if line.strip() in ["'''", '"""']:
                break
            doc_string.append(line)

        # read answer example
        reading_ans = False
        for line in f:
            if line.startswith('def answer('):
                reading_ans = True
            if not reading_ans:
                continue
            answer_example.append(line)
            if line.startswith('    return '):
                break
    doc_string[0] = doc_string[0][len("'''"):]
    q_name, q_desc = doc_string[0][len('Question '):].split(': ', 1)
    doc_string = doc_string[2:]
    return q_name, q_desc, ''.join(doc_string), ''.join(answer_example)

