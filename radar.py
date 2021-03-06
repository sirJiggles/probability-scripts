
# sample script to test probability that
# A there is a plane in the sky, 0.5 % chance this is true, given
# this fact we also have a radar (B) it works thusly
#  if there is a plane in the sky it will pick it up with probabilty 99%
#  if not there is still a 10% chance it will regester something. maybe noise

# A and a compliment (is there a plane)
A = 0.05
Ac = 0.95

# B and b complment (can we see it on the radar)
BgivenA = 0.99
BcGivenA = 0.01
BgivenAc = 0.10
BcGivenAc = 0.90

print "Plane in the sky examples with radar"
print "A is in sky B is picked up on radar"

print "#################################"

# how to calculate there is a plane and we got it on radar
# P(A intersection B) = P(A)*P(B|A)
# This is known as the multiplication rule
print "probabilty of A and B"
numerator = A * BgivenA
print numerator
# this is known as the multiplation rule
# conditional probabilty is the probabilty of thing a * b, if we have
# more than one condition we could use something like
# P((A and B) and C) = P(A and B)*P(C|A and B), then to break
# down the A and B it would be P(A and B) = P(A)*P(B|A)*P(C|A and B)


# how to calculate probabilty of B, it can occur for both when a
# plane is and is not in te sky, so first we get the prob for when
# A and B are true (as previous) then get the probabilty for Ac and B
# P(B) =  P(A)*P(B|A) + P(Ac)*P(B|Ac)
# DENOMINATOR
print "probabilty of B"
denominator = (A * BgivenA) + (Ac * BgivenAc)
print denominator
# this is known as total probability theorem, this is the total
# probabilty of the event. It can happen in multiple places.
# to calculate it you add together all Probabilities together.
# we can get each events probability by using the multiplation rule

# now for something cool, given radar found something. how likely is
# it that it was a plane
# P(A|B) = P(A and B) / P(B)
probabiltyOfPlane = numerator / denominator
print "Probability of plane on radar"
print probabiltyOfPlane
# Inference poblem given event, how likely was it to be a plane.
# Byes rule!!
