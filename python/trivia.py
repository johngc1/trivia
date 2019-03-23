#!/usr/bin/env python


def is_odd(roll):
    return roll % 2 != 0

class Game:
    def __init__(self):
        self.players = []
        self.places = [0] * 6
        self.coinTally = [0] * 6
        self.in_penalty_box = [0] * 6
        
        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []
        
        self.current_player = 0
        self.is_getting_out_of_penalty_box = False
        
        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append(self.create_rock_question(i))
    
    def create_rock_question(self, index):
        return "Rock Question %s" % index
    
    def add(self, player_name):
        self.players.append(player_name)
        self.places[self.how_many_players] = 0
        self.coinTally[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False
        
        print player_name + " was added"
        print "They are player number %s" % len(self.players)
        
        return True
    
    @property
    def how_many_players(self):
        return len(self.players)
    
    def roll(self, roll):
        print "%s is the current player" % self.players[self.current_player]
        print "They have rolled a %s" % roll
        
        if self.in_penalty_box[self.current_player]:
            if not is_odd(roll):
                print "%s is not getting out of the penalty box" % self.players[self.current_player]
                self.is_getting_out_of_penalty_box = False
                return

            self.is_getting_out_of_penalty_box = True
                
            print "%s is getting out of the penalty box" % self.players[self.current_player]

        self.move_player(roll)
        self._ask_question()
        
        
    def move_player(self, roll):
        self.places[self.current_player] = self.places[self.current_player] + roll
        if self.places[self.current_player] > 11:
            self.places[self.current_player] = self.places[self.current_player] - 12
        
        print self.players[self.current_player] + \
                    '\'s new location is ' + \
                    str(self.places[self.current_player])
        print "The category is %s" % self._current_category
        
    def _ask_question(self):
        if self._current_category == 'Pop': print self.pop_questions.pop(0)
        if self._current_category == 'Science': print self.science_questions.pop(0)
        if self._current_category == 'Sports': print self.sports_questions.pop(0)
        if self._current_category == 'Rock': print self.rock_questions.pop(0)
    
    @property
    def _current_category(self):
        if self.places[self.current_player] == 0: return 'Pop'
        if self.places[self.current_player] == 4: return 'Pop'
        if self.places[self.current_player] == 8: return 'Pop'
        if self.places[self.current_player] == 1: return 'Science'
        if self.places[self.current_player] == 5: return 'Science'
        if self.places[self.current_player] == 9: return 'Science'
        if self.places[self.current_player] == 2: return 'Sports'
        if self.places[self.current_player] == 6: return 'Sports'
        if self.places[self.current_player] == 10: return 'Sports'
        return 'Rock'

    def increment_coins(self):
        self.coinTally[self.current_player] += 1
        print self.players[self.current_player] + \
            ' now has ' + \
            str(self.coinTally[self.current_player]) + \
            ' Gold Coins.'
        
    def finish_turn(self):
        self.increment_coins()
        keep_playing = not (self.coinTally[self.current_player] == 6)

        self.move_to_next_player()
        
        return keep_playing

    def was_correctly_answered(self):
        if not self.in_penalty_box[self.current_player]:
            print "Answer was corrent!!!!"
            return self.finish_turn()
        
        if self.is_getting_out_of_penalty_box:
            print 'Answer was correct!!!!'
            return self.finish_turn()

        self.move_to_next_player()
        return True

    def move_to_next_player(self):
        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0

    def wrong_answer(self):
        print 'Question was incorrectly answered'
        print self.players[self.current_player] + " was sent to the penalty box"
        self.in_penalty_box[self.current_player] = True
        
        self.move_to_next_player()
        return True
    
    def play(self):
        not_a_winner = False
        self.roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = self.wrong_answer()
        else:
            not_a_winner = self.was_correctly_answered()

        return not_a_winner


from random import randrange

if __name__ == '__main__':
    not_a_winner = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        not_a_winner = game.play()
        
        if not not_a_winner: break
