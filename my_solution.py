#!/usr/bin/env python3
"""
Routing Cycle Detector
Finds the longest routing cycle in a pipe-delimited claims routing file.
"""
import sys
from collections import defaultdict


def find_longest_cycle(adj):
      """
          Find the longest simple cycle in a small directed graph.
              adj: dict mapping node -> list of neighbor nodes
                  Returns the length of the longest cycle (number of edges), or 0.
                      """
      best = 0
      nodes = list(adj.keys())

    for start in nodes:
              # DFS stack: (current_node, visited_set, path_length)
              stack = [(start, frozenset([start]), 0)]
              while stack:
                            node, visited, length = stack.pop()
                            for neighbor in adj.get(node, []):
                                              if neighbor == start and length > 0:
                                                                    # Found a cycle back to start
                                                                    cycle_len = length + 1
                                                                    if cycle_len > best:
                                                                                              best = cycle_len
                                              elif neighbor not in visited:
                                                                    stack.append((neighbor, visited | {neighbor}, length + 1))
                                                    return best


def main():
      if len(sys.argv) < 2:
                print("Usage: python3 my_solution.py <input_file>", file=sys.stderr)
                sys.exit(1)

      filepath = sys.argv[1]

    # Phase 1: Stream file and group edges by (claim_id, status_code)
      # Store adjacency lists per group
      groups = defaultdict(lambda: defaultdict(list))

    with open(filepath, "r", encoding="utf-8") as f:
              for line in f:
                            line = line.rstrip("\n")
                            if not line:
                                              continue
                                          parts = line.split("|")
                            src, dst, claim_id, status_code = parts[0], parts[1], parts[2], parts[3]
                            groups[(claim_id, status_code)][src].append(dst)

          # Phase 2: Find longest cycle across all groups
          best_length = 0
    best_claim = None
    best_status = None

    for (claim_id, status_code), adj in groups.items():
              cycle_len = find_longest_cycle(adj)
              if cycle_len > best_length:
                            best_length = cycle_len
                            best_claim = claim_id
                            best_status = status_code

          if best_claim is not None:
                    print(f"{best_claim},{best_status},{best_length}")
else:
          print("No cycles found", file=sys.stderr)


if __name__ == "__main__":
      main()
