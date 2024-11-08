# Earth 616 Ontology Project: User Stories

Welcome to the shared repository for documenting user stories related to the Earth 616 Ontology project. This repository serves as a common space for collecting and organizing requirements through user stories, using a structured template inspired by the [Polifonia User Story Template](https://github.com/polifonia-project/stories). This README outlines the purpose, methodology, and process for contributing user stories.

## Purpose

User stories are crucial for capturing the needs and expectations of various stakeholders, guiding the development of the Earth 616 Ontology and associated software solutions. By documenting user stories, we ensure that the ontology and tools are aligned with real-world requirements, making them more useful and accessible to end-users.

### Two Primary Purposes of User Stories

1. **Knowledge Engineering (KE):**
   - Focuses on capturing the requirements for building and optimizing the knowledge graph, integrating it with large language models (LLMs), and ensuring the system meets the needs of knowledge engineers, data scientists, and related roles.
   - KE user stories emphasize the importance of data accuracy, integration, and context-aware responses, leveraging knowledge graphs to enhance AI performance.

2. **End-User Applications:**
   - Aimed at capturing requirements for applications that directly interact with end-users, such as mobile apps or web interfaces.
   - These stories often involve personas who use the ontology-driven applications in their daily tasks, such as analysts using mobile devices to capture supply chain documentation via OCR.

## Methodology

This user story collection methodology is inspired by the Polifonia Ontology Network's approach to requirements collection, as detailed in the paper "The Polifonia Ontology Network: Building a Semantic Backbone for Musical Heritage," particularly in section 3.1. The Polifonia methodology emphasizes structured and research-based user stories to gather requirements effectively and drive ontology development.

### Key Elements of the Methodology:

- **Persona-Centric:** User stories are centered around personas that represent typical users, providing insights into their roles, goals, and challenges.
- **Scenario-Driven:** Scenarios describe the interaction of personas with the system before, during, and after the implementation of features, capturing the practical impact of the system.
- **Competency Questions:** These are used to frame the specific needs and questions that the system must address, particularly in knowledge engineering contexts.
- **Privacy and Feedback:** User stories are classified by privacy level and feedback mechanisms to manage internal and external review processes appropriately.

## User Story Template

Each user story should be documented using the following template in Markdown:

```markdown
---
name: Story
about: Suggest a user story for the Earth 616 Ontology Project
title: ''
labels: ''
assignees: ''
---

## ID of the Story
Indicate the unique ID of the story.

## Work Packages (WPs)
List the work packages involved in this story.

## Pilots
Identify the pilots involved in this story, if applicable.

## Priority
Indicate the priority of the story:
- **Must have**
- **Life improver**
- **Life changer**
- **Breakthrough**

## Persona
- **Name**: Provide the name of the persona involved in this story.
- **Age**: Indicate the age of the persona.
- **Occupation**: Describe the occupation and primary role of the persona. If there are secondary roles, list them as well.
- **Relevant Characteristics**: Include relevant characteristics, such as skills, knowledge, and interests.

## Goal
- **Description**: Provide a short description of the persona’s goal(s) that need to be addressed in the story.
- **Keywords**: List up to 5 keywords that represent the goal of the persona.

## Scenario
Write a narrative describing how the persona's task/need/problem is solved before, during, and after interaction with the resource, software, or service being developed. 
- **Before Interaction**: Describe the persona's situation before using the system.
- **During Interaction**: Outline the steps or actions the persona takes while interacting with the system.
- **After Interaction**: Explain the outcomes or changes after using the system.

## Competency Questions (CQs)
- List the specific questions that the persona needs the resource, software, or service to answer in order to satisfy their task, need, or problem.

## Resources (Optional)
- List any resources, with references or links, where it is expected or known that the persona can find what they are looking for.

## Privacy Level
Indicate the privacy level of the story:
- **Private**: Internal to the project, for example, AI Engineer stories.
- **Public with HITL**: Requires human-in-the-loop feedback, such as stories involving DoD Data Analysts.

## Feedback Mechanism
Specify the feedback mechanism:
- **Internal Review**: Feedback will be collected internally within the project team.
- **External Review with HITL**: Feedback will involve external stakeholders and include HITL processes.
```

## How to Contribute

### 1. Create a New User Story Discussion

- Start by creating a new issue in the GitHub repository using the "Story" template. This will serve as the initial discussion space for your proposed user story.
- Label the issue appropriately (e.g., Knowledge Engineering, End-User Application) and provide initial details as per the template.

### 2. Engage in Discussion

- Use the GitHub issue to discuss the user story with other team members, stakeholders, and external reviewers if applicable.
- Gather feedback, refine the story details, and ensure that all relevant aspects of the user story are well-defined and agreed upon.

### 3. Finalize and Move to Stories Directory

- Once the user story is finalized through the GitHub issue discussion, create a Markdown file in the `stories` directory of the repository.
- Copy the finalized user story into the Markdown file, ensuring that all sections are filled out correctly.
- Submit a pull request to add the finalized story to the `stories` directory. Tag the relevant reviewers and ensure that the story is reviewed and approved.

### 4. Review and Feedback

- After the pull request is merged, continue to monitor the story for any updates or changes as the project evolves.
- Regularly update stories in the `stories` directory to reflect new insights, changes in requirements, or feedback from ongoing project development.

## Example User Stories

### Example 1: Knowledge Engineering

```markdown
---
name: Story
about: Suggest a user story for the Earth 616 Ontology Project
title: 'Improving Data Retrieval Accuracy for AI Engineer'
labels: 'Knowledge Engineering'
assignees: ''
---

## ID of the Story
KE-001

## Work Packages (WPs)
WP3, WP5

## Pilots
Ontology Alignment Pilot

## Priority
Must have

## Persona
- **Name**: Casey
- **Age**: 30
- **Occupation**: AI Engineer
- **Primary Role**: Responsible for improving LLM responses through better data integration.
- **Relevant Characteristics**: Expert in LLMs, focused on optimizing system performance and accuracy.

## Goal
- **Description**: As Casey, I want to integrate and fine-tune the knowledge graph with the LLM to enhance data retrieval accuracy, reducing the occurrence of irrelevant or incorrect responses.
- **Keywords**: LLM, knowledge graph, data retrieval, accuracy, optimization.

## Scenario
- **Before Interaction**: Casey manually adjusts parameters of the LLM based on trial and error, which is time-consuming and often yields inconsistent improvements.
- **During Interaction**: Casey integrates the knowledge graph into the LLM pipeline using GraphRAG, allowing the LLM to ground its responses in structured data. Casey monitors results through a feedback loop.
- **After Interaction**: The system now consistently provides more accurate and contextually relevant responses, significantly reducing manual adjustments.

## Competency Questions (CQs)
- (KE-001-CQ1) How can the knowledge graph be optimized to reduce irrelevant information during data retrieval?
- (KE-001-CQ2) What metrics can be used to validate the improvement in response accuracy?

## Resources (Optional)
- Knowledge Graph API documentation
- LLM integration guidelines

## Privacy Level
Private

## Feedback Mechanism
Internal Review by the AI Engineering Team
```

### Example 2: End-User Facing Application (Mobile Supply Chain Documentation for OCR)

```markdown
---
name: Story
about: Suggest a user story for the Earth 616 Ontology Project
title: 'Mobile Supply Chain Documentation for OCR'
labels: 'End User Application'
assignees: ''
---

## ID of the Story
APP-002

## Work Packages (WPs)
WP2, WP4

## Pilots
Supply Chain Documentation Pilot

## Priority
Must have

## Persona
- **Name**: Alex
- **Age**: 45
- **Occupation**: Receiving Personnel at Aerospace Component Facility
- **Primary Role**: Responsible for receiving, verifying, and documenting incoming aerospace components by scanning shipping labels and managing inventory records.
- **Relevant Characteristics**: Familiar with logistics and inventory systems, works under tight schedules, and needs tools that streamline data capture while ensuring security and accuracy.

## Goal
- **Description**: As Alex, I want to use a mobile app that captures data from shipping labels via OCR, so that I can quickly and accurately document received components into the inventory system without manual data entry, ensuring all parts are correctly logged and discrepancies are minimized.
- **Keywords**: mobile app, OCR, shipping labels, inventory, accuracy.

## Scenario
- **Before Interaction**: Alex receives shipments of aerospace components and manually enters data from shipping labels into an inventory system. This process is slow, prone to errors, and often causes delays in updating inventory records, leading to potential mismatches and audit issues.
- **During Interaction**: Alex uses a mobile app equipped with OCR technology to scan shipping labels directly at the receiving dock. The app automatically extracts data such as part numbers, quantities, supplier details, and shipment dates, and uploads it in real-time to the inventory management system. The app checks Alex's verifiable credentials to ensure authorized access before allowing data submission.
- **After Interaction**: The inventory system is immediately updated with the accurate details of the received components, reducing manual errors and processing time. Alex can quickly address any discrepancies flagged by the system, ensuring that inventory records are up-to-date and accurate for auditing and operational purposes.

## Competency Questions (CQs)
- (APP-002-CQ1) How can the system verify the end user’s credentials using verifiable credentials to ensure secure access to the application?
- (APP-002-CQ2) How does the application manage user permissions and ensure that only authorized personnel can perform specific actions, such as data submission or corrections?
- (APP-002-CQ3) How does the application interact with the KG to validate the authenticity of received components against known suppliers and parts in the supply chain?
- (APP-002-CQ4) How does the system ensure the integrity and accuracy of data captured from OCR scans, particularly in variable lighting or label conditions?
- (APP-002-CQ5) What feedback does the application provide to the user to confirm successful data capture and submission, and how is this feedback personalized based on user roles?

## Resources (Optional)
- OCR technology specifications for mobile devices
- Documentation on integrating verifiable credentials for mobile applications
- Inventory management system integration guides

## Privacy Level
Public with HITL

## Feedback Mechanism
External Review with HITL involving logistics supervisors, IT support staff, and security officers to ensure the secure handling of data and compliance with access protocols.
```
