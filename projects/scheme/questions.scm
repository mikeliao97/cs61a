(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cddr x) (cdr (cdr x)))
(define (cadar x) (car (cdr (car x))))

; Some utility functions that you may find useful to implement.
(define (map proc items)
  (if (null? items) 
    nil
    (cons (proc (car items)) (map proc (cdr items)))))

;what is the point of cons-all
(define (cons-all first rests)
  (if (null? rests) 
    nil
    (cons (append (list first) (car rests)) (cons-all first (cdr rests)))))

(cons-all 1 '((2 3) (2 4) (3 5)))
(cons-all 10 '(()))

;x = [1, 2, 3] y = [4, 5, 6]    zip(x, y) = [(1, 4), (2, 5), (3, 6)]
;x = [1,2] y = [3, 4] z = [5, 6] zip(x,y,z) = [(1 3 5), (2 4 6)]

  

(define (get-rest-list pairs)
  (if (null? pairs)
    '()
    (cons (cdr (car pairs)) (get-rest-list (cdr pairs)))))

(get-rest-list '((1 2) (3 4) (5 6)) )


(define (get-first-element pairs)
    (if (null? pairs)
      '()
      (cons (car (car pairs )) (get-first-element (cdr pairs)))))

(get-first-element '((1 2) (3 4) (5 6)))

(define (zip pairs)
  (if (null? (car pairs) )
    '() 
    (cons (get-first-element pairs) (zip (get-rest-list pairs)))))

(zip '((1 2) (3 4) (5 6)))
(zip '((1 2 3) (2 4 5)))
  

;; Problem 18
;; Returns a list of two-element lists
;s is a list of values like (3 4 5 6)
;if s is empty then return '()
; ( (0 3) (1 4) (2 5) (3 6)) ----> Pair(Pair(0, Pair(3, nil)), Pair(
(define (enumerate s)
  ; BEGIN Question 18
  (define (inner s count)
    (if (null? s) 
      '()
      (cons (cons count (cons (car s) nil)) (inner (cdr s) (+ 1 count)))))
  (inner s 0)
  )
  ; END Question 18

;; Problem 19
;; List all ways to make change for TOTAL with DENOMS
;How to do this in python
;if total == 0, return 0
;if n < 0 or m == 0
; return nil

(define (list-change total denoms)
  (cond ((= total 0) '(()))
        ((or (< total 0) (null? denoms)) '()) 
        (else 
          (begin (define using_denoms (list-change (- total (car denoms)) denoms))
                 (define with_denoms (cons-all (car denoms) using_denoms ))
            (define without_denoms (list-change total (cdr denoms)))
            (append with_denoms without_denoms))))
  )


(list-change 10 '(10 5 1))
  ; END Question 19

;; Problem 20
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (analyze expr)
  (cond ((atom? expr)
         ; BEGIN Question 20
         expr
         ; END Question 20
         )
        ((quoted? expr)
         ; BEGIN Question 20
         expr
         ; END Question 20
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN Question 20
           (append (list form params) (map analyze body))
           ; END Question 20
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN Question 20
           (begin
           (define parameters (car (zip values)))
           (define arguments (car (cdr (zip values))))
           ; END Question 20
           (append (list (list 'lambda parameters (analyze (car body)))) (map analyze arguments))
           )))
        (else
         ; BEGIN Question 20
         (map analyze expr)
         ; END Question 20
         )))

(analyze '(+ let a b))
;; Problem 21 (optional)
;; Draw the hax image using turtle graphics.
(define (hax d k)
  ; BEGIN Question 21
  'REPLACE-THIS-LINE
  )
  ; END Question 21

