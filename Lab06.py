import datetime
class Player:
     def __init__(self, firstname,lastname,team=None):
          self.first_name = firstname
          self.last_name = lastname
          self.scores = []
          self.team = team

     def add_score(self,date,score):
          self.scores.append( (date,score) )

     def total_score(self):
          score_set = ()
          tot_score = 0
          for score in self.scores:
               score_set = score
               tot_score += score_set[1]
          return tot_score


     def average_score(self):
          score_set = ()
          tot_score = 0
          for score in self.scores:
               score_set = score
               tot_score += score_set[1]
          avg_score = float(tot_score) / len(self.scores)
          return avg_score


torres = Player('Fernando','Torres')
torres.add_score(datetime.date(2012,06,02),0)
torres.add_score(datetime.date(2012,07,02),0)
torres.add_score(datetime.date(2012,07,12),1)
torres.add_score(datetime.date(2012,07,22),0)
torres.add_score(datetime.date(2012,07,10),1)

average_score = torres.average_score();
print "Fernando Torees' average score so far is", average_score

##        PART THREE

class  Team:
     def __init__(self,Name,League,manager,pts,players=[]):
          self.name = Name
          self.league = League
          self.manager_name = manager
          self.points = pts
          self.players = players

     def add_player(self,player):
          self.players.append(player)
          
     def __str__(self):
          string = self.name 
##          n = self.name
##          m = self.manager_name
##          p = self.players
##          string = "The team " + n  +" has " + m + " as its manager and has " + len(p) +" players"
          return string

portugal = Team('Portugal FC','Premier League','Hans Harrohf',5)
spain = Team('Spain FC','La Liga','Gerrad Fuschemo',3,)
## printing default message for spain

print spain
print

## Adding teams to both player's profiles
torres = Player('Fernando', 'Torres',spain)
ronaldo = Player('Christiano','Ronaldo',portugal)

## Adding both players to their respective teams
portugal.add_player(ronaldo)
spain.add_player(torres)


##        8 Match Class

class Match:
     def __init__(self,home_team, away_team, date, home_scores={},away_scores={}):
          self.home_team = home_team
          self.away_team = away_team
          self.date = date
          self.home_scores = home_scores
          self.away_scores = away_scores

     def home_score(self):
          total_hscores = 0
          for score in self.home_scores:
               total_hscores += score
          return total_hscores
          


     def away_score(self):
          total_ascores = 0
          for score in self.away_scores:
               total_ascores += score
          return total_ascores

     def winner(self):
          hts = self.home_scores
          ats = self.away_scores
          if(hts > ats):               
               return self.home_team
          elif(ats > hts):
               return self.away_team

     def add_score(self,player,score):
          team = player.team
          count =0
          if (team == self.home_team):
               for play in self.home_scores:
                    if(play == player):
                         self.home_scores[play] += score
                         count += 1
               if(count ==0):
                    self.home_scores[player] = score
          elif(team == self.away_team):
               for play in self.away_scores:
                    if(play == player):
                         self.away_scores[play] += score
                         count += 1
               if(count ==0):
                    self.away_scores[player] = score



##        CREATING MATCH euro_semi_finals between portugal and spain
euro_semi_final = Match(spain,portugal,datetime.date(2012,06,27))
euro_semi_final.add_score(torres,1)
euro_semi_final.add_score(ronaldo,1)
euro_semi_final.add_score(torres,1)
winner = euro_semi_final.winner()
print "The winner of the match is ", winner
                    
