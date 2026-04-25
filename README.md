# Singapore Bus Route Project

Goal: construct a route that visits every bus stop in Singapore.

The problem is modelled as a directed graph traversal problem, where:
- vertices = bus stops
- edges = valid bus transitions
- objective = visit all vertices at least once, while minimising repetition

---

## Project Structure

```text
prototype_py/   initial Python prototype (data pipeline + early traversal logic)
go/             rewrite in Go (clean architecture + performance focus)
docs/           LaTeX writeups (problem statement, system design, heuristics)
```

https://github.com/rpeky/Singapore-Bus-Route-Project/wiki
