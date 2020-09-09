
def optimize_transaction(transaction_list):

    transactions = transaction_list['transaction_list']

    graph_edges = {}
    graph_weights = {}

    for trans in transactions:
        
        edge = '{0}-{1}'.format(trans[0],trans[1])
        reverse_edge = '{0}-{1}'.format(trans[1],trans[0])
        
        if trans[0] not in graph_edges:
            graph_edges[trans[0]] = set()            
            graph_edges[trans[0]].add(trans[1])
            
        else:
            graph_edges[trans[0]].add(trans[1])
            
        if edge in graph_weights.keys():
                graph_weights[edge] += trans[2]
        else:
            graph_weights[edge] = trans[2]
        
        if reverse_edge in graph_weights.keys():
            if graph_weights[reverse_edge] >= graph_weights[edge]:
                if graph_weights[reverse_edge]-graph_weights[edge] == 0:
                    del graph_weights[reverse_edge]
                    del graph_weights[edge]
                    graph_edges[trans[1]].discard(trans[0])
                    graph_edges[trans[0]].discard(trans[1])
                else:
                    graph_weights[reverse_edge] = graph_weights[reverse_edge] - graph_weights[edge]
                    del graph_weights[edge]
                    graph_edges[trans[0]].discard(trans[1])
            else:
                graph_weights[edge] = graph_weights[edge] - graph_weights[reverse_edge]
                del graph_weights[reverse_edge]
                graph_edges[trans[1]].discard(trans[0])
    
    return graph_edges
                

    
    