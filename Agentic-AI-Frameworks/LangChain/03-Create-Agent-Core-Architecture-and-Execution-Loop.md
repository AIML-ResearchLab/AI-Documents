# 03 - create_agent Core Architecture and Execution Loop

## 3.1 create_agent Basics
`create_agent` is the standard LangChain v1 interface for building tool-using agents.

## 3.2 Agent Loop
Core loop: model call -> tool selection/execution -> repeated reasoning -> final response.

## 3.3 Stop Conditions
Agents stop on final answer, iteration limit, or explicit middleware termination.

## 3.4 Runtime Foundation
LangChain agents run on graph-based runtime behavior inherited from LangGraph.

## 3.5 Real-Time Example
Research agent iteratively calls search and summarization tools before returning a final brief.
