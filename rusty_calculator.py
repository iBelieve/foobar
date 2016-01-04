"""
Rusty calculator
================

Lab minion Rusty works for Professor Boolean, a mad scientist. He's been stuck
in this dead-end job crunching numbers all day since 1969. And it's not even
the cool type of number-crunching - all he does is addition and multiplication.
To make matters worse, under strict orders from Professor Boolean, the only
kind of calculator minions are allowed to touch is the Unix dc utility, which
uses reverse Polish notation.

Recall that reverse Polish calculators such as dc push numbers from the input
onto a stack. When a binary operator (like "+" or "*") is encountered, they pop
the top two numbers, and then push the result of applying the operator to them.

For example:
2 3 * => 6
4 9 + 2 * 3 + => 13 2 * 3 + => 26 3 + => 29

Each day, Professor Boolean sends the minions some strings representing
equations, which take the form of single digits separated by "+" or "*",
without parentheses. To make Rusty's work easier, write function called
answer(str) that takes such a string and returns the lexicographically largest
string representing the same equation but in reverse Polish notation.

All numbers in the output must appear in the same order as they did in the
input. So, even though "32+" is lexicographically larger than "23+", the
expected answer for "2+3" is "23+".

Note that all numbers are single-digit, so no spaces are required in the
answer. Further, only the characters [0-9+*] are permitted in the input and
output.

The number of digits in the input to answer will not exceed 100.

Test cases
==========

Inputs:
	(string) str = "2+3*2"
Output:
	(string) "232*+"

Inputs:
	(string) str = "2*4*3+9*3+5"
Output:
	(string) "243**93*5++"
"""


def answer(str):
	# Make these properties on answer so Python doesn't try to create
	# local variables in the nested functions
	answer.output = ''
	answer.index = 0

	op_stack = []

	def current_op():
		"""Return the currently active operator"""
		if len(op_stack) > 0:
			return op_stack[-1]['op']
		else:
			return None

	def update_op(op):
		"""Update the count of currently active operator or replace it if necessary"""
		if op == current_op():
			op_stack[-1]['count'] += 1
		else:
			op_stack.append(dict(op=op, count=1))

	def pop_op():
		"""Apply the current operator"""
		op_info = op_stack.pop()
		for i in range(op_info['count']):
			answer.output += op_info['op']

	def next_token():
		token = str[answer.index]
		answer.index += 1
		return token

	def has_more():
		return answer.index < len(str)

	# Addition is always performed last, with multiplication only when necessary
	# (specifically, when completing multiplication and switching back to addition)
	while has_more():
		number = next_token()

		if has_more():
			op = next_token()

			answer.output += number

			# Multiplication must be finished before starting addition
			if current_op() == '*' and op == '+':
				pop_op()

			update_op(op)
		else:
			# The number was the last token, so add it to the ouput
			# and apply all remaining operators
			answer.output += number
			while len(op_stack) > 0:
				pop_op()

	return answer.output
