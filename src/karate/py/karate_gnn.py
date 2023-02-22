import numpy as np
import networkx as nx


def draw_plain(g):
    # Visualize the graph with matplotlib
    import matplotlib.pyplot as plt
    nx.draw(g, with_labels=True)
    plt.show()



def draw_kkl(nx_G, label_map, node_color, pos=None, **kwargs):
    """
    Draw a graph using networkx and matplotlib.
    Parameters
    ----------
    nx_G : graph
       A networkx graph
    label_map : dict
       A dictionary that maps node ids to labels
    node_color : list
       A list of node colors
    pos : dict
       A dictionary that maps node ids to positions
    """
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(10,10))
    if pos is None:
        pos = nx.spring_layout(nx_G, k=5/np.sqrt(nx_G.number_of_nodes()))
        #pos = nx.spring_layout(nx_G)

    nx.draw(
        nx_G,
        pos,
        with_labels=label_map is not None,
        labels=label_map,
        node_color=node_color,
        ax=ax,
        **kwargs
    )
    plt.show()
    #nx.draw(nx_G, pos, node_color=node_color, **kwargs)
    #labels = {n: label_map[n] for n in nx_G.nodes()}
    #nx.draw_networkx_labels(nx_G, pos, labels, font_size=16)
    #plt.show()


def AHat(A):

    print(A)
    A_mod = A + np.eye(A.shape[0])
    D_mod = np.zeros_like(A_mod)

    #for i in range(A_mod.shape[0]):
    #    D_mod[i, i] = np.sum(A_mod[i, :])
    np.fill_diagonal(D_mod, np.asarray(A_mod.sum(axis=1))).flatten()

    #D_mod_invroot = np.zeros_like(D_mod)
    #for i in range(D_mod.shape[0]):
    #    D_mod_invroot[i, i] = 1 / np.sqrt(D_mod[i, i])
    D_mod_invroot = np.linalg.inv(np.sqrt(D_mod))

    A_hat = D_mod_invroot @ A_mod @ D_mod_invroot

    return A_hat





# Dataset: Zachary's Karate Club
g = nx.karate_club_graph()
print("Number of nodes: ", g.number_of_nodes())
print("Number of edges: ", g.number_of_edges())


communities = nx.algorithms.community.greedy_modularity_communities(g)
print("Number of communities: ", len(communities))

colors = np.zeros(g.number_of_nodes())
for i, community in enumerate(communities):
    colors[list(community)] = i

n_classes = np.unique(colors).shape[0]
print("Number of classes: ", n_classes)

labels = np.eye(n_classes)[colors.astype(int)]
club_labels = nx.get_node_attributes(g, 'club')

#_ = draw_kkl(g, None, colors, cmap='gist_rainbow', edge_color='gray')

A = nx.convert_matrix.to_numpy_array(g)
A[A > 0] = 1
A_hat = AHat(A)


# Feature vector
X = np.eye(A.shape[0])