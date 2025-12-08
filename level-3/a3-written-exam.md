---
layout: default
title: "Level 3 Written Exam"
parent: "Level 3: Advanced"
nav_order: 98
---

## Certified Voice AI Architect

<p style="background: #e7f3fe; border-left: 4px solid #2196F3; padding: 15px; margin: 20px 0;">
<strong>📝 Take Exam:</strong> <a href="https://classroom.github.com/a/p4u1IUB1" target="_blank"><strong>Start Level 3 Written Exam</strong></a><br>
<small>Accept the assignment to get your exam repository. Submit answers by creating an issue.</small>
</p>

| | |
|--|--|
| **Duration** | 75 minutes |
| **Questions** | 50 |
| **Passing Score** | 80% (40 correct) |

---

## Section A: Architecture Patterns (12 questions)

**Question 1:** Which pattern uses a central entry point to distribute calls to specialized agents?
- A) Skill Composition
- B) Gateway Router
- C) Context State Machine
- D) DataMap Integration

**Question 2:** When should you use the Skill Composition pattern?
- A) When you need call routing logic
- B) When you have common functionality across agents
- C) When you need complex state transitions
- D) When you need serverless API integration

**Question 3:** Which is an example of the "Monolithic Agent" anti-pattern?
- A) Using environment variables for configuration
- B) One agent with 50 functions covering all domains
- C) Using multiple specialized agents
- D) Implementing health checks

**Question 4:** What is the recommended approach for sharing state in horizontally scaled agents?
- A) Store state in local memory
- B) Use global variables
- C) Externalize state to Redis or a database
- D) Store state in the SWML document

**Question 5:** Which anti-pattern exposes implementation details to callers?
- A) Hardcoded Configuration
- B) Synchronous External Calls
- C) Exposing Internal Errors
- D) Monolithic Agent

**Question 6:** What is an Architecture Decision Record (ADR)?
- A) A log of all API calls
- B) A document explaining why a decision was made
- C) A list of system errors
- D) A performance benchmark

**Question 7:** Which principle suggests agents should have focused, specific responsibilities?
- A) Defense in Depth
- B) Single Responsibility
- C) Fail Secure
- D) Least Privilege

**Question 8:** What is the primary benefit of the Context State Machine pattern?
- A) Better API integration
- B) Structured multi-step workflows
- C) Faster response times
- D) Easier deployment

**Question 9:** Which scaling pattern requires stateless agents?
- A) Vertical scaling
- B) Horizontal scaling
- C) Cold start scaling
- D) Serverless scaling

**Question 10:** What should be documented in agent documentation?
- A) Only the agent name
- B) Endpoints, functions, dependencies, and configuration
- C) Just the code
- D) Marketing materials

**Question 11:** Which is NOT a recommended practice for agent architecture?
- A) Use environment variables for secrets
- B) Implement health checks
- C) Put all business logic in one agent
- D) Document architectural decisions

**Question 12:** What is the purpose of a Gateway Router in a multi-agent system?
- A) Process payments
- B) Route calls to appropriate specialized agents
- C) Store customer data
- D) Generate reports

---

## Section B: Knowledge and RAG (8 questions)

**Question 13:** What does RAG stand for?
- A) Rapid Agent Generation
- B) Retrieval-Augmented Generation
- C) Remote API Gateway
- D) Real-time Audio Gateway

**Question 14:** Which CLI tool builds search indexes for knowledge bases?
- A) swaig-test
- B) sw-agent-init
- C) sw-search
- D) sw-index

**Question 15:** What is the purpose of "chunking" in knowledge base preparation?
- A) Compress the data
- B) Break content into searchable segments
- C) Encrypt sensitive information
- D) Validate document format

**Question 16:** Which parameter controls how many search results are returned?
- A) `distance`
- B) `count`
- C) `limit`
- D) `max_results`

**Question 17:** What is the `distance` parameter in search configuration?
- A) Network latency
- B) Similarity threshold for results
- C) Maximum document size
- D) Search timeout

**Question 18:** How can you combine static knowledge with live data?
- A) You cannot combine them
- B) Use search skill for static, DataMap for live
- C) Put all data in the knowledge base
- D) Only use live APIs

**Question 19:** What should you do when the knowledge base doesn't have an answer?
- A) Make up an answer
- B) Admit limits and offer alternatives
- C) Hang up the call
- D) Repeat the question

**Question 20:** What is the recommended chunk size for FAQ content?
- A) 50 tokens
- B) 200 tokens
- C) 1000 tokens
- D) 5000 tokens

---

## Section C: Performance Optimization (8 questions)

**Question 21:** What is a "cold start" in serverless deployments?
- A) Running without cache
- B) Initial container/runtime startup latency
- C) Server reboot
- D) Network timeout

**Question 22:** Which technique keeps users engaged during slow operations?
- A) Hangup
- B) Fillers
- C) Transfer
- D) Recording

**Question 23:** What is the recommended timeout for external API calls in voice agents?
- A) 30 seconds
- B) 2-5 seconds
- C) 1 minute
- D) No timeout needed

**Question 24:** Which caching decorator is built into Python?
- A) @cache
- B) @lru_cache
- C) @memoize
- D) @cached

**Question 25:** How can you run multiple warehouse checks in parallel?
- A) Sequential loops
- B) ThreadPoolExecutor
- C) Longer timeouts
- D) Multiple agents

**Question 26:** What makes prompts "optimized" for performance?
- A) Using more words
- B) Being concise and focused
- C) Including all possible scenarios
- D) Using complex language

**Question 27:** What is the purpose of the `end_of_speech_timeout` parameter?
- A) Call duration limit
- B) Time to wait after user stops speaking
- C) Function timeout
- D) Recording duration

**Question 28:** Which metric type is best for measuring function latency?
- A) Counter
- B) Gauge
- C) Histogram
- D) Summary

---

## Section D: Security and Compliance (10 questions)

**Question 29:** What should happen to call recording when collecting credit card numbers?
- A) Continue recording
- B) Pause recording
- C) Stop recording permanently
- D) Increase volume

**Question 30:** What is the maximum number of PIN attempts before lockout (best practice)?
- A) 1
- B) 3
- C) 10
- D) Unlimited

**Question 31:** Which parameter marks a function as handling sensitive data?
- A) `private=True`
- B) `secure=True`
- C) `sensitive=True`
- D) `protected=True`

**Question 32:** What should be stored in logs regarding credit card numbers?
- A) Full card number
- B) Encrypted card number
- C) Last 4 digits only
- D) Nothing about cards

**Question 33:** Which type of authentication protects SWML endpoints?
- A) OAuth
- B) Basic Auth
- C) API Keys only
- D) No authentication needed

**Question 34:** What is tokenization in payment processing?
- A) Breaking text into words
- B) Replacing card numbers with secure tokens
- C) Encrypting all data
- D) Validating card format

**Question 35:** Which input pattern might indicate prompt injection?
- A) "What time is it?"
- B) "ignore previous instructions"
- C) "What's my balance?"
- D) "Transfer to sales"

**Question 36:** What should happen when an account is locked due to failed PIN attempts?
- A) Keep trying
- B) End the call with guidance
- C) Transfer to sales
- D) Reset the PIN automatically

**Question 37:** What is the purpose of timing-safe comparison for PIN verification?
- A) Faster verification
- B) Prevent timing attacks
- C) Better logging
- D) Simpler code

**Question 38:** Which data should NEVER be in logs?
- A) Call ID
- B) Timestamps
- C) Full credit card numbers
- D) Function names

---

## Section E: Monitoring and Troubleshooting (12 questions)

**Question 39:** What are the three pillars of observability?
- A) Speed, Size, Security
- B) Logs, Metrics, Traces
- C) CPU, Memory, Network
- D) Input, Output, Errors

**Question 40:** Which log format enables easy querying and analysis?
- A) Plain text
- B) Structured JSON
- C) CSV
- D) XML

**Question 41:** What is a correlation ID used for?
- A) Measuring latency
- B) Tracking requests across systems
- C) Counting errors
- D) Storing state

**Question 42:** Which Prometheus metric type tracks current values (like active calls)?
- A) Counter
- B) Gauge
- C) Histogram
- D) Summary

**Question 43:** What should a health check endpoint verify?
- A) Only that the server responds
- B) Agent, database, and external API status
- C) Just CPU usage
- D) Only memory

**Question 44:** Which alert would indicate potential AI handling issues?
- A) High CPU usage
- B) High transfer rate
- C) Low memory
- D) High disk usage

**Question 45:** What does `histogram_quantile(0.95, ...)` calculate?
- A) Average latency
- B) 95th percentile latency
- C) Maximum latency
- D) Minimum latency

**Question 46:** What is the purpose of the `swaig-test` command `--dump-swml`?
- A) Test a function
- B) Output the SWML document
- C) List all tools
- D) Start the server

**Question 47:** How do you test a specific function with swaig-test?
- A) `--exec function_name`
- B) `--test function_name`
- C) `--call function_name`
- D) `--run function_name`

**Question 48:** What indicates a "degraded" health status?
- A) All checks pass
- B) Some checks fail but system works
- C) Complete system failure
- D) Network timeout

**Question 49:** Which pattern helps handle temporary external service failures?
- A) Immediate failure
- B) Circuit breaker
- C) Ignore errors
- D) Infinite retry

**Question 50:** What should logs EXCLUDE for security?
- A) Timestamps
- B) Sensitive data (passwords, card numbers)
- C) Function names
- D) Call IDs

---

## Submission

Submit your answers via GitHub Classroom. Your exam will be auto-graded.

---

## Scoring

- 45-50 correct: Excellent
- 40-44 correct: Good (Pass)
- Below 40: Review required

---

**Next:** [Level 3 Practical Exam](a3-practical-exam)
