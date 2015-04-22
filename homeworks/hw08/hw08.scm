; 1. If the second element is null and the first element is a symbol.
          ;if it (car s) is equal to old then return (cons new nil)
          ;else return (cons (car s) nil)
  ; else this means it is a inner list of one element like ((1)) or other lists (1 2) or ((1) 2)
      ;if (cdr s) is null like ((1)) then return (cons (subsitute (car s) old new))
      ;else its a regular list like (1 2) or (1 . 2)
        ;if the first element is a symbol then




 ;check the first element
;  (if (null? (cdr s)) ;this is for if s is like ('a')
 ;   (if (equal? (car s) old) ;this doesnt work for elements like ( (a))
  ;    (cons new nil)
   ;   (cons (car s) nil))
    ;(if (symbol? (car s)) ;now if the start of this is a list then do checks assuming its a string
     ; (if (equal? (car s) old)
      ;  (cons new (substitute (cdr s) old new))  ;this switches because first of s == old 
       ; (cons (car s) (substitute (cdr s) old new)))
      ;(cons (substitute (car s) old new) (substitute (cdr s) old new)))) ;this means the first element is now a pair and a list

(define (substitute s old new)
  (if (and (null? (cdr s)) (not (list? (car s)))) 
    (if (equal? (car s) old)
      (cons new nil)
      (cons (car s) nil))
    (if (null? (cdr s))
      (cons (substitute (car s) old new) nil)
      (if (not (list? (car s)))
        (if (equal? (car s) old)
          (cons new (substitute (cdr s) old new))
          (cons (car s) (substitute (cdr s) old new)))
        (cons (substitute (car s) old new ) (substitute (cdr s) old new)))))
    
    
    
)

;you might need a higher order function for this one but the basis for this is that.
; the basis for this is that if (car old)

;so first you define x to be s in the outer function
;define a 

(define (sub-all s olds news)
  (if (null? olds)
    s ;return s
    (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news)))
)


(define (cadr s) (car (cdr s)))
(define (caddr s) (car (cdr (cdr s))))
; Derive returns the derivative of exp with respect to var.
(define (derive expr var)
  (cond ((number? expr) 0)
        ((variable? expr) (if (same-variable? expr var) 1 0))
        ((sum? expr) (derive-sum expr var))
        ((product? expr) (derive-product expr var))
        ((exp? expr) (derive-exp expr var))
        (else 'Error)))

; Variables are represented as symbols
(define (variable? x) (symbol? x))
(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))

; Numbers are compared with =
(define (=number? expr num)
  (and (number? expr) (= expr num)))

; Sums are represented as lists that start with +.
(define (make-sum a1 a2)
  (cond ((=number? a1 0) a2)
        ((=number? a2 0) a1)
        ((and (number? a1) (number? a2)) (+ a1 a2))
        (else (list '+ a1 a2))))
(define (sum? x)
  (and (list? x) (eq? (car x) '+)))
(define (addend s) (cadr s))
(define (augend s) (caddr s))

; Products are represented as lists that start with *.
(define (make-product m1 m2)
(cond ((or (=number? m1 0) (=number? m2 0)) 0)
      ((=number? m1 1) m2)
      ((=number? m2 1) m1)
      ((and (number? m1) (number? m2)) (* m1 m2))
      (else (list '* m1 m2))))
(define (product? x)
  (and (list? x) (eq? (car x) '*)))
(define (multiplier p) (cadr p))
(define (multiplicand p) (caddr p))

(define (derive-sum expr var)
  (make-sum (derive (addend expr) var) (derive (augend expr) var))
  )

;d/dx (x * y) = dx/dx y + dy/dx +
;have to use multiplier and multiplicand
(define (derive-product expr var)
  (make-sum (make-product (derive (multiplier expr) var) (multiplicand expr) ) 
            (make-product (multiplier expr) (derive (multiplicand expr) var))) 
)
; Exponentiations are represented as lists that start with ^.
;if the exponent is 0, this means if it would return 1
;if the exponent is 1, this means it should return x
;if the base is a number this means return (expt base exponent)
;else just return (list '^ base exponent)
(define (make-exp base exponent)
  (cond ((=number? exponent 0) 1)
        ((=number? exponent 1) base)
        ((number? base) (expt base exponent))
        (else (list '^ base exponent)))
  )

(define (base exp)
  (cadr exp)
  )

(define (exponent exp)
  (caddr exp)
  )

(define (exp? exp)
  (and (list? exp) (eq? (car exp) '^))
  )

(define x^2 (make-exp 'x 2))
(define x^3 (make-exp 'x 3))


;x^2 becomes (* 2 x)
;x^3 becomes (* 3 (^ x 2))
(define (derive-exp exp var)
  (make-product (exponent exp) (make-exp (base exp) (- (exponent exp) 1)))
)

