class node:

    node_id #an ID that uniquely determines a node, must contain its value, and its type. The edges will be stored seperately.
    #since we can have 128 node numbers that will take up 8 bits of info.
    #we will use 16 bits to store a half-precision floating point number
    #total = 24 bits = 6 hexadecimal characters to completely identify our nodes. If we decide to go beyond a total of 128 nodes we will need more values.
    #Example: node_id = 0xC901B4

    network #the network object it belongs to
    value #the value that the node stores
    node_number #the order in which the nodes will be updated, also encapsulates the type of node,
    #0-15 (16 possible) represents the input node types, 16-111 (96 possible) represents the internal nodes, 112-127 (16 possible) represents output nodes.
    input_edges #a list of edges that enter this node. Will be calculated once when the network is created, and stored to perform faster network updates.

    def update():
        if 0 <= node_number < NUMBER_OF_SENSES: #if its an input node
            return this.sense()
        else: #if its not an input node
            updated_value=0
            for e:input_edges: #compute weighted sum of input edges
                update_value += (e.get_node_from().get_value())*(e.get_weight())
            return update_value

    def set_value(i):
        value = i

    def get_value():
        return value

    def set_input_edges(e):
        input_edges = e

    def get_input_edges():
        return input_edges

    #should only be called if it is an input node type
    def sense():
        #will check which sense it is, and get the proper value, for now returns 1
        return 1;

#List of senses:
#   1   smell food
#   2
#   3
#   4
#   5
#   6
#   7
#   8
#   9
#   10
#   11
#   12
#   13
#   14
#   15
#   16

#List of outputs:
#   1   move up
#   2   move down
#   3   move right
#   4   move left
#   5
#   6
#   7
#   8
#   9
#   10
#   11
#   12
#   13
#   14
#   15
#   16
