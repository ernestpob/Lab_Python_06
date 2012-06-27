"""
Lab_Python_06
Part 1
"""

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/21/2012	| 1
"""
import datetime
## create the player_stats data structure

player_stats ={ ('rooney',datetime.date(2012,06,23))  :(datetime.date(2012,06,23),2),
                         ('rooney',datetime.date(2012,06,25))  :(datetime.date(2012,06,25),2),
                         ('ronaldo',datetime.date(2012,06,19)) :(datetime.date(2012,06,19),0),
                         ('ronaldo',datetime.date(2012,06,20)) :(datetime.date(2012,06,20),3),
                          ('torres',datetime.date(2012,06,21))   :(datetime.date(2012,06,21),0),
                           ('torres',datetime.date(2012,06,23))  :(datetime.date(2012,06,21),1)   }

## implement highest_score
def highest_score(player_stats):
     val_tup = tuple()                        # to store the value as a tuple
     key_tup = tuple()                     # to store the key as a tuple
     g_count = 0                             # to store the highest goal
     for player in player_stats:
          key_tup = player
          val_tup = player_stats[player]
          if(val_tup[1] > g_count):
               g_count = val_tup[1]          
               g_scorer = key_tup[0]          # to store the player name
               g_date = str(val_tup[0])      # to store date of goal 
     results =(g_scorer,g_date,g_count)  # to store the results (player name, date of score, score).
     return results


####   TESTING FUNCTION highest_score
##asdf = highest_score(player_stats)
##print asdf
##print


## implement highest_score_for_player
def highest_score_for_player(player_stats,player):
     val_tup = tuple()                        # to store the value as a tuple
     key_tup = tuple()                     # to store the key as a tuple
     g_count = 0                             # to store the highest goal
     count = 0                                    # counter variable
     for p in player_stats:
          key_tup = p
          if(player == key_tup[0]):
               val_tup = player_stats[p]
               if(val_tup[1] > g_count):
                    g_count = val_tup[1]
                    g_date = str(val_tup[0])
                    count += 1
     if(count ==0):
          return
     else:
          results = (player,g_date,g_count)
          return results
     
#### TESTING FUNCTION highest_score_for_player
##adf = highest_score_for_player(player_stats,'torres')
##print adf
##print

## implement highest_scorer
def highest_scorer(player_stats):
     val_tup = tuple()                        # to store the value as a tuple
     key_tup = tuple()                     # to store the key as a tuple
     g_highest = 0                           #highest no. of goals in system
     count = 0                                    # counter variable
     player_list = list()
     for p in player_stats:
          player_list.append(p[0])
     for player in player_list:
          g_count = 0                             # to store the highest goal
          for pl in player_stats:
               if(pl[0] == player):
                    val_tup = player_stats[pl]
                    g_count += val_tup[1]
          if(g_count > g_highest):
               g_highest = g_count
               player_name = player
     results = (player_name, g_highest)

     return results

####   TESTING FUNCTION highest_scorer
##fsd = highest_scorer(player_stats)
##print fsd
##print




     
