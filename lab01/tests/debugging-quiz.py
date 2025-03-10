test = {
		'name'  : 'debugging-quiz',
		'points': 0,
		'suites': [
				{
						'cases' : [
								{
										'answer'   : '04c227bc171e79bdf2f704618b690d63',
										'choices'  : [
												'f("hi")',
												'g(x + x, x)',
												'h(x + y * 5)'
										],
										'hidden'   : False,
										'locked'   : True,
										'multiline': False,
										'question' : r"""
          In the following traceback, what is the most recent function call?
          Traceback (most recent call last):
              File "temp.py", line 10, in <module>
                f("hi")
              File "temp.py", line 2, in f
                return g(x + x, x)
              File "temp.py", line 5, in g
                return h(x + y * 5)
              File "temp.py", line 8, in h
                return x + 0
            TypeError: must be str, not int
          """
								},
								{
										'answer'   : 'e415098d79d97b14a9c3ed4bb799941c',
										'choices'  : [
												'the code attempted to add a string to an integer',
												'the code looped infinitely',
												'there was a missing return statement'
										],
										'hidden'   : False,
										'locked'   : True,
										'multiline': False,
										'question' : r"""
          In the following traceback, what is the cause of this error?
          Traceback (most recent call last):
              File "temp.py", line 10, in <module>
                f("hi")
              File "temp.py", line 2, in f
                return g(x + x, x)
              File "temp.py", line 5, in g
                return h(x + y * 5)
              File "temp.py", line 8, in h
                return x + 0
            TypeError: must be str, not int
          """
								},
								{
										'answer'   : '379a2d693f94542100c79dcbef881bf2',
										'choices'  : [
												r"""
												def square(x):
													'''
													doctest: (2, 4)
													'''
													return x * x
												""",
												r"""
												def square(x):
													'''
													input: 2
													output: 4
													'''
													return x * x
												""",
												r"""
												def square(x):
													'''
													square(2)
													4
													'''
													return x * x
												""",
												r"""
												def square(x):
													'''
													>>> square(2)
													4
													'''
													return x * x
												"""
										],
										'hidden'   : False,
										'locked'   : True,
										'multiline': False,
										'question' : 'How do you write a doctest asserting that square(2) == 4?'
								},
								{
										'answer'   : 'f48da7442af11bddcb273308a88a9970',
										'choices'  : [
												'For permanant debugging so you can have long term confidence in your code',
												'To ensure that certain conditions are true at certain points in your code',
												'To investigate the values of variables at certain points in your code'
										],
										'hidden'   : False,
										'locked'   : True,
										'multiline': False,
										'question' : 'When should you use print statements?'
								},
								{
										'answer'   : '57309603fab64e9deef8aab56ab89f9b',
										'choices'  : [
												"You don't need to do anything, ok only looks at returned values, not printed values",
												"Print with 'DEBUG:' at the front of the outputted line",
												'Print with # at the front of the outputted line'
										],
										'hidden'   : False,
										'locked'   : True,
										'multiline': False,
										'question' : 'How do you prevent the ok autograder from interpreting print statements as output?'
								},
								{
										'answer'   : '8a0e59465cbd3db201c83bad39a38190',
										'choices'  : [
												'python3 ok -q sum_digits -i',
												'python3 ok -q sum_digits --trace',
												'python3 ok -q sum_digits',
												'python3 -i lab01.py'
										],
										'hidden'   : False,
										'locked'   : True,
										'multiline': False,
										'question' : 'What is the best way to open an interactive terminal to investigate a failing test for question sum_digits in assignment lab01?'
								},
								{
										'answer'   : '5c1e38494cf0399527b69ad7bd7037f2',
										'choices'  : [
												'Code that returns a wrong answer instead of crashing is generally better as it at least works fine',
												'Testing is very important to ensure robust code',
												'Debugging is not a substitute for testing',
												'It is generally bad practice to release code with debugging print statements left in',
												'It is generally good practice to release code with assertion statements left in'
										],
										'hidden'   : False,
										'locked'   : True,
										'multiline': False,
										'question' : 'Which of the following is NOT true?'
								}
						],
						'scored': False,
						'type'  : 'concept'
				}
		]
}
