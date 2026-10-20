# Technical Knowledge — Agent SDLC Architecture and Workflow

## Topic record
**Topic:** architecture and delivery workflow for an agentic full-stack project. **Status:** documentary interpretation of research report §§8–13, **not** an approved architecture for a concrete application. **Research cut-off:** 2026-10-19. **Order adopted:** 2026-10-20.

## Problem and requirements
The documented problem is to select a professional order for 13 course modules while developing a new agentic application with Claude Code; see [original request](../../../raw/agent-sdlc-13-modulos/chat-1/turns/0001-user-original.md) §2. Specific product requirements do not exist in the preserved corpus. The **process-level** concerns include traceability, security, evaluations, deployment and observability when relevant; none is evidence of selected production software.

## Technical alternatives and dependencies
- Published **M1 through M13**: curriculum sequence for learning.
- Personally adopted route: **M1 → M3 → M6 → M4 → M2 → M5 → M13 → M7 → M8 → M9 → M10 → M11 → M12**.
- **M4** offers planning/value criteria; **M2** formalizes specifications; **M5** preserves architecture decisions; **M6/M13** introduce risks/security from early stages; **M7/M11** structure tests; **M8** addresses data persistence; **M9** is a main implementation entry point for backend/agent capability; **M10** addresses frontend; **M12** addresses delivery/infrastructure. Cross-cutting activities may run in parallel rather than as a rigid queue.
- Selected frontend technology, backend framework, DB, agent framework, cloud provider, and system architecture: **NOT_SELECTED**.

## Evidence
- **Primary source for this interpretation:** [full original report](../../../raw/agent-sdlc-13-modulos/chat-1/turns/0002-assistant-original.md) §§1,6–13.
- **Original question:** [user original](../../../raw/agent-sdlc-13-modulos/chat-1/turns/0001-user-original.md).
- **Externally cited references:** [source catalog](../evidence/sources.md). Listing an external reference in the ZIP does not independently check the linked content.

## Evaluation and future work
The route is an order of **priority and prerequisites**, not an immutable dependency chain. The report locates substantial agent implementation mostly in M9 once capabilities, boundaries, and evidence of verification are planned. A small disposable technical spike is permissible earlier when needed for critical uncertainty, but cannot be passed off as an operational product. Full-stack integration, security assurance, end-to-end tests, production observation, and maintenance remain future **activities**, not executed test results.

## Decisions and follow-up
**Adopted decision:** [DEC-0001.md](../decisions/DEC-0001.md). **Questions:** [questions.md](../questions.md). **Committed tasks:** none. New product-specific choices need evidence and owner consent, notwithstanding his authorization of the documentation package.
