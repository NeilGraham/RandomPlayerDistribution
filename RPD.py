import random
import math

def input_players():
    players = []
    while True:
        print('- ', end='')
        player = input()
        if player.lower() == 'done':
            break
        elif player.lower() == 'back':
            if len(players) == 0:
                print('There are no players to remove.')
            else:
                print('Player ' + players[-1] + ' has been removed.')
                del players[-1]

        elif player.lower() == 'show':
            print(players)
        elif 'remove ' in player:
            remove_player = player[7:len(player)].strip()
            could_find = False
            for p in range(len(players)):
                if remove_player == players[p]:
                    del players[p]
                    could_find = True
                    print('Player ' + remove_player + ' has been removed.')
                    break
            if could_find == False:
                print('We could not find ' + remove_player + '.')
        elif player in players:
            print('That player name has already been taken.')
            print('Use another character alongside the name to be able to differentiate it.')
        else:
            players.append(player)
    return players

def group_players(players, group_max):
    print()
    print('Distributing ' + str(len(players)) + ' people into ' + str(math.ceil(len(players)/group_max)) + ' groups.')
    print()
    group_sizes = find_group_sizes(players, group_max)
    return randomly_distribute(players, group_sizes)


def find_group_sizes(players, group_max):
    group_sizes = []
    if len(players) % group_max == 0:
        group_sizes = [group_max] * int(len(players) / group_max)
    else:
        min_groups = math.ceil(len(players)/group_max)
        negation = 0
        while True:
            for i in range(min_groups):
                sum = ((i + 1) * (group_max - 1 - negation)) + ((min_groups - (i + 1)) * (group_max - negation))
                if sum == len(players):
                    group_sizes += [group_max - 1 - negation] * (i + 1)
                    group_sizes += [group_max - negation] * (min_groups - (i + 1))
                    break
            if len(group_sizes) > 0:
                break
            negation += 1
    return group_sizes

def randomly_distribute(players, group_sizes):
    all_groups = []
    n_players = players
    for g in range(len(group_sizes)):
        group = []
        iteration = 0
        while iteration != group_sizes[g]:
            print(players)
            rand_player = random.randint(0, len(n_players) - 1)
            group += [n_players.pop(rand_player)]
            iteration += 1
        all_groups += [group]
    return all_groups

def print_groups(groups):
    for g in range(len(groups)):
        print('Group ' + str(g+1) + ':')
        for p in range(len(groups[g])):
            print('  ' + groups[g][p])
        print()



def biquery(c1, c2):
    print(' ({}/{}) '.format(c1, c2), end='')
    cap_c = 0
    if c1 == c1.upper():
        cap_c = 1
    elif c2 == c2.upper():
        cap_c = 2
    i = input().strip().lower()
    while True:
        if i == c1.lower() or i == c2.lower():
            break
        if cap_c > 0:
            if i == '':
                break
        print("    Type in the letter '{}' or '{}'. ({}/{}) ".format(c1.lower(), c2.lower(), c1, c2), end='')
        i = input().strip().lower()
    if cap_c == 1:
        if i == c1.lower() or i == '':
            return c1.lower()
        else:
            return c2
    elif cap_c == 2:
        if i == c2.lower() or i == '':
            return c2.lower()
        else:
            return c1
    else:
        if i == c1:
            return c1
        else:
            return c2


def main():
    print()
    print('Type in the names of each player, then type in \'done\' once you\'re finished.')
    print('Type \'back\' to remove the last name. Type \'show\' to see who\'s already in.')
    print('Type \'remove [playerName]\' to remove a player from the list. (Case sensitive)')
    print()
    players = input_players()
    print(players)
    groups = group_players(players, 4)
    print(players)
    print_groups(groups)
    print('To add or remove more players, type in \'change\'.')
    print('To randomize again, just press enter/return.')

main()
