
def optimize_transaction(transaction_list):

    transactions = transaction_list['transaction_list']

    graph = {}

    #Adjacentcy list implementation 
    for transaction in transactions:
        if transaction[0] not in graph:
            graph[transaction[0]]=[]
            graph[transaction[0]].append([transaction[1],transaction[2]]) 
        else:
            graph[transaction[0]].append([transaction[1],transaction[2]])

        

    