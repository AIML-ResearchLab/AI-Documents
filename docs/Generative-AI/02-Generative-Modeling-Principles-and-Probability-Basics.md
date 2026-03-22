# 02 - Generative Modeling Principles and Probability Basics

## 2.1 Core Objective

**Goal:** Learn the underlying data distribution and generate realistic samples.

**Intuition**

A generative model tries to answer:

`“What does real data look like, and how can I create new data that looks similar?”`

Mathematically, we want to learn: 

P(x)

Where:

- x = data sample (text, image, audio, etc.)
- P(x) = probability distribution of real data

**Example (Text Generation)**

- Training data: customer support chats
- Model learns: probability of word sequences
- Output: new realistic support responses


## 2.2 Probabilistic View

**Objective:**

Maximize how well the model explains the data.

**Likelihood Maximization**

\max_{\theta} \prod_{i=1}^{N} P_\theta(x_i)

Or (more commonly):

\max_{\theta} \sum_{i=1}^{N} \log P_\theta(x_i)

Where:

- 𝜃 = model parameters
- 𝑥𝑖 = training samples


**Why Log?**

- Avoid numerical underflow
- Converts multiplication → addition
- Easier optimization

**Surrogate Objectives**

Sometimes 𝑃(𝑥) is hard to compute → use approximations:

| Model Type     | Objective                   |
| -------------- | --------------------------- |
| Autoregressive | Next-token likelihood       |
| VAE            | ELBO (Evidence Lower Bound) |
| GAN            | Minimax loss                |
| Diffusion      | Noise prediction loss       |



- Avoid numerical underflow
## 2.3 Model Families
autoregressive, latent-variable, adversarial, and diffusion paradigms.

**Autoregressive Models (Sequential)**

P(x)=t=1∏T​P(xt​∣x<t​)

P(x) = \prod_{t=1}^{T} P(x_t \mid x_{<t})

**Examples:**

- GPT, LLMs




## 2.4 Real-Time Example
Generate synthetic support utterances from learned intent distribution.

**How it works:**

- Predict next token given previous tokens

**Pros:**

- High-quality text generation
 
**Cons:**

Slow generation (token by token)



## 2.5 Latent Variable Models (Representation Learning)

Introduce hidden variable 𝑧:
P(x)=∫P(x∣z)P(z)dz

P(x) = \int P(x \mid z) P(z) dz

**Examples:**

- VAE (Variational Autoencoders)

**Idea:**

- Learn compressed representation
- Generate by sampling latent space


## 2.6 Adversarial Models (GANs)

Two networks:

- Generator (G)
- Discriminator (D)


Objective:

\min_G \max_D ; \mathbb{E}{x \sim p{data}}[\log D(x)] + \mathbb{E}_{z \sim p(z)}[\log (1 - D(G(z)))]


**Examples:**

- Image generation (StyleGAN)

**Pros:**

- Very realistic outputs

**Cons:**

- Training instability
- Mode collapse

## 2.7 Diffusion Models (State-of-the-Art for Images)

**Idea:**

- Add noise → remove noise step-by-step

xt​=noise(xt−1​)

Model learns reverse process:

P(xt−1∣xt)

**Examples:**

- Stable Diffusion
- DALL·E


**Pros:**

- High-quality images
- Stable training

**Cons:**

- Slow inference


## Real-Time Example (Enterprise Use Case)

**📞 Scenario: Customer Support AI**

**Goal:** Generate synthetic support utterances

**Workflow:**

1. **Data Collection**
    - Historical support chats

2. **Distribution Learning**
- Model learns:
    - Intent patterns
    - Language style
    - Response structures

3. **Generation**
- Input: “Payment failed”
- Output:
    - “We’re sorry, please retry…”
    - “Your payment didn’t go through…”

**Probabilistic View**

Model learns:

P(response∣intent)

P(\text{response} \mid \text{intent})

## Architect-Level Insights

1. **Distribution Learning vs Memorization**

- Good model → generalizes
- Bad model → memorizes

2. **Mode Coverage vs Mode Collapse**

- GAN risk: only generate few patterns
- Diffusion: better coverage

| Model          | Quality   | Speed | Stability   |
| -------------- | --------- | ----- | ----------- |
| Autoregressive | High      | Slow  | Stable      |
| VAE            | Medium    | Fast  | Stable      |
| GAN            | Very High | Fast  | Unstable    |
| Diffusion      | Very High | Slow  | Very Stable |


## Final Summary

- Generative AI = **probability modeling problem**
- Core goal = learn 𝑃(𝑥) or 𝑃(𝑥∣𝑐𝑜𝑛𝑡𝑒𝑥𝑡)
- Different models = different approximations of distribution
- Real-world systems = combine:
    - Autoregressive (LLMs)
    - Retrieval (RAG)
    - Diffusion (multimodal)


## What is Generative Modeling?

![alt text](image.png)

![alt text](image-1.png)

![alt text](image-2.png)

![alt text](image-3.png)


## Probabilistic View — How Models Learn

![alt text](image-4.png)

![alt text](image-5.png)

![alt text](image-6.png)

## Model Families (VERY IMPORTANT)

**Autoregressive Models (LLMs)**

![alt text](image-7.png)

![alt text](image-8.png)

![alt text](image-9.png)

![alt text](image-10.png)

**Latent Variable Models (VAE)**

![alt text](image-11.png)

![alt text](image-12.png)

![alt text](image-13.png)

![alt text](image-14.png)


**Adversarial Models (GANs)**

![alt text](image-15.png)

![alt text](image-16.png)

![alt text](image-17.png)

**Diffusion Models (Modern SOTA)**

![alt text](image-18.png)

![alt text](image-19.png)

![alt text](image-20.png)

![alt text](image-21.png)


**Real-Time Example**

![alt text](image-22.png)

![alt text](image-23.png)

![alt text](image-24.png)

![alt text](image-25.png)

