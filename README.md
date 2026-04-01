# Routing Cycle Detector

Finds the longest routing cycle in a large, pipe-delimited claims routing file.

## Problem

Given a newline-delimited text file where each line represents a claim being routed between internal systems:

```
<source_system>|<destination_system>|<claim_id>|<status_code>
```

Find the longest simple directed cycle where all hops share the same `claim_id` and `status_code`.

## Usage

```bash
python3 my_solution.py large_input_v1.txt
```

Output format:

```
<claim_id>,<status_code>,<cycle_length>
```

## Solution

**Result:** `190017,190116,10` (a 10-hop cycle)

**Runtime:** ~30 seconds on 11M lines

## Approach

1. Stream the file line-by-line, grouping edges into adjacency lists keyed by `(claim_id, status_code)`
2. 2. For each group, run iterative DFS from every node to find the longest simple cycle back to start
   3. 3. Track visited nodes using frozensets to ensure cycles are simple (no repeated nodes)
     
      4. ## Files
     
      5. - `my_solution.py` - Main solution script
         - - `solution.txt` - Output of the script on the provided dataset
           - - `explanation.txt` - Brief strategy explanation
