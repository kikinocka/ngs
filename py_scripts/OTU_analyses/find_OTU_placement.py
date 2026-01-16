#!/usr/bin/env python3
import os
import json

os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/trees/amoebozoa/placement/')

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
JPLACE_FILE = "RAxML_portableTree.EPARUN_amoebozoa.accumulated.jplace"

# ==================================================
# LOAD JPLACE
# ==================================================
with open(JPLACE_FILE) as f:
    data = json.load(f)

tree_str = data["tree"]

# ==================================================
# OTU -> EDGE (best placement)
# ==================================================
otu_to_edge = {}
for placement in data["placements"]:
    edge = placement["p"][0][0]
    for otu in placement["n"]:
        otu_to_edge[otu] = edge

# ==================================================
# PURE-PYTHON NEWICK PARSER (RAxML-CORRECT)
# ==================================================
def extract_edge_to_terminal_sets(newick):
    """
    Correctly maps RAxML edge numbers to the subtree they subtend.
    Handles internal edges AND tip edges.
    """

    stack = [[]]          # root container
    token = ""
    edge_to_terminals = {}
    last_subtree = None   # last closed internal subtree
    last_leaf = None      # last seen leaf name

    def flatten(x):
        for y in x:
            if isinstance(y, list):
                yield from flatten(y)
            else:
                yield y

    i = 0
    while i < len(newick):
        c = newick[i]

        if c == "(":
            stack.append([])
            i += 1

        elif c == ",":
            # if token:
            #     stack[-1].append(token)
            #     last_leaf = token
            #     token = ""
            i += 1

        elif c == ")":
            if token:
                stack[-1].append(token)
                last_leaf = token
                token = ""
            subtree = stack.pop()
            stack[-1].append(subtree)
            last_subtree = subtree
            i += 1

        elif c == "{":   # RAxML edge number
            if token:
                stack[-1].append(token)
                last_leaf = token
                token = ""
            
            j = newick.index("}", i)
            edge = int(newick[i + 1 : j])

            if last_subtree is not None:
                leaves = sorted(set(flatten(last_subtree)))
                edge_to_terminals[edge] = leaves
                last_subtree = None

            elif last_leaf is not None:
                # TIP EDGE
                edge_to_terminals[edge] = [last_leaf]

            else:
                # root edge (rare, safe fallback)
                leaves = sorted(set(flatten(stack[0])))
                edge_to_terminals[edge] = leaves

            i = j + 1

        elif c == ":":
            # skip branch length
            i += 1
            while i < len(newick) and newick[i] not in ",){}":
                i += 1

        elif c in "; \n\t":
            i += 1

        else:
            token += c
            i += 1

    return edge_to_terminals

# ==================================================
# EDGE -> TERMINAL SETS
# ==================================================
edge_to_terminals = extract_edge_to_terminal_sets(tree_str)

# ==================================================
# OUTPUT
# ==================================================
print("OTU\tEdge\tTerminal_Set")

for otu, edge in otu_to_edge.items():
    terminals = edge_to_terminals.get(edge)
    if terminals is None:
        raise RuntimeError(f"Missing terminal set for edge {edge}")
    print(f"{otu}\t{edge}\t{';'.join(terminals)}")

# ==================================================
# SANITY CHECKS
# ==================================================
print("\n# Sanity checks")
print("OTUs:", len(otu_to_edge))
print("Edges with terminal sets:", len(edge_to_terminals))
print("Edges used by OTUs:", len(set(otu_to_edge.values())))
