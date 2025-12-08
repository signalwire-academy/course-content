---
layout: default
title: "Level 2 Written Exam"
parent: "Level 2: Intermediate"
nav_order: 98
---

## Certified Agent Engineer

<p style="background: #e7f3fe; border-left: 4px solid #2196F3; padding: 15px; margin: 20px 0;">
<strong>📝 Take Exam:</strong> <a href="https://classroom.github.com/a/M3RPSah6" target="_blank"><strong>Start Level 2 Written Exam</strong></a><br>
<small>Accept the assignment to get your exam repository. Submit answers by creating an issue.</small>
</p>

| | |
|--|--|
| **Duration** | 60 minutes |
| **Questions** | 40 |
| **Passing Score** | 80% (32 correct) |

---

## Section A: Function Results and Actions (8 questions)

**Question 1:** What class is used to return results from SWAIG functions?
- A) FunctionResponse
- B) SwaigFunctionResult
- C) ActionResult
- D) ToolResponse

**Question 2:** Which method transfers a call to another number?
- A) `.transfer()`
- B) `.forward()`
- C) `.connect()`
- D) `.dial()`

**Question 3:** What does `post_process=True` do when adding an action?
- A) Processes the action before the AI speaks
- B) Executes the action after the AI finishes speaking
- C) Adds the action to a processing queue
- D) Validates the action parameters

**Question 4:** Which action type sends an SMS message?
- A) `sms`
- B) `send_message`
- C) `send_sms`
- D) `text`

**Question 5:** How do you store data that persists for the call duration?
- A) `add_action("store_data", {...})`
- B) `update_global_data({...})`
- C) `add_action("save_state", {...})`
- D) `add_action("persist", {...})`

**Question 6:** What happens when you chain multiple `add_action()` calls?
- A) Only the last action executes
- B) Actions execute in sequence
- C) Actions execute in parallel
- D) An error is raised

**Question 7:** Which code correctly transfers a call after speaking?

A)
```python
SwaigFunctionResult("Transferring...").connect("+1555", final=True)
```

B)
```python
SwaigFunctionResult("Transferring...").transfer("+1555", after_speech=True)
```

C)
```python
SwaigFunctionResult("Transferring...").post_action("transfer", "+1555")
```

D)
```python
SwaigFunctionResult("Transferring...", transfer="+1555")
```

**Question 8:** What is the purpose of the `set_end_of_speech_prompt` action?
- A) Sets what the AI says at call end
- B) Changes the prompt after current speech
- C) Defines the end-of-call behavior
- D) Sets the silence timeout

---

## Section B: DataMap Integration (6 questions)

**Question 9:** What is DataMap primarily used for?
- A) Storing agent configuration
- B) Making serverless REST API calls
- C) Mapping data between agents
- D) Creating database schemas

**Question 10:** In a DataMap webhook URL, how do you reference a function argument named `user_id`?
- A) `{user_id}`
- B) `${args.user_id}`
- C) `{{user_id}}`
- D) `%{args.user_id}`

**Question 11:** Which DataMap output field specifies what the AI says?
- A) `speech`
- B) `message`
- C) `response`
- D) `say`

**Question 12:** How do you reference a JSON response field `email` in the output template?
- A) `${response.email}`
- B) `${email}`
- C) `{data.email}`
- D) `{{email}}`

**Question 13:** What field handles API errors in DataMap configuration?
- A) `error_handler`
- B) `on_error`
- C) `error_output`
- D) `fallback`

**Question 14:** Which is a valid DataMap webhook configuration for a POST request?

A)
```python
webhooks=[{
    "url": "https://api.example.com/users",
    "method": "POST",
    "body": {"name": "${args.name}"},
    "output": {"response": "Created ${id}"}
}]
```

B)
```python
webhooks={
    "endpoint": "https://api.example.com/users",
    "type": "POST",
    "data": {"name": "${args.name}"},
    "result": "Created ${id}"
}
```

C)
```python
webhook={
    "url": "https://api.example.com/users",
    "post_data": {"name": "${args.name}"},
    "response": "Created ${id}"
}
```

D)
```python
api_call={
    "url": "https://api.example.com/users",
    "method": "POST",
    "payload": {"name": "${args.name}"}
}
```

---

## Section C: Skills and Contexts (8 questions)

**Question 15:** How do you add a built-in skill to an agent?
- A) `agent.use_skill("datetime")`
- B) `agent.add_skill("datetime")`
- C) `agent.enable_skill("datetime")`
- D) `agent.load_skill("datetime")`

**Question 16:** When creating a custom skill, what class should you inherit from?
- A) `BaseSkill`
- B) `SkillBase`
- C) `CustomSkill`
- D) `AgentSkill`

**Question 17:** Which method defines tools in a custom skill?
- A) `__init__()`
- B) `configure()`
- C) `setup()`
- D) `initialize()`

**Question 18:** What is the purpose of contexts in an agent?
- A) Store global variables
- B) Define multi-step workflows
- C) Handle errors
- D) Configure logging

**Question 19:** How do you switch to a different context from a function?
- A) `SwaigFunctionResult().switch_context("name")`
- B) `SwaigFunctionResult().swml_change_context("name")`
- C) `SwaigFunctionResult().goto_context("name")`
- D) `SwaigFunctionResult().set_context("name")`

**Question 20:** Which class is used to define a context?
- A) `Context`
- B) `ContextBuilder`
- C) `WorkflowContext`
- D) `StepContext`

**Question 21:** What method adds a step to a context?
- A) `context.add_step("message")`
- B) `context.step("message")`
- C) `context.append("message")`
- D) `context.add("message")`

**Question 22:** How do you restrict which functions are available in a context?
- A) `context.allowed_functions(["func1", "func2"])`
- B) `context.set_functions(["func1", "func2"])`
- C) `context.enable(["func1", "func2"])`
- D) `context.functions = ["func1", "func2"]`

---

## Section D: State and Recording (6 questions)

**Question 23:** What is the scope of global data set with `set_global_data()`?
- A) Single function call
- B) Single call/conversation
- C) Agent lifetime (all calls)
- D) Server restart

**Question 24:** How do you access global data stored via `update_global_data()` in a function?
- A) `self.get_global_data()`
- B) `raw_data.get("global_data", {})`
- C) `args.get("global_data")`
- D) `self.global_data`

**Question 25:** Which action controls call recording?
- A) `record`
- B) `toggle_record`
- C) `set_recording`
- D) `control_record`

**Question 26:** What recording state pauses recording without stopping?
- A) `"stop"`
- B) `"pause"`
- C) `"hold"`
- D) `"suspend"`

**Question 27:** Which parameter marks a function as handling sensitive data?
- A) `sensitive=True`
- B) `private=True`
- C) `secure=True`
- D) `protected=True`

**Question 28:** What format provides separate audio channels for caller and agent?
- A) `"mono"`
- B) `"dual"`
- C) `"stereo"`
- D) `"split"`

---

## Section E: Multi-Agent and Deployment (8 questions)

**Question 29:** What class manages multiple agents?
- A) `MultiAgent`
- B) `AgentServer`
- C) `AgentManager`
- D) `ServerAgent`

**Question 30:** How do you specify an agent's URL path?
- A) `AgentBase(path="/sales")`
- B) `AgentBase(route="/sales")`
- C) `AgentBase(endpoint="/sales")`
- D) `AgentBase(url="/sales")`

**Question 31:** In Docker, what directive creates a health check?
- A) `HEALTH`
- B) `CHECK`
- C) `HEALTHCHECK`
- D) `MONITOR`

**Question 32:** What Kubernetes probe checks if a container is running?
- A) `startupProbe`
- B) `readinessProbe`
- C) `livenessProbe`
- D) `healthProbe`

**Question 33:** In AWS Lambda, what function is the entry point?
- A) `main()`
- B) `handler()`
- C) `lambda_handler()`
- D) `entry_point()`

**Question 34:** What is a "cold start" in serverless?
- A) Starting a container in cold storage
- B) Initial container startup adding latency
- C) Restarting after an error
- D) Starting without cached data

**Question 35:** Which command deploys using Serverless Framework?
- A) `serverless publish`
- B) `serverless deploy`
- C) `serverless push`
- D) `serverless launch`

**Question 36:** What method handles Lambda requests in SignalWire agents?
- A) `agent.handle_request()`
- B) `agent.handle_lambda()`
- C) `agent.lambda_request()`
- D) `agent.process_lambda()`

---

## Section F: Short Answer (4 questions)

**Question 37** (2 points): Describe two strategies to minimize cold start latency in serverless deployments.

**Question 38** (2 points): Explain the difference between a cold transfer and a warm transfer.

**Question 39** (2 points): Why should recording be paused when collecting credit card information?

**Question 40** (2 points): What are two advantages of using DataMap instead of writing custom webhook code?

---

## Submission

Submit your answers via GitHub Classroom. Your exam will be auto-graded.

---

## Scoring

- 36-40 correct: Excellent
- 32-35 correct: Good (Pass)
- Below 32: Review required

---

**Next:** [Level 2 Practical Exam](a2-practical-exam)
