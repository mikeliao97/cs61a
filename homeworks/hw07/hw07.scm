
;(1 2 3 4)
;cddr gets second second elemen
; after one cdr (2 3 4)
; after two (3 4)
;this might error if the length is better than a certain number
(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (if (<= (length s) 1)
  nil
  (car (cdr s)))
)

(define (caddr s)
  (if (<= (length s) 2)
  nil
  (car (cddr s)))
)


(define (sign x)
  (cond 
    ((< x 0) -1)
    ((= x 0) 0)
    ((> x 0) 1))
)


(define (square x) (* x x))

;raise the number b to the pwoer of integer n 
; 3^4 = (3 * 3) ^ 2
; 3^3 = 3 * 3 ^ 2
; 3 ^ 8 = (3^4) ^ 2
;base case, if n == 0 return 1  because 3^0 = 1
;if its odd , return b * b^ n - 1
; if its even return  (pow(b, n//2)) ^ 2
(define (pow b n)
  (if (= n 0)
    1 ;return 1
    (if (= n 1 )
    b
      (if (odd? n)
        (* b (pow b (- n 1))) ;return b * pow b n -1 
        (square (pow b (quotient n 2)))))) ;if its even return (pow b 
)

; 4 minutes 46 seconds
(define (ordered? s)
  ;if its empty then return true
  ;if its one element also true
  ;if (car (cdr s)) < (car s) then return False
  (if (<= (length s ) 1)
    True
    (if (< (car (cdr s)) (car s)) ;if the second element is smaller thanf irst
      False
      (ordered? (cdr s))))
                
)

;takes a well or not well-formed list and returns a nested list
;with the same content and strcuture but which does not have any
;dots when displayed
;(2 . 1)
;(2 1) the difference between these two
;base case: if the length of s is 1 then return the con of s
;Test the car of s. if its a number then (cons (car s) (nodots (cdr s))
;else return (cons (nodots (car s)) (nodots (car s)))
;if its a number then return the con of it else plus the list else

; if the car of this is a number:
    ;if the cdr of this is a number as well return (cons (car s) (cons s)))
    ;else return return (cons (car s) (nodots (cdr s)))
  ;else
    ;if the cdr of this is a number as well (con (nodots (car s)) (cons s nil))
    ;else return (con (nodots (car s)) (cons (nodots (cdr s)))

(define (nodots s)
  (if (null? (cdr s)) ;if its only one element like a list (1)
    (cons (car s) nil)
    (if (number? (car s))
      (if (number? (cdr s))
        (cons (car s) (cons (cdr s) nil))
        (cons (car s) (nodots (cdr s))))
      (if (number? (cdr s))
        (cons (nodots (car s)) (cons (cdr s) nil))
        (cons (nodots (car s)) (nodots (cdr s))))))
)


; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) false) ;if its empty return false
          ((= v (car s)) true) ;if v == (car s) then return true
          (else (contains? (cdr s) v)) ; replace this line else return shorter list
          ))


; Equivalent Python code, for your reference:
;
; def empty(s):
;     return len(s) == 0
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

;if its empty you return the list v
;if its v < than the current value than you do con( rest of list)
;if its equal then return the list s
(define (add s v)
    (cond ((empty? s) (list v))
          ((= v (car s)) (car s ) (add (cdr s) v))
          ((< v (car s)) (cons v s))
          (else (cons (car s) (add (cdr s) v))) ; replace this line
          ))




(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          ((= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
          ((< (car s) (car t)) (intersect (cdr s) t))
          (else (intersect s (cdr t)) ; replace this line
          )))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

;if it equals then return it decrement both
;if s > t decrement s and recturn
;else decrement t
(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          ((= (car s) (car t)) (cons (car s) (union (cdr s) (cdr t))))
          ((> (car s) (car t)) (cons (car t) (union s (cdr t))))
          (else (cons (car s) (union (cdr s) t))) ; replace this line
          ))


