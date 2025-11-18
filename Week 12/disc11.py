'''
Q1: Representing Expressions
Write the Scheme expression in Scheme syntax represented by each Link below. Try drawing the linked list diagram too.
>>> Link('+', Link(1, Link(Link('*', Link(2, Link(3, nil))), nil)))
(+ 1 (* 2 3))
>>> Link('and', Link(Link('<', Link(1, Link(0, nil))), Link(Link('/', Link(1, Link(0, nil))), nil)))
(and (< 1 0) (/ 1 0))
'''

'''
Q2: Evaluation
(Note: Some past exams have had a question in exactly this format.) 
Which of the following are evaluated when scheme_eval is called on 
(if (< x 0) (- x) (if (= x -2) 100 y)) in an environment in which x is bound to -2? 
(Assume <, -, and = have their default values.)
Called:
<
x
-
Uncalled:
if
=
y
0
-2
100
(
)
'''

def print_evals(expr):
        """Print the expressions that are evaluated while evaluating expr.

        expr: a Scheme expression containing only (, ), +, *, and numbers.

        >>> nested_expr = Link('+', Link(Link('*', Link(3, Link(4, nil))), Link(5, nil)))
        >>> print_evals(nested_expr)
        (+ (* 3 4) 5)
        +
        (* 3 4)
        *
        3
        4
        5
        >>> print_evals(Link('*', Link(6, Link(7, Link(nested_expr, Link(8, nil))))))
        (* 6 7 (+ (* 3 4) 5) 8)
        *
        6
        7
        (+ (* 3 4) 5)
        +
        (* 3 4)
        *
        3
        4
        5
        8
        """
        if not isinstance(expr, Link):
            print(expr)
        else:
            print(expr)
            current = expr.first
            while current != nil:
                print_evals(current.first)
                current = current.rest

