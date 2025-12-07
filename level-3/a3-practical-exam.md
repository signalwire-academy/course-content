---
layout: default
title: "Level 3 Practical Exam: Certified Voice AI Architect"
parent: "Level 3: Advanced"
nav_order: 99
---

**Time Allowed:** 4 hours
**Passing Criteria:** Score 80+ points across all categories

---

## Exam Overview

Design and implement a production-ready enterprise voice AI system demonstrating mastery of all architect-level concepts.

---

## Scenario: TeleHealth Connect

You are architecting a telehealth voice AI system that:

- Triages patient symptoms
- Schedules appointments with specialists
- Provides medication reminders
- Handles prescription refill requests
- Routes to on-call nurses for urgent issues

### Compliance Requirements

- HIPAA-compliant data handling
- No PHI in logs
- Recording consent required
- Identity verification before PHI access

---

## Part 1: Architecture Design (20 points)

### Deliverables

Create `architecture/` directory with:

**1. `overview.md`** - System overview including:

- High-level architecture description
- List of agents and responsibilities
- Integration points
- Data flow description

**2. `diagram.md`** - ASCII or described system diagram showing:

- Agent relationships
- Data flow
- External integrations
- Security boundaries

**3. `adr/001-agent-structure.md`** - ADR for agent organization
**4. `adr/002-hipaa-compliance.md`** - ADR for HIPAA approach
**5. `adr/003-knowledge-strategy.md`** - ADR for knowledge base design

### Evaluation Criteria

- [ ] Clear separation of concerns (4 points)
- [ ] Security boundaries defined (4 points)
- [ ] Scalability considered (4 points)
- [ ] ADRs explain rationale (4 points)
- [ ] Diagram accurate and complete (4 points)

---

## Part 2: Gateway Agent (15 points)

### Requirements

Create `agents/gateway_agent.py`:

- Route to appropriate department
- Handle after-hours routing
- Provide general information
- Implement health check

### Required Functions

1. `route_call(department)` - Route to specialist
2. `get_hours()` - Return operating hours
3. `emergency_guidance()` - Provide emergency info

### Evaluation Criteria

- [ ] Clean routing logic (5 points)
- [ ] After-hours handling (3 points)
- [ ] Emergency handling (3 points)
- [ ] Health endpoint (2 points)
- [ ] Proper authentication (2 points)

---

## Part 3: Patient Services Agent (25 points)

### Requirements

Create `agents/patient_agent.py`:

- Multi-step patient verification
- Symptom triage workflow (contexts)
- Appointment scheduling (DataMap)
- Prescription refills
- Secure data handling

### Required Contexts

1. **Verification** - Verify patient identity
2. **Triage** - Assess symptoms
3. **Scheduling** - Book appointments
4. **Prescriptions** - Handle refills

### Required Functions

**Verification:**

- `verify_patient(dob, member_id)` - Verify identity (secure)

**Triage:**

- `assess_symptoms(symptoms)` - Initial assessment
- `escalate_urgent()` - Route to nurse

**Scheduling:**

- `check_availability(specialty, date)` - DataMap to scheduling API
- `book_appointment(slot_id)` - Confirm booking

**Prescriptions:**

- `request_refill(medication, pharmacy)` - Submit refill request

### Evaluation Criteria

- [ ] Verification before PHI access (5 points)
- [ ] Context workflow correct (5 points)
- [ ] DataMap integration working (5 points)
- [ ] Recording paused for sensitive data (3 points)
- [ ] Proper error handling (3 points)
- [ ] Security logging (4 points)

---

## Part 4: Knowledge Integration (10 points)

### Requirements

Create knowledge base for:

- Common symptoms and guidance
- Medication information
- Provider directory
- FAQ

### Deliverables

1. `knowledge/symptoms.md` - Symptom guidance
2. `knowledge/medications.md` - Medication info
3. Knowledge integration in patient agent

### Evaluation Criteria

- [ ] Relevant content created (3 points)
- [ ] Search skill configured (3 points)
- [ ] Appropriate use in functions (2 points)
- [ ] Fallback for unknown queries (2 points)

---

## Part 5: Observability (15 points)

### Requirements

Create `shared/` directory with:

**1. `logging_config.py`** - Structured JSON logging

- Call ID correlation
- Function timing
- PHI exclusion

**2. `metrics.py`** - Prometheus metrics

- Call counters
- Function latency histograms
- Business metrics (appointments, refills)

**3. `config/alerts.yml`** - Alert rules

- Error rate alert
- Latency alert
- Business metric alerts

### Evaluation Criteria

- [ ] JSON structured logs (3 points)
- [ ] Correlation IDs (2 points)
- [ ] PHI excluded from logs (3 points)
- [ ] Relevant metrics defined (3 points)
- [ ] Appropriate alert thresholds (2 points)
- [ ] Health check comprehensive (2 points)

---

## Part 6: Deployment (10 points)

### Requirements

Create `deployment/` directory with:

**1. `Dockerfile`**

- Multi-stage build
- Non-root user
- Health check

**2. `docker-compose.yml`**

- All agents
- Environment configuration
- Health checks

**3. `.env.example`**

- All required variables
- Comments explaining each

### Evaluation Criteria

- [ ] Dockerfile follows best practices (3 points)
- [ ] Health checks configured (2 points)
- [ ] Environment properly managed (2 points)
- [ ] Compose orchestrates correctly (2 points)
- [ ] Documentation accurate (1 point)

---

## Part 7: Testing & Documentation (5 points)

### Requirements

**1. `tests/test_verification.py`** - Test patient verification

**2. `README.md`**

- Setup instructions
- Architecture overview
- API documentation

### Evaluation Criteria

- [ ] Tests cover critical paths (2 points)
- [ ] README complete (2 points)
- [ ] Setup instructions work (1 point)

---

## Submission Structure

```diagram
telehealth/
├── architecture/
│   ├── overview.md
│   ├── diagram.md
│   └── adr/
│       ├── 001-agent-structure.md
│       ├── 002-hipaa-compliance.md
│       └── 003-knowledge-strategy.md
├── agents/
│   ├── gateway_agent.py
│   └── patient_agent.py
├── knowledge/
│   ├── symptoms.md
│   └── medications.md
├── shared/
│   ├── logging_config.py
│   └── metrics.py
├── config/
│   └── alerts.yml
├── deployment/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── .env.example
├── tests/
│   └── test_verification.py
└── README.md
```

---

## Scoring Summary

| Category | Points |
|----------|--------|
| Architecture Design | 20 |
| Gateway Agent | 15 |
| Patient Services Agent | 25 |
| Knowledge Integration | 10 |
| Observability | 15 |
| Deployment | 10 |
| Testing & Documentation | 5 |
| **Total** | **100** |

**Passing Score: 80 points**

---

## Testing Commands

```bash
# Test gateway agent
swaig-test agents/gateway_agent.py --dump-swml
swaig-test agents/gateway_agent.py --exec route_call --department "triage"

# Test patient agent
swaig-test agents/patient_agent.py --list-tools
swaig-test agents/patient_agent.py --exec verify_patient \
  --dob "1980-01-15" --member_id "M123456"

# Build Docker
docker build -t telehealth:latest -f deployment/Dockerfile .

# Run with compose
docker-compose -f deployment/docker-compose.yml up

# Check health
curl http://localhost:3000/health

# Check metrics
curl http://localhost:9090/metrics
```

---

## Time Management

| Phase | Suggested Time |
|-------|---------------|
| Architecture & Design | 45 min |
| Gateway Agent | 30 min |
| Patient Agent | 75 min |
| Knowledge Base | 30 min |
| Observability | 45 min |
| Deployment | 30 min |
| Testing & Docs | 15 min |
| Review & Polish | 30 min |

---

## Important Notes

1. **HIPAA Compliance**: All PHI handling must follow secure patterns
2. **Code Quality**: Clean, documented, production-ready code expected
3. **Testing**: Verify all functions work before submission
4. **Documentation**: Architecture decisions must be justified

---

## Submission

1. Compress complete directory as `level3_exam_[name].zip`
2. Include all required files
3. Verify all code runs without errors
4. Submit via course portal

Good luck! This exam demonstrates your readiness to architect enterprise voice AI systems.
