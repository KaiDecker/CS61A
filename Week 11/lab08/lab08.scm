(define (over-or-under num1 num2) 
  (cond
    ((< num1 num2) -1)
    ((= num1 num2) 0)
    (else 1))
)

(define (make-adder num)
  (lambda (x) (+ num x))
)

(define (composed f g)
  (lambda (x) (f (g x)))
)

(define (repeat f n)
  (if (< n 1)
      (lambda (x) x) ; 如果 n 小于 1，返回恒等函数
      (composed f (repeat f (- n 1)))) ; 递归调用 repeat
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b)
  (cond ((zero? b) a)
        ((zero? a) b)
        ((= (modulo (max a b) (min a b)) 0) (min a b))
        (else (gcd (min a b) (modulo (max a b) (min a b)))))
)
