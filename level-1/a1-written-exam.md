---
layout: default
title: "Level 1 Written Assessment"
parent: "Level 1: Foundations"
nav_order: 99
---

## Certified Agent Developer

<p style="background: #e7f3fe; border-left: 4px solid #2196F3; padding: 15px; margin: 20px 0;">
<strong>📝 Take Exam:</strong> <a href="https://classroom.github.com/a/mJzD3NS1" target="_blank"><strong>Start Level 1 Written Exam</strong></a><br>
<small>Accept the assignment to get your exam repository. Submit answers by creating an issue.</small>
</p>

| | |
|--|--|
| **Duration** | 45 minutes |
| **Questions** | 30 |
| **Passing Score** | 70% (21 correct) |

---

## Section 1: Core Concepts (10 questions)

**Question 1:** What is SWML?
- A) A Python framework for building agents
- B) A JSON document format that tells SignalWire how to handle calls
- C) A text-to-speech engine
- D) A database for storing call data

**Question 2:** Which class is the foundation for all SignalWire agents?
- A) SWMLService
- B) SwaigFunction
- C) AgentBase
- D) VoiceAgent

**Question 3:** What does SWAIG stand for?
- A) SignalWire Agent Integration Gateway
- B) SignalWire AI Gateway
- C) Smart Web AI Generator
- D) Signal Wire Application Interface

**Question 4:** When a call arrives at your agent, what does SignalWire request?
- A) A phone number to forward to
- B) An audio file to play
- C) A SWML document with instructions
- D) User credentials

**Question 5:** What is the purpose of the `ai` verb in SWML?
- A) To play audio files
- B) To create an AI-powered conversation
- C) To transfer calls
- D) To record the call

**Question 6:** What happens when a user asks something that requires a function call?
- A) The call disconnects
- B) SignalWire calls your SWAIG endpoint with the function request
- C) The AI makes up an answer
- D) The call transfers to a human

**Question 7:** Which of these is NOT a SignalWire platform component?
- A) SWML Engine
- B) AI Gateway
- C) Phone Numbers
- D) Code Compiler

**Question 8:** What must every SWML document include?
- A) A phone number
- B) A version field and sections object with main array
- C) User authentication
- D) Audio files

**Question 9:** Why is ngrok useful for agent development?
- A) It compiles Python code faster
- B) It provides a public URL to reach your localhost
- C) It generates SWML automatically
- D) It stores call recordings

**Question 10:** What is the primary purpose of basic authentication on your agent?
- A) To improve call quality
- B) To prevent unauthorized access to your endpoints
- C) To speed up response time
- D) To enable voice recognition

---

## Section 2: Building Agents (10 questions)

**Question 11:** What is the minimum code needed to create a working agent?
- A) `agent = AgentBase(name="my-agent")` and `agent.run()`
- B) `agent = AgentBase()` only
- C) A full class definition with at least 5 methods
- D) A YAML configuration file

**Question 12:** What is the Prompt Object Model (POM)?
- A) A database for storing prompts
- B) A structured way to build prompts using sections
- C) A text-to-speech engine
- D) A testing framework

**Question 13:** Which method adds a prompt section to an agent?
- A) `agent.set_prompt()`
- B) `agent.prompt_add_section()`
- C) `agent.add_prompt()`
- D) `agent.create_section()`

**Question 14:** What do "fillers" do in a voice agent?
- A) Fill in missing words in speech recognition
- B) Provide phrases spoken while processing or waiting
- C) Complete incomplete sentences
- D) Fill database fields

**Question 15:** Which code correctly configures voice?
- A) `agent.voice("English", "en-US", "rime.spore")`
- B) `agent.add_language("English", "en-US", "rime.spore")`
- C) `agent.set_voice("rime.spore")`
- D) `agent.configure_tts("English")`

**Question 16:** What is the purpose of `if __name__ == "__main__":`?
- A) To define the main prompt
- B) To ensure code only runs when file is executed directly
- C) To set the agent name
- D) To configure authentication

**Question 17:** What is wrong with this prompt for a voice agent?
> "Click the blue button to proceed, then fill out the form on page 2."

- A) It's too short
- B) It references visual/web elements that callers can't see
- C) It uses incorrect grammar
- D) Nothing is wrong

**Question 18:** What command generates SWML from an agent file?
- A) `python agent.py --swml`
- B) `swml-generate agent.py`
- C) `swaig-test agent.py --dump-swml`
- D) `signalwire build agent.py`

**Question 19:** Which is a valid language code?
- A) `english-us`
- B) `en-US`
- C) `ENGLISH`
- D) `us-en`

**Question 20:** What is the class-based agent pattern best for?
- A) Simple, one-line agents
- B) Agents with complex logic and multiple methods
- C) Agents without functions
- D) Testing only

---

## Section 3: SWAIG Functions (10 questions)

**Question 21:** What decorator creates a SWAIG function?
- A) `@function`
- B) `@agent.tool`
- C) `@swaig`
- D) `@callable`

**Question 22:** What parameter is REQUIRED in the @tool decorator?
- A) `name`
- B) `parameters`
- C) `description`
- D) `secure`

**Question 23:** What must a SWAIG function return?
- A) A string
- B) A dictionary
- C) A SwaigFunctionResult
- D) None

**Question 24:** How does the AI know when to call a specific function?
- A) Random selection
- B) Based on the function's description matching user intent
- C) Based on the function's name
- D) The user must request it explicitly

**Question 25:** What does this parameter definition create?

```python
def search(query: str, limit: int = 10)
```

- A) Two required parameters
- B) One required (query) and one optional (limit) parameter
- C) Two optional parameters
- D) Invalid syntax

**Question 26:** How do you test a function without making a call?
- A) `python agent.py --test`
- B) `swaig-test agent.py --exec function_name --param value`
- C) `curl localhost:3000/test`
- D) Functions can only be tested with live calls

**Question 27:** What is the purpose of function fillers?
- A) To fill in missing parameters
- B) To provide speech while the function is processing
- C) To complete the function code
- D) To fill the database

**Question 28:** Which is a valid enum parameter definition?
- A) `"enum": "sales, support, billing"`
- B) `"enum": ["sales", "support", "billing"]`
- C) `"type": "enum"`
- D) `"options": ["sales", "support", "billing"]`

**Question 29:** What command lists all functions in an agent?
- A) `swaig-test agent.py --list-tools`
- B) `swaig-test agent.py --functions`
- C) `python agent.py --list`
- D) `signalwire functions agent.py`

**Question 30:** What happens when a function returns an error message in SwaigFunctionResult?
- A) The call disconnects
- B) The AI incorporates the message into its response to the caller
- C) An error log is created
- D) The function is retried automatically

---

## Submission

Submit your answers via GitHub Classroom. Your exam will be auto-graded.

---

## Scoring

- 27-30 correct: Excellent
- 24-26 correct: Good
- 21-23 correct: Pass
- Below 21: Review required

---

**Next:** [Level 1 Practical Exam](a1-practical-exam)
