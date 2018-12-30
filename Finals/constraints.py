text1 = "HERWHRITENAMESPOTTHINGAMAJIGNINECONTROLITIDIGYEARHITTHEIRUNTUTMIAREOILCIRCUTAREEATSNOTUPHERMINTONEWONTARILEABOTOKMTAREATDOOIRAMAITGRAVEL"

text2 = "ALICEHADGIVENITTOHERCHILDFORHEHADBROUGHTASTHECOURAGEHEGAVEHERHEREINTHEPRIZESBUTWHOTHEREINTHEDOORITWASHIGHADDEDTHATDOROTHYDIDNOTHURTYOUOH"


constraints = [
   None, None, None, None, None, None, None, None, None, None,
   None, None, None, None, None, None, None, None, (4,), None,
   None, None, None, None, None, None, None, None, None, None,
   None, None, None, None, (20,), None, None, None, None, (19,),
   None, None, (14,), (26,), (21,), (33,), (12,), (22,), None, (0,),
   None, None, (18,4), (52,18,4), None, (6,), (5,), None, (30,), (7,),
   None, (53,52,18,4), (23,), (39,19), (63,39,19), (2,), (31,), (15,), None, None,
   (38,), (64,63,39,19), (48,), None, None, (16,), (10,), None, None, (8,),
   (71,64,63,39,19), None, None, (9,), None, (61,53,52,18,4), (57,), (65,2), (55,6), (78,),
   (56,5), (62,23), None, (58,30), (75,16), None, (83,9), (89,78), (3,), (67,15),
   (25,), (44,21), (47,22), (77,), (80,71,64,63,39,19), (66,31), None, (24,), None, (99,67,15),
   (40,), (37,), None, (42,14), (59,7), (28,), (72,48), (46,12), (76,10), (101,44,21),
   (113,42,14), (109,99,67,15), (50,), (32,), (74,), (102,47,22), (91,62,23), (104,80,71,64,63,39,19), (68,), (17,),
   (27,), (116,72,48), (127,104,80,71,64,63,39,19), None, (117,46,12,), (69,),
   ]


def numConstraintsMet(txt):
   total = 0
   meet = 0
   for pos, ch in enumerate(txt):
      if constraints[pos] == None: continue #no constraints at this position 
      total += 1

      #since we allow reverse homophones, 
      #constraint is met if any(OR) of the position has the same character,
      #other than all(AND) have to be met
      anyOneMeet = False
      for _posIdx in constraints[pos]:
         if ch == txt[_posIdx]: anyOneMeet = True
      if anyOneMeet: meet += 1 

   return meet, total


if __name__ == '__main__':
   for txt in [text1, text2]:
      meet, total = numConstraintsMet(txt)
      print("for text = %s:" % txt)
      print("%d out of %d constraints are met!" % (meet, total))
