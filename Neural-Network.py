class NeuralNetwork:
    def __init__(self, input_nodes_qty, hidden_layers_qty, hidden_layers_size, output_nodes):
        # setup global vars
        self.input_nodes_qty = input_nodes_qty          # number of input nodes min 2
        self.hidden_layers_qty = hidden_layers_qty      # number of hidden layers min 0
        self.hidden_layers_size = hidden_layers_size    # number of nodes in each hidden layer min 1 (if hidden_layers_qty == 0 then hidden_layers_size is ignored)
        self.output_nodes_qty = output_nodes_qty        # list of output nodes labeled min 2

        # test input
        if input_nodes_qty < 2:
            raise ValueError("input_nodes_qty must be min 2")
        if hidden_layers_qty < 0:
            raise ValueError("hidden_layers_qty must be min 0")
        if hidden_layers_size < 1:
            raise ValueError("hidden_layers_size must be min 1")
        if len(output_nodes_qty) < 2:
            raise ValueError("output_nodes_qty must be min 2")

        # generate empty untrained neural network
        nn = []
        for hlq in range(self.hidden_layers_qty):
            nn.append([])
            for hls in range(self.hidden_layers_size):
                nn[hlq].append(0.5)

    def get_labeled_data(self, labeled_data, lbl):
        # make sure the data size is correct
        if len(labeled_data) != self.input_nodes_qty:
            raise ValueError("labeled_data size must be a list of exactly: "+str(self.input_nodes_qty)+" nodes")
        
        # 

NeuralNetwork(3,4,4,4)