class neuralnet:

    num_nodes #the total number of nodes used for the network

    network_id #hexadecimal string that encapsulates all the info of the network (depends on num_nodes)
    #idea behind this is we want to be able to 'mutate' this string to create a similar neural network, but without changing the number of nodes.

    #How does this work? we need the first few bits to encapsulate the number of nodes, so the computer knows how many digits to read. We will cap our neural networks at
    #a maximum of 128 nodes, which requires 8 bits, or 2 Hexadecimal characters. (this will probably be increased later)
    #Once it knows how many nodes, and it knows that each node has a 6-character hexadecimal code, it can read in all the nodes and add them to the node list,
    #and add them to the proper identifier list.
    #It will then read the rest of the id as edges, and add all the edges to the list.
    #minimum length: 1 node 0 edges = 8 hexa chars e.g: 0x00C901B4
    #maximum length: 128 nodes, 128*127/2 edges = 2+(6*128)+8*(128*127/2) = 65794 hexa chars. This is very large, but in general there will not be maximum edges.

    nodes #list of nodes in the network
    input_nodes #list of input nodes
    internal_nodes #list of internal nodes
    output_nodes #list of output nodes

    edges #list of edges for the network

    #Calculates the next step in the neural netwrok.
    #the calculation is performed as followed:
    #1. Update the values for the nodes marked as 'senses' based on the what is happening in the 'world'
    #2. for each node, calulate the sum of the value of each node running into it, multiplied by the weight of each edge that connects them.
    #The nodes will update in their order in the list their type ID, with internal nodes updated first.
    def update_network():
        for n:nodes:
            n.update()
