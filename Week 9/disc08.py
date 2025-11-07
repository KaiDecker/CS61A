def strange_loop():
    """Return a Link s for which s.rest.first.rest is s.

    >>> s = strange_loop()
    >>> s.rest.first.rest is s
    True
    """
    s = Link(1, Link(Link(2)))
    s.rest.first.rest = s
    return s

def sum_rec(s, k):
    """Return the sum of the first k elements in s.

    >>> a = Link(1, Link(6, Link(8)))
    >>> sum_rec(a, 2)
    7
    >>> sum_rec(a, 5)
    15
    >>> sum_rec(Link.empty, 1)
    0
    """
    # Use a recursive call to sum_rec; don't call sum_iter
    if s == Link.empty or k == 0:
        return 0
    return s.first + sum_rec(s.rest, k - 1)

def sum_iter(s, k):
    """Return the sum of the first k elements in s.

    >>> a = Link(1, Link(6, Link(8)))
    >>> sum_iter(a, 2)
    7
    >>> sum_iter(a, 5)
    15
    >>> sum_iter(Link.empty, 1)
    0
    """
    # Don't call sum_rec or sum_iter
    total = 0
    while s != Link.empty and k > 0:
        total += s.first
        s = s.rest
        k -= 1
    return total

def overlap(s, t):
    """For increasing s and t, count the numbers that appear in both.

    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8)))))
    >>> overlap(a, b)  # 3 and 7
    2
    >>> overlap(a.rest, b)  # just 7
    1
    >>> overlap(Link(0, a), Link(0, b))
    3
    """
    k = 0
    while s != Link.empty and t != Link.empty:
        if s.first < t.first:
            s = s.rest
        elif s.first > t.first:
            t = t.rest
        else:
            k += 1
            s = s.rest
            t = t.rest
    return k

def iterate_in_order(s, t):
    """For increasing s and t, yields the elements in s and t, in non-decreasing order.

    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8)))))
    >>> t = iterate_in_order(a, b)
    >>> for item in t:
    ...     print(item)
    1
    3
    3
    4
    5
    6
    7
    7
    8
    9
    10
    >>> t = iterate_in_order(Link.empty, b)
    >>> for item in t:
    ...      print(item)
    1
    3
    5
    7
    8
    """
    while s != Link.empty and t != Link.empty:
        if s.first < t.first:
            yield s.first
            s = s.rest
        else:
            yield t.first
            t = t.rest
    while s != Link.empty:
        yield s.first
        s = s.rest
    while t != Link.empty:
        yield t.first
        t = t.rest

def display(s, k=10):
    """Print the first k digits of infinite linked list s as a decimal.

    >>> s = Link(0, Link(8, Link(3)))
    >>> s.rest.rest.rest = s.rest.rest
    >>> display(s)
    0.8333333333...
    """
    assert s.first == 0, f'{s.first} is not 0'
    digits = f'{s.first}.'
    s = s.rest
    for _ in range(k):
        assert s.first >= 0 and s.first < 10, f'{s.first} is not a digit'
        digits += str(s.first)
        s = s.rest
    print(digits + '...')

def divide(n, d):
    """Return a linked list with a cycle containing the digits of n/d.

    >>> display(divide(5, 6))
    0.8333333333...
    >>> display(divide(2, 7))
    0.2857142857...
    >>> display(divide(1, 2500))
    0.0004000000...
    >>> display(divide(3, 11))
    0.2727272727...
    >>> display(divide(3, 99))
    0.0303030303...
    >>> display(divide(2, 31), 50)
    0.06451612903225806451612903225806451612903225806451...
    """
    assert n > 0 and n < d
    result = Link(0)  # The zero before the decimal point
    remainder = n * 10 # 使用长除法，需要使余数乘以10
    decimal_place = result.rest # 指向第一个小数位
    seen_remainders = {} # 记录余数及其对应的小数位节点
    while True:
        digit = remainder // d # 计算当前小数位的数字
        remainder = remainder % d # 更新余数
        decimal_place.rest = Link(digit) # 创建新节点存储当前小数位
        decimal_place = decimal_place.rest # 移动到下一个小数位
        if remainder == 0:
            break
        if remainder in seen_remainders: # 出现小数循环
            decimal_place.rest = seen_remainders[remainder]
            break
        seen_remainders[remainder] = decimal_place # 记录当前余数和对应的小数位节点
        remainder *= 10
    return result

class Link:
    """A linked list is either a Link object or Link.empty

    >>> s = Link(3, Link(4, Link(5)))
    >>> s.rest
    Link(4, Link(5))
    >>> s.rest.rest.rest is Link.empty
    True
    >>> s.rest.first * 2
    8
    >>> print(s)
    <3 4 5>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
