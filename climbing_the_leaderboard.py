# https://www.hackerrank.com/challenges/climbing-the-leaderboard/

# esse reprovou em 4 testes por causa do tempo limite excedido, vou tentar otimizar
def climbingLeaderboard(ranked, player):
    ranked = set(ranked) # set não pertmite itens duplicados
    player_ranks = []
    rank = 1
    
    for x in player:
        for y in ranked:
            if x < y:
                rank += 1
        player_ranks.append(rank)
        rank = 1
    return player_ranks