def minimax(nodes, depth, alpha, beta, maximizing_player, index=0):
    # Terminal node or maximum depth reached
    if depth == 0 or 2 * index >= len(nodes):
        return nodes[index]

    if maximizing_player:  # Maximizer's turn
        best_value = float('-inf')
        # Explore left child
        best_value = max(best_value, minimax(nodes, depth - 1, alpha, beta, False, 2 * index))
        alpha = max(alpha, best_value)
        if beta <= alpha:  # Prune right child
            return best_value
        # Explore right child
        best_value = max(best_value, minimax(nodes, depth - 1, alpha, beta, False, 2 * index + 1))
        alpha = max(alpha, best_value)
        return best_value

    else:  # Minimizer's turn
        best_value = float('inf')
        # Explore left child
        best_value = min(best_value, minimax(nodes, depth - 1, alpha, beta, True, 2 * index))
        beta = min(beta, best_value)
        if beta <= alpha:  # Prune right child
            return best_value
        # Explore right child
        best_value = min(best_value, minimax(nodes, depth - 1, alpha, beta, True, 2 * index + 1))
        beta = min(beta, best_value)
        return best_value

def main():
    player = int(input("Player 1 (Maximizer) or 2 (Minimizer)? "))
    depth = int(input("Enter depth of the tree: "))
    # Number of terminal nodes must be 2^depth
    nodes = [0 for _ in range(2 ** depth)]
    for i in range(len(nodes)):
        nodes[i] = int(input(f"Enter value of terminal node {i + 1}: "))

    # If player 1 is selected, they are the maximizer
    is_maximizer = player == 1
    best = minimax(nodes, depth, float('-inf'), float('inf'), is_maximizer)
    print(f"\nBest outcome for Player {player}: {best}")

main()
