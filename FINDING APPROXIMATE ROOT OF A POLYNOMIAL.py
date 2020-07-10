#!/usr/bin/env python
# coding: utf-8

# In[3]:


epsilon = 0.01
y = 6 #constant moved to the right of the given polynomial
guess = y/2
num_guesses = 0

while abs((guess**3 + 6*guess) - y) >= epsilon:
    num_guesses += 1
    guess = guess - (((guess**3 + 6*guess) - y)/(3*(guess**2) + 6))
print("num_guesses = ", str(num_guesses))
print("Root of the polynomial p(x) = x**3 + 6x - 6 is ", str(guess))

#MATHEMATICAL CONCEPT
# when we try to find the root r, then its better approximation is given by r - p(r)/p'(r)

