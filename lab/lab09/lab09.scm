;; Scheme ;;

; Q2
(define (cube x)
  (* x x x)
)


; Q3
(define (over-or-under x y)
  (cond 
    ((> x y) 1)
    ((= x y) 0)
    (else -1))
)


; Q4
(define lst (list (cons 1 nil) 2 (cons 3 4) 5)
)
  

; Q5
(define (remove item lst)
  ;This is some recursive thing you 
  ;If the lst is empty use the length operator return ()
  ;If the first item equals item then return a list that skips the element
  (if (= (length lst) 0)
    ()
    (if (= (car lst) item)
      (remove item (cdr lst))
      (cons (car lst) (remove item (cdr lst)))))
)

;;; Tests

(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)


; Q6
(define (filter f lst)
  (if (= (length lst) 0)
  ()
  (if (f (car lst))  ;if it statisfies the condition
    (cons (car lst) (filter f (cdr lst)))
    (filter f (cdr lst))))
)


; Q7
(define (make-adder num)
  ;This procedure returns another procedure that adds based on the number
  (lambda (x) (+ num  x))
)


; Q8
(define (composed f g)
  ;this function returns f(g(x))
  (lambda (x) (f (g x)))
)

