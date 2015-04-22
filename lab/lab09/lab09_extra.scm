;; Extra Scheme Questions ;;

; Q9
; if the smaller value is divisible by the bigger value return
; the smaller value
; else return the gcd of the smaller value, and bigger % smaller
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  (cond ((zero? a) b)
        ((zero? b) a)
        (else (if (= 0 (modulo (max a b) (min a b)))
    (min a b)
    (gcd (min a b) (modulo (max a b) (min a b))))))
)


; Q10
(define (num-leaves tree)
  (cond ((null? tree) 0)
        ((and (null? (left tree)) (null? (right tree))) 1)
        (else (+ (num-leaves (left tree)) (num-leaves (right tree)))))
)

; Q11
(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (accumulate )
  )
)


; Binary Tree ADT
(define (make-btree entry left right)
  (cons entry (cons left right)))

(define (entry tree)
  (car tree))

(define (left tree)
  (car (cdr tree)))

(define (right tree)
  (cdr (cdr tree)))

(define test-tree
  (make-btree 2
              (make-btree 1
                          nil
                          nil)
              (make-btree 4
                          (make-btree 3
                                      nil
                                      nil)
                          nil)))

; test-tree:
;     2
;    / \
;   1   4
;      /
;     3
