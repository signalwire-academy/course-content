---
layout: default
title: "Level 1 Practical Assessment"
parent: "Level 1: Foundations"
nav_order: 99
---

# Level 1 Practical Assessment

<p style="background: #e7f3fe; border-left: 4px solid #2196F3; padding: 15px; margin: 20px 0;">
<strong>🎯 Assignment:</strong> <a href="https://classroom.github.com/a/TmGI_vWG" target="_blank"><strong>Accept this exam on GitHub Classroom</strong></a><br>
<small>You'll get your own repository. Submit your code and a recording (wav, mp3, or mp4) of your live demo.</small>
</p>

## Certified Agent Developer

| | |
|--|--|
| **Duration** | 2 hours |
| **Passing Score** | 70% (automated) + manual review |
| **Grading** | Automated checks + instructor review |

---

## Overview

Build a complete voice AI agent based on the requirements below. You will be evaluated on:

- Agent functionality (40%)
- Code quality (20%)
- SWAIG functions (25%)
- Live demonstration (15%)

---

## Scenario

**TechSupport Inc.** needs a voice AI agent for their customer support line. Customers call to:

1. Get help with common technical issues
2. Check the status of support tickets
3. Create new support tickets

---

## Requirements

### Part 1: Basic Agent Setup (25 points)

Create an agent with:

- [ ] Appropriate name and route
- [ ] Professional prompt with clear role definition
- [ ] At least 3 prompt sections (Role, Guidelines, Process)
- [ ] Voice configuration with appropriate voice selection
- [ ] At least 3 filler phrases
- [ ] Basic authentication configured

**Deliverable:** `techsupport_agent.py`

---

### Part 2: SWAIG Functions (40 points)

Implement two functions:

#### Function 1: Check Ticket Status (20 points)

```text
Name: check_ticket_status
Parameter: ticket_id (string)
```

Requirements:

- [ ] Accept ticket ID as parameter
- [ ] Return status for valid tickets
- [ ] Handle invalid ticket IDs gracefully
- [ ] Include helpful information in response

Use this mock data:

```python
TICKETS = {
    "T-1001": {"status": "open", "issue": "Login problems", "created": "Monday"},
    "T-1002": {"status": "in_progress", "issue": "Slow performance", "created": "Tuesday"},
    "T-1003": {"status": "resolved", "issue": "Password reset", "created": "Last week"},
}
```

#### Function 2: Create Support Ticket (20 points)

```text
Name: create_ticket
Parameters:
  - issue_type (string, enum: ["login", "performance", "billing", "other"])
  - description (string)
```

Requirements:

- [ ] Accept issue type and description
- [ ] Generate a ticket number (can be mock)
- [ ] Return confirmation with ticket number
- [ ] Use appropriate fillers while "processing"

---

### Part 3: Testing (15 points)

Demonstrate using swaig-test:

- [ ] Show `--list-tools` output with both functions
- [ ] Execute `check_ticket_status` with valid ticket
- [ ] Execute `check_ticket_status` with invalid ticket
- [ ] Execute `create_ticket` with parameters
- [ ] Show `--dump-swml` output

**Deliverable:** Screenshot or terminal log of tests

---

### Part 4: Live Demonstration (20 points)

Deploy and demonstrate:

- [ ] Agent running locally
- [ ] ngrok tunnel active
- [ ] SignalWire phone number configured
- [ ] Make live call demonstrating:
  - Greeting and conversation flow
  - Checking a ticket status
  - Creating a new ticket

**Evaluation Criteria:**

- Natural conversation flow
- Functions called appropriately
- Error handling works
- Professional voice experience

---

## Submission Requirements

1. **Code File:** `techsupport_agent.py`
2. **Test Output:** Screenshots or copy of swaig-test results
3. **Configuration:** SignalWire URL used
4. **Demo Notes:** Brief notes on your live call

---

## Grading Rubric

### Automated Checks (85 points)

These checks run automatically when you push your code:

| Criteria | Points | Type |
|----------|--------|------|
| Agent loads without errors | 10 | Automated |
| Generates valid SWML | 10 | Automated |
| Has prompt sections configured | 5 | Automated |
| check_ticket_status function exists | 10 | Automated |
| create_ticket function exists | 10 | Automated |
| Valid ticket lookup returns data | 10 | Automated |
| Invalid ticket handled gracefully | 5 | Automated |
| Ticket creation returns confirmation | 5 | Automated |
| Language configured | 10 | Automated |
| Fillers configured | 10 | Automated |

### Manual Review (15 points)

After passing automated checks, an instructor will review:

| Criteria | Points |
|----------|--------|
| Code quality and organization | 10 |
| Live demonstration recording | 5 |

---

## Starter Template

```python
#!/usr/bin/env python3
"""TechSupport Agent - Level 1 Assessment"""

import os
from signalwire_agents import AgentBase, SwaigFunctionResult

# Your code here...

if __name__ == "__main__":
    agent.run()
```

---

## Tips

1. **Start simple** - Get the basic agent working first
2. **Test incrementally** - Use swaig-test after each change
3. **Read error messages** - They tell you what's wrong
4. **Check the SWML** - Verify your configuration appears
5. **Practice the call** - Do a dry run before assessment

---

## Time Management

| Task | Suggested Time |
|------|----------------|
| Part 1: Setup | 30 minutes |
| Part 2: Functions | 45 minutes |
| Part 3: Testing | 15 minutes |
| Part 4: Demo | 30 minutes |

---

Good luck!
