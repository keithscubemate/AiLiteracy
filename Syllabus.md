
# AI Literacy Study Plan

## 1. Classical Foundations of AI & ML

### Key Concepts

- Symbolic AI (rules, expert systems)
    
- Statistical ML (regression, clustering, trees, SVMs, boosting)
    
- Neural networks (perceptrons, CNNs, RNNs)
    
- Genetic / evolutionary algorithms
    

### Resources

- [Bishop – _Pattern Recognition and Machine Learning_ (book)](https://www.microsoft.com/en-us/research/people/cmbishop/prml-book/) (theory-heavy but foundational)
    
- [Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/) (practical)
    
- [3Blue1Brown Neural Networks video series](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) (visual explanation)
    
- [Genetic Algorithms overview (Nature of Code)](https://natureofcode.com/genetic-algorithms/)
    

### Exercise

- Train a simple decision tree on a CSV (e.g., iris dataset).
    
- Implement a tiny neural net from scratch (e.g., XOR problem).
    

### Check Your Literacy

- Can you explain why a decision tree is more interpretable than a neural net?
    
- What kind of problems are evolutionary algorithms well-suited for?
    

---

## 2. Modern AI: LLMs and the Transformer Era

### Key Concepts

- Embeddings & vector databases
    
- Transformer architecture & attention
    
- LLMs as next-token predictors
    
- RAG (retrieval-augmented generation)
    
- Agents & tool use
    

### Resources

- [Attention Is All You Need (original paper, 2017)](https://arxiv.org/abs/1706.03762)
    
- [Jay Alammar – _The Illustrated Transformer_](https://jalammar.github.io/illustrated-transformer/)
    
- [Lil’Log – _Illustrated Guide to Transformers_](https://lilianweng.github.io/posts/2018-06-24-attention/)
    
- [Pinecone – Vector DB Introduction](https://www.pinecone.io/learn/vector-database/)
    
- [LangChain Docs – Getting Started](https://python.langchain.com/docs/get_started/introduction)
    

### Exercise

- Use OpenAI or Hugging Face to embed a few paragraphs and run a semantic search.
    
- Build a toy RAG pipeline with a vector DB + GPT API.
    

### Check Your Literacy

- Why are embeddings useful beyond plain keyword search?
    
- How does RAG differ from fine-tuning?
    

---

## 3. When Not to Use AI

### Key Concepts

- Regex for structured pattern matching
    
- Business rules for deterministic workflows
    
- Data scarcity as a blocker for ML
    
- Need for interpretability / determinism
    

### Resources

- [RegexOne – Interactive regex practice](https://regexone.com/)
    
- [Google Cloud – When not to use ML](https://cloud.google.com/blog/products/ai-machine-learning/when-should-you-not-use-machine-learning)
    

### Exercise

- Write a regex that extracts phone numbers from text, then compare with asking an LLM to do it.
    

### Check Your Literacy

- Can you explain why regex is cheaper/faster than LLMs for pattern matching?
    
- What’s a real-world case where rules outperform machine learning?
    

---

## 4. The Messy Middle: Hybrid Systems

### Key Concepts

- Combining rules, traditional ML, and LLMs
    
- Tradeoffs: cost, accuracy, explainability
    
- AI orchestration in workflows
    

### Resources

- [Microsoft – Responsible AI design practices](https://learn.microsoft.com/en-us/azure/architecture/guide/responsible-ai/)
    
- [Hybrid AI Systems Overview (Medium article)](https://towardsdatascience.com/hybrid-ai-systems-rules-and-machine-learning-working-together-9f9a5e58e2d8)
    

### Exercise

- Build a chatbot where simple queries (e.g., “What’s 2+2?”) go through a rule, and everything else goes to an LLM.
    

### Check Your Literacy

- Why is hybrid often more practical than “pure” AI?
    
- How do cost considerations influence architecture choice?
    

---

## 5. Limits of AI Today

### Key Concepts

- Fluency vs. reasoning
    
- Data/compute limits
    
- Hallucinations & reliability
    
- Ethical concerns (bias, misuse, privacy)
    

### Resources

- [Emily Bender’s “Stochastic Parrots” paper](https://dl.acm.org/doi/10.1145/3442188.3445922)
    
- [Stanford HAI – AI Index Report (latest edition)](https://aiindex.stanford.edu/report/)
    

### Exercise

- Collect 3 examples of LLM hallucinations. Try prompting differently to mitigate them.
    

### Check Your Literacy

- Can you clearly explain the difference between “predicting the next token” and “understanding”?
    
- What are the most important risks of AI adoption in your workplace?
    

---

## 6. Putting It All Together (Presentation Prep)

- **Goal framing:** AI = toolbox, not magic.
    
- **Structure for coworkers:**
    
    1. What is AI? (history + buckets)
        
    2. How do modern systems work?
        
    3. When not to use AI
        
    4. Hybrids & tradeoffs
        
    5. Limits and literacy
        
- **Activity ideas for audience:**
    
    - Compare regex vs. LLM for a pattern task.
        
    - Try a semantic search demo.
        
    - Discuss “would you use AI here?” case studies.
        
