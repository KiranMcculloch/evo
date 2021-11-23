class edge:

    edge_id #a uniquely determined ID that stores the node_from, the node_to and the weight of the edge.
    #will contain the node_number of the node from (2 hex char), then the node_number of the node_to (2 hex chars), then a half precison fpn (4 hex chars) for the weight
    #So each edge is a 8-char hexadecimal number.
    #Ex: edge_id = 0x15A9C405

    network #the network object it belongs to
    weight #the weight of the edge (Float Value)
    node node_from #the node the edge originates from
    node node_to #the node the edge is inputing to

        def set_weight(w):
            weight = w

        def get_weight():
            return weight

        #Should never be called, might actually break everything
        def set_node_from(i):
            #no lol

        def get_node_from():
            return node_from
