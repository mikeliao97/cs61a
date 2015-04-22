; Load this file into an interactive session with:
; python3 scheme -load quiz03.scm

; Filter (from lab) takes a predicate procedure f and a list s. It returns a
(define (filter f s)
    (cond ((null? s) '())
          ((f (car s)) (cons (car s) (filter f (cdr s))))
          (else (filter f (cdr s))))
)

(define (all f s)
  (cond ((null? s) True)
        ((f (car s)) (all f (cdr s)))
        (else False))
)


;if g((car s) (each element of s)) passes then keep s
(define (every g s)
  ;g takes two elements as an argument 
  ;you need another list to compare s with  
  ;if s is null then return open list
  ;else run (all? s), (all?  takes g). if all return cons((car s), (every g (cdr s))
  (define (inner inner_list)
    (cond ((null? inner_list) '())
          ((all_apply? (car inner_list) g s) (cons (car inner_list) (inner (cdr inner_list))))
          (else (inner (cdr inner_list)))))
  (inner s)
)

(define (all_apply? value f s)
  (cond ((null? s) True)
        ((f value (car s)) (all_apply? value f (cdr s)))
        (else False)))


(define (equal hand highest) ;returns wether there is a card equal to highest in the hand
  (cond ((null? hand) False)
        ((= (car hand) highest) True)
        (else (equal (cdr hand) highest))))

; Return a minimum card.
(define (min hand) (car (every <= hand)))

(define (find_largest_after value hand) 
  (if (equal hand value) 
    value
    (find_largest_after (+ 1 value) hand)))


(define (fimp hand highest)
  ;if highest bigger than all your hand than return (min hand)
  ;else than run a functon that gro
  (cond ((all_apply? highest > hand) (min hand))
        (else (find_largest_after highest hand)))

)












; Legal returns pairs of (card . control) for all legal plays in Cucumber.

(define (legal hand highest)
  (define least (min hand))

  (define (result hand)

    (if (null? hand) nil (begin
        (define card (car hand)) ;have to compare card the card. have like (card, True). if (= card least) or (>= card highest) return True
        (if (or (= card least) (>= card highest)) ;if its bigger than the card or card = list the its valid
          (if (>= card highest) 
            (cons (cons card True) (result (cdr hand)))
            (cons (cons card False) (result (cdr hand))))
          (result (cdr hand))) 
        )))
  (result hand))


