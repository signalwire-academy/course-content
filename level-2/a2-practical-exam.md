---
layout: default
title: "Level 2 Practical Exam: Certified Agent Engineer"
parent: "Level 2: Intermediate"
nav_order: 99
---

# Level 2 Practical Assessment

<p style="background: #e7f3fe; border-left: 4px solid #2196F3; padding: 15px; margin: 20px 0;">
<strong>🎯 Assignment:</strong> <a href="https://classroom.github.com/a/zbinSMy6" target="_blank"><strong>Accept this exam on GitHub Classroom</strong></a><br>
<small>You'll get your own repository. Submit your code and a recording (wav, mp3, or mp4) of your live demo.</small>
</p>

## Certified Agent Engineer

| | |
|--|--|
| **Duration** | 3 hours |
| **Passing Score** | 70% (automated) + manual review |
| **Grading** | Automated checks + instructor review |

---

## Exam Overview

Build a complete customer service agent system that demonstrates mastery of Level 2 concepts:

- Function results and actions
- State management
- Call recording compliance
- Multi-context workflows
- Transfer patterns
- Production deployment

---

## Scenario: TechSupport Pro

You are building a technical support system for "TechSupport Pro" that handles:

1. Customer identification
2. Issue triage and troubleshooting
3. Ticket creation
4. Escalation to specialists

---

## Requirements

### Part 1: Agent Structure (20 points)

Create an agent with the following specifications:

**Basic Setup:**

- Name: `techsupport-agent`
- Route: `/support`
- Language: English (en-US) with appropriate TTS

**Prompt Configuration:**

- Clear role definition as a technical support agent
- Bullet list of capabilities
- Instructions for handling sensitive customer data

**Expected Deliverable:** Base agent class with prompt configuration

---

### Part 2: Customer Identification (20 points)

Implement customer identification with state management:

**Requirements:**

- Function to identify customer by phone or email
- Store customer info in metadata (id, name, tier)
- Greet returning customers by name
- Handle unknown customers gracefully

**Customer Data (simulated):**

```python
CUSTOMERS = {
    "john@example.com": {"id": "C001", "name": "John Smith", "tier": "premium"},
    "+15551234567": {"id": "C002", "name": "Jane Doe", "tier": "standard"},
    "mike@example.com": {"id": "C003", "name": "Mike Wilson", "tier": "premium"}
}
```

**Expected Functions:**

- `identify_customer(identifier: str)` - Look up and store customer

---

### Part 3: Multi-Context Workflow (25 points)

Implement a three-context workflow:

**Context 1: Greeting**

- Welcome message
- Available functions: `identify_customer`, `get_status`

**Context 2: Triage**

- Collect issue details
- Available functions: `describe_issue`, `create_ticket`, `check_knowledge_base`

**Context 3: Resolution**

- Resolve or escalate
- Available functions: `resolve_ticket`, `escalate_ticket`, `schedule_callback`

**Required Transitions:**

- Greeting → Triage (after customer identified)
- Triage → Resolution (after ticket created)
- Resolution → Greeting (after resolution or escalation)

---

### Part 4: Issue Handling Functions (20 points)

Implement the following functions with proper action chaining:

**`describe_issue(issue_type, description)`**

- Store issue in metadata
- Move to triage context if not already there

**`create_ticket(priority)`**

- Generate ticket ID
- Store ticket info in metadata
- Move to resolution context

**`resolve_ticket(resolution_notes)`**

- Update ticket status
- Send confirmation SMS to customer
- Return to greeting context

**`escalate_ticket(specialist_type)`**

- Set escalation reason in metadata
- Transfer to appropriate specialist (post-process)

**Specialist Numbers:**

```python
SPECIALISTS = {
    "billing": "+15551111111",
    "technical": "+15552222222",
    "account": "+15553333333"
}
```

---

### Part 5: Recording Compliance (10 points)

Implement recording controls:

**Requirements:**

- Enable stereo MP3 recording
- Pause recording when collecting sensitive info
- Resume after sensitive info collected
- Include disclosure in agent prompt

**Required Function:**

- `secure_mode()` - Pause recording, inform caller

---

### Part 6: Deployment Configuration (5 points)

Create production-ready configuration:

**Required Files:**

- `Dockerfile` with health check
- `requirements.txt` with dependencies
- `.env.example` with all required variables

---

## Deliverables

Submit the following files:

1. `techsupport_agent.py` - Main agent code
2. `Dockerfile` - Container configuration
3. `requirements.txt` - Dependencies
4. `.env.example` - Environment template

---

## Grading Rubric

### Automated Checks (85 points)

These checks run automatically when you push your code:

| Criteria | Points | Type |
|----------|--------|------|
| Agent loads without errors | 10 | Automated |
| Generates valid SWML | 10 | Automated |
| identify_customer function exists | 5 | Automated |
| identify_customer finds known customer | 10 | Automated |
| Contexts defined | 10 | Automated |
| describe_issue function exists | 5 | Automated |
| create_ticket function exists | 5 | Automated |
| resolve_ticket function exists | 5 | Automated |
| escalate_ticket function exists | 5 | Automated |
| create_ticket returns ticket ID | 5 | Automated |
| Transfer capability configured | 5 | Automated |
| Recording configured | 5 | Automated |
| secure_mode function exists | 5 | Automated |

### Manual Review (15 points)

After passing automated checks, an instructor will review:

| Criteria | Points |
|----------|--------|
| Deployment files (Dockerfile, etc.) | 5 |
| Code quality and organization | 5 |
| Live demonstration recording | 5 |

---

## Sample Solution Structure

```python
#!/usr/bin/env python3
"""TechSupport Pro Agent - Level 2 Practical Exam"""

import os
from datetime import datetime
from signalwire_agents import AgentBase, SwaigFunctionResult
from signalwire_agents.contexts import ContextBuilder


class TechSupportAgent(AgentBase):
    CUSTOMERS = {
        "john@example.com": {"id": "C001", "name": "John Smith", "tier": "premium"},
        "+15551234567": {"id": "C002", "name": "Jane Doe", "tier": "standard"},
        "mike@example.com": {"id": "C003", "name": "Mike Wilson", "tier": "premium"}
    }

    SPECIALISTS = {
        "billing": "+15551111111",
        "technical": "+15552222222",
        "account": "+15553333333"
    }

    def __init__(self):
        super().__init__(name="techsupport-agent", route="/support")

        # Configure prompts
        self._configure_prompts()

        # Configure recording
        self._configure_recording()

        # Configure language
        self.add_language("English", "en-US", "rime.spore")

        # Set up contexts and functions
        self._setup_contexts()
        self._setup_functions()

    def _configure_prompts(self):
        self.prompt_add_section(
            "Role",
            "You are a technical support agent for TechSupport Pro. "
            "This call may be recorded for quality purposes."
        )

        self.prompt_add_section(
            "Capabilities",
            bullets=[
                "Identify customers by phone or email",
                "Create and manage support tickets",
                "Troubleshoot common issues",
                "Escalate to specialists when needed"
            ]
        )

        self.prompt_add_section(
            "Privacy",
            "When collecting sensitive information, always pause recording first."
        )

    def _configure_recording(self):
        self.set_params({
            "record_call": True,
            "record_format": "mp3",
            "record_stereo": True
        })

    def _setup_contexts(self):
        # Greeting context
        greeting = ContextBuilder("greeting")
        greeting.add_step("Welcome to TechSupport Pro! How can I help you today?")
        greeting.set_functions(["identify_customer", "get_status"])
        self.add_context(greeting)

        # Triage context
        triage = ContextBuilder("triage")
        triage.add_step("I can help you with that. Let me get some details.")
        triage.set_functions(["describe_issue", "create_ticket", "check_knowledge_base"])
        self.add_context(triage)

        # Resolution context
        resolution = ContextBuilder("resolution")
        resolution.add_step("Let's work on resolving this for you.")
        resolution.set_functions(["resolve_ticket", "escalate_ticket", "schedule_callback", "secure_mode"])
        self.add_context(resolution)

    def _setup_functions(self):
        # Implementation of all required functions
        # ... (students implement this)
        pass


if __name__ == "__main__":
    agent = TechSupportAgent()
    agent.run()
```

---

## Testing Your Solution

```bash
# Test agent SWML output
swaig-test techsupport_agent.py --dump-swml

# List all functions
swaig-test techsupport_agent.py --list-tools

# Test customer identification
swaig-test techsupport_agent.py --exec identify_customer \
  --identifier "john@example.com"

# Test ticket creation
swaig-test techsupport_agent.py --exec create_ticket \
  --priority "high"

# Build Docker image
docker build -t techsupport:latest .

# Run container
docker run -p 3000:3000 --env-file .env techsupport:latest

# Test health endpoint
curl http://localhost:3000/health
```

---

## Submission Instructions

1. Implement your solution in `solution/techsupport_agent.py`
2. Create deployment files (Dockerfile, requirements.txt, .env.example)
3. Add your demo recording (wav, mp3, or mp4) to the repository
4. Push to trigger auto-grading
5. Check the "Grading Results" issue for automated feedback

**Note:** After automated checks pass, your submission will be tagged for manual review by an instructor.

---

## Time Management Suggestions

| Task | Suggested Time |
|------|---------------|
| Part 1: Agent Structure | 20 minutes |
| Part 2: Customer ID | 30 minutes |
| Part 3: Contexts | 45 minutes |
| Part 4: Functions | 45 minutes |
| Part 5: Recording | 15 minutes |
| Part 6: Deployment | 15 minutes |
| Testing & Debug | 30 minutes |

Good luck!
