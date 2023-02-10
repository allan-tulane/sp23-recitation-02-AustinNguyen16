"""
CMPS 2200 Recitation 2
"""
import tabulate
import time
import math

def simple_work_calc(n,a,b):
  if n == 1:
    return 1
  result = a * simple_work_calc(int(n/b),a,b) + n
  return result

def test_simple_work():
  assert simple_work_calc(10,2,2) == 36
  assert simple_work_calc(20,3,2) == 230
  assert simple_work_calc(30,4,2) == 650
  assert simple_work_calc(5,2,2) == 13
  assert simple_work_calc(2,2,2) == 4
  assert simple_work_calc(1, 1, 1) == 1

def work_calc(n,a,b,f):
  if n == 1:
    return 1
  result = a * work_calc(int(n/b), a, b, f) + f(n)
  return result

def test_work():
  assert work_calc(10,2,2, lambda n: 1) == 15
  assert work_calc(20,1,2, lambda n: n*n) == 530
  assert work_calc(30,3,2, lambda n: n) == 300
  assert work_calc(40,2,2, lambda n:n) == 224
  assert work_calc(4,2,2, lambda n:n*n) == 28
  assert work_calc(2,2,2, lambda n:n) == 4

print(work_calc(10,2,1,lambda n:1))
print(work_calc(10,2,1,lambda n:math.log(n)))
print(work_calc(10,2,1,lambda n:n))

def compare_work(work_fn1, work_fn2, sizes = [10, 20, 50, 10, 100, 5000, 10000]):
  result = []
  for n in input_sizes:
    result.append((n, work_fn(n), work_fn(n)))
  return result
  
def span_calc(n,a,b,f):
  if n == 1:
        return n
    else:
        return a * span_calc(n//b, a, b, f) + f(n)

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work():
  work_fn1(1)=1
  work_fn2(1)=1
  work_fn1 = (lambda n:2) * work_fn1(n//2) + work_fn1(n)
  work_fn2 = (lambda n:2) * work_fn2(n//2) + work_fn2(n*n)
  res=comapre_work(work_fn1,work_fn2)
  print_work_results(res)

def test_compare_span():
  result=[]
  for n in sizes:
    result.append((n,span_fn1(n),span_fn2(n)))
  return result