# various_algos_on_n-queens

Implementations and benchmarking of local-search algorithms applied to the **N-Queens problem** — placing N queens on an N×N chessboard so that no two attack each other, solved via heuristic search rather than backtracking.

## Why local search for N-Queens?

N-Queens is a classic constraint-satisfaction problem usually taught alongside backtracking, but it's also a convenient sandbox for comparing local-search strategies: the state space is easy to define (one queen per column, its row is the only free variable), and the cost function (number of attacking pairs) is cheap to compute. This repo is a hands-on comparison of a few such strategies and how they scale.

## Algorithms implemented

| File | Algorithm |
|---|---|
| `hill_climbing.py` | Steepest-ascent hill climbing — greedily moves to the neighbor state with the fewest attacking pairs |
| `random_walk.py` | Pure random walk — moves to a randomly chosen neighbor regardless of cost |
| `random_Walk_hill_climbing.py` | Hybrid: random walk combined with hill climbing (e.g. random moves with a chance of a greedy step) |
| `random_state_hill_climbing.py` | Random-restart hill climbing — reruns hill climbing from fresh random states to escape local optima |
| `iterative_depth_random_walk.py` | Random walk bounded by an iterative depth/step limit |
| `random_State.py` / `random_State_mod.py` | Helpers for generating (and modifying) random board states |



## Results

`time_taken_random_walk_hill_climbing.png` benchmarks time-to-solution across the implemented methods.

**TODO:** add 2–3 sentences here on what the benchmark shows — which method converges fastest, how performance changes as N grows, and any surprising failure cases (e.g. does plain random walk ever get stuck / time out?).

## Getting started

```bash
git clone https://github.com/willow788/various_algos_on_n-queens.git
cd various_algos_on_n-queens
python hill_climbing.py
```

**TODO:** confirm/add:
- Python version used
- any dependencies (add a `requirements.txt` if there are any beyond the standard library)
- how N is set (CLI arg, edit a constant in the file, etc.)
- expected output format (prints the board? the number of steps? a success/failure flag?)

## Status

Work in progress — algorithms are implemented and benchmarked individually; next steps could include a shared `Board`/state interface so all algorithms share one implementation, a CLI to pick algorithm + N in one place, and unit tests.

## References

- Russell & Norvig, *Artificial Intelligence: A Modern Approach* — local search chapter (hill climbing, random restarts, simulated annealing)