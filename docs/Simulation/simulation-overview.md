# Types of simulation 

| Category                   | Simulation Type                   | Description                          | Key Characteristics          | Example Use Case                |
| -------------------------- | --------------------------------- | ------------------------------------ | ---------------------------- | ------------------------------- |
| **Based on Time**          | Static Simulation                 | No time component; snapshot analysis | One-time evaluation          | Risk analysis using Monte Carlo |
|                            | Dynamic Simulation                | Changes over time                    | Time-dependent behavior      | Weather forecasting             |
| **Based on Randomness**    | Deterministic Simulation          | No randomness; fixed output          | Same result every run        | Physics equations               |
|                            | Stochastic Simulation             | Includes randomness                  | Different results per run    | Stock market prediction         |
| **Based on State Change**  | Discrete Event Simulation (DES)   | Changes at specific events           | Event-driven                 | Bank queue system               |
|                            | Continuous Simulation             | Continuous change over time          | Differential equations       | Fluid dynamics                  |
| **Core Simulation Models** | Monte Carlo (MC)                  | Random sampling simulation           | Probabilistic                | Financial risk                  |
|                            | Markov Chain (DTMC/CTMC)          | State transition-based               | Memoryless property          | Disease progression             |
|                            | Hidden Markov Model (HMM)         | Hidden states + observable outputs   | Probabilistic inference      | Speech recognition              |
|                            | Semi-Markov Model                 | Variable state durations             | More realistic than Markov   | Reliability systems             |
|                            | Random Walk                       | Step-by-step random movement         | Path-dependent               | Stock price movement            |
|                            | Poisson Process                   | Random events over time              | Event arrival modeling       | Call center traffic             |
|                            | Brownian Motion                   | Continuous random motion             | Wiener process               | Particle simulation             |
|                            | SDE (Stochastic Differential Eq.) | Continuous + randomness              | Advanced stochastic modeling | Financial derivatives           |
|                            | Gillespie Algorithm (SSA)         | Exact stochastic simulation          | Reaction-based               | Chemical systems                |
| **Advanced Simulation**    | Agent-Based Model (ABM)           | Individual agents interact           | Bottom-up modeling           | Crowd / epidemic                |
|                            | System Dynamics (SD)              | Stocks, flows, feedback loops        | Top-down modeling            | Population growth               |
|                            | Hybrid Simulation                 | Combines multiple models             | MC + ABM + Markov etc.       | Digital twin systems            |
| **Digital Twin Layer**     | Digital Twin Simulation           | Real-time replica of system          | Real-time + predictive       | Smart manufacturing, healthcare |
| **Implementation Type**    | Computer Simulation               | Software-based models                | Scalable                     | AI/ML simulations               |
|                            | Physical Simulation               | Real-world simulators                | Hardware-based               | Flight simulator                |
| **Application-Based**      | Business Simulation               | Business processes modeling          | Decision support             | Supply chain                    |
|                            | Medical Simulation                | Healthcare systems modeling          | Patient modeling             | Surgery training                |
|                            | Military Simulation               | Defense scenarios                    | Strategy testing             | War games                       |
|                            | Engineering Simulation            | Physical system modeling             | High precision               | CFD, structural analysis        |

## 📌 Definition

A **Simulation Engine** is a system that uses **mathematical and probabilistic models** to simulate how a system evolves over time.


