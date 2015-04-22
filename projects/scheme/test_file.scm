; ADDITIONAL TESTS FOR PRIMITIVE EXPRESSIONS
; Problem 3
(/ 10 (+ 1 1))
; expect 5 


(+ 1 (* 3 4))
; expect 13

(/ 5 2)
; expect 2.5

(+ 1)
; expect 1

(* 3)
; expect 3

(+ (* 3 3) (* 4 4))
; expect 25

(define a (define b 3))
; expect a
a
;expect b
b
;expect 3

(odd? 31)
; expect True

(even? 32)
; expect True

(odd? 32)
; expect False

+
; expect #[+]

odd?
; expect #[odd?]

display
; expect #[display]


;Q4
(+ 2 3)
; expect 5


(+)
;expect 0

(* (+ 3 2) (+ 1 7))
;expect 40

(odd? 13)
;expect True

(car (list 1 2 3 4 5))
;expect 1


(1 2)
;expect Error: cannot call: 1

;Q5
(eval (eval (eval (define tau 6.29))))
;expect 6.29

(define bunny (* 11 11))
;expect bunny

(define bunny_friend (* 10 bunny))
;expect bunny_friend

bunny_friend
;expect 1210

;Testing do_quote_form Q6
(eval (cons 'cdr '('(1 2))))
;expect (2)

'''2
;expect (quote (quote 2))

''(+ (- 4 2) 5)
;expect (quote (+ (- 4 2) 5))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Move the following (exit) line to run additional tests. ;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;;; 1.1.2

(define size 2)
; expect size
size
; expect 2

(* 5 size)
; expect 10

(define pi 3.14159)
(define radius 10)
(* pi (* radius radius))
; expect 314.159

(define circumference (* 2 pi radius))
circumference
; expect 62.8318

;ADDITIONAL TESTS

(define a 3)
; expect a
a
; expect 3

(define a 1)
; expect a
a
; expect 1

(define b a)
; expect b
b
; expect 1

(eval (define largest_number 1000000000))
; expect 1000000000


(define x '20)
;expect x

x
;expect 20

(define x '(20))
; expect x

x
;expect (20)


;Once you finish question6B your evluator should be able to support
;Evaluate atoms, which include numbers, booleans, nil, and symbols
;Evaluate the quote special form
;Evaluate lists,
;Define symbols and
;Call primitive procedures like (+ (-4 2) 5)

;Tests for quotes

'hello
;expect hello

'(1 2 3)
;expect (1 2 3)

'"hi"
;expect "hi"

'(+ 3 4)
;expect (+ 3 4)

'(define x 25)
;expect (define x 25)

(eval 'car)
;expect #[car]
;;; 1.1.4


;TESTING EVAL_ALL Q7
(begin 30 '(+ 2 2))
;expect (+ 2 2)

(begin 42 (define x (+ x 1)))
;x

(begin (+ 2 3) (+ 5 6))
;expect 11

(begin (print 3) '(+ 2 3))
;expect (+ 2 3)

(begin (display "4 plus 1 equals ") (display (+ 4 1)))
;expect 4 plus 1 equals 5okay

(begin (define x 10) x)
;expect 10

(begin (begin (define x 5) x) (begin (define x 7)))
;expect x

;TESTING LAMBDA PROCEDURES Q8

(lambda (x) (+ x x))
;expect (lambda (x) (+ x x))

(lambda () 100)
;expect (lambda () 100)

(lambda (a b) (+ (* 2 a) b))
;expect (lambda (a b) (+ (* 2 a) b))

(define f (lambda (x) (* x 2)))
;expect f

(lambda (x y) (+ x y))
;expect (lambda (x y) (+ x y))

((lambda (x) x) 10)
;expect 10

((lambda (x) (* x x)) 3)
;expect 9

((lambda (x y) (+ x y)) 3 4)
;expect 7

((lambda (x1 x2)
         (* (- x1 x2) (- x1 x2)))
 2 -5) 
;expect 49

(define f
  (lambda (x)
    (g x)))
;expect f


;TESTING SHORTHAND PROCEDURES Q9
(define (f x) (* x 2))
;expect f

(define (square x) (* x x))
; expect square
(square 21)
; expect 441

(define square (lambda (x) (* x x))) ; See Section 1.3.2
(square 21)
; expect 441

(square (+ 2 5))
; expect 49

(square (square 3))
; expect 81

(define (sum-of-squares x y)
  (+ (square x) (square y)))
(sum-of-squares 3 4)
; expect 25

(define (f a)
  (sum-of-squares (+ a 1) (* a 2)))
(f 5)
; expect 136

(define reverse-subtract
  (lambda (x y) (- y x)))
(reverse-subtract 7 10)
;expect 3

(define add4
  (let ((x 4))
    (lambda (y) (+ x y))))
(add4 6)  
;expect 10

(define (factorial n)
 (if (zero? n) 1
 (* n (factorial (- n 1)))))
;expect factorial

(factorial 0)
;expect 1


(factorial 4)
;expect 24

(factorial 10)
;expect 3628800

(define (sum ls)
 (if (null? ls) 0
 (+ (car ls) (sum (cdr ls)))))
;expect sum

(sum '(10 11 12 13))
;expect 46

;Q13 If Form Tests
(if (= 4 2) 'a 'b)
;expect b

(if (= 4 4) (* 1 2) (+ 3 4))
;expect 2

(if (= 4 2) 'a)
;expect okay

(if (= 4 5) (error "doesn't get here") 2)
;expect 2

(define p 80)

(if (> p 70) 'safe 'unsafe)
;expect safe

 (define (digit-num n)
    (if (<= n 9)
      1
      (if (<= n 99)
        2
        (if (<= n 999)
          3
          (if (<= n 9999)
            4
            "a lot")))))
;expect digit-num

(digit-num 1000)
;expect 4

(digit-num 10)
;expect 2


;;; 1.1.6

;Q13 Testing Do_if_form and if expressions







;Q14 And and OR
(and)
;expect True

(and (= 2 2) (< 2 1))
;expect False

(and 1 2 'c '(f g))
;expect (f g)

(and 1)
;expect 1

(and #f (error "doesn't get here"))
;expect False 

(and #t 5)
;expect 5

(and #t #t 100)
;expect 100

(and '(1/0))
;expect (1/0) 


(or (= 2 2) (> 2 1))
;expect True

(or (= 2 2) (< 2 1))
;expect True

(or #f #f #f)
;expect False 

;Testing Cond form Q15

(define (abs x)
  (cond ((> x 0) x)
        ((= x 0) 0)
        ((< x 0) (- x))))

(abs -3)
; expect 3

(abs 0)
; expect 0

(abs 3)
; expect 3

(cond ((> 3 2) 'bigger)
                ((< 3 2) 'smaller)) 
;expect bigger 

(cond ((> 3 3) 'bigger)
                ((< 3 3) 'smaller)
                (else 'equal))
;expect equal

(cond)
;expect okay

(cond (1))
;expect 1

(cond (False) (True))
;expect True

(cond (False 2) (True 32))
;expect 32

;Testing Q16 Make let form
(let ((x 12) (y (* 4 3))) (list x y))
;expect (12 12)

(let ((x (define y 3)) (y 12)) (list x y))
;expect (y 12)

(let ((x (define a 3)) (y (define b 3))) (cons x y))
;expect (a . b)

(let ((n 10)) (if (= n 0) False True))
;expect True


;Q17 DO_MU_FORM
(define a (mu (x) (* x y)))
;expect a

(define g (mu (x y) (a (+ x z))))
;expect g

(define another_func (mu (z) (g 13 13)))
;expect another_func

(another_func 2)
;expect 195 

