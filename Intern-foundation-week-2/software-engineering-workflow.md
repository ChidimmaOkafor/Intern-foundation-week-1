# Software Engineering Workflow

## Introduction

Software engineering is more than writing code. A complete software engineering workflow starts with understanding requirements and ends with delivering a tested solution that meets user needs. The workflow helps teams build reliable software in an organized way.

---

## 1. Requirements

A requirement is a description of what the software should do.

Requirements explain the problem that needs to be solved and the expected outcome.

### Example

A user should be able to reset their password if they forget it.

---

## 2. Tasks and Tickets

A requirement is usually broken into smaller pieces of work called tasks or tickets.

A ticket contains:

* Task description
* Priority
* Assignee
* Acceptance criteria
* Status

### Example Ticket

**Title:** Add Password Reset Feature

**Description:** Create functionality that allows users to reset forgotten passwords through email verification.

---

## 3. Acceptance Criteria

Acceptance criteria are conditions that must be met before a task is considered complete.

They help developers understand exactly what success looks like.

### Example Acceptance Criteria

* User can request a password reset.
* Reset link is sent to the user's email.
* User can create a new password.
* Invalid links display an error message.

---

## 4. Development

Development is the process of writing the code required to complete the ticket.

Developers should follow the ticket requirements and acceptance criteria instead of making assumptions.

### Why Development Should Follow the Ticket

* Prevents unnecessary features.
* Ensures requirements are met.
* Keeps work aligned with project goals.
* Makes progress easier to track.

---

## 5. Testing

Testing verifies that the software works correctly before it is reviewed or delivered.

### Types of Testing

* Manual testing
* Unit testing
* Integration testing

### Why Testing Is Required

* Finds bugs early.
* Improves software quality.
* Confirms acceptance criteria are satisfied.
* Reduces issues after release.

---

## 6. Code Review

Code review is the process of another developer examining the code before it is merged into the main project.

### Why Code Review Matters

* Detects bugs and mistakes.
* Improves code quality.
* Encourages knowledge sharing.
* Ensures coding standards are followed.

---

## 7. Deployment Awareness

Deployment is the process of making software available to users.

Developers should understand where and how their code will be released.

### Basic Deployment Process

1. Code is approved.
2. Code is merged.
3. Application is deployed.
4. Users receive the updated version.

---

## 8. Documentation

Documentation explains how the software works and how changes were made.

### Why Documentation Matters

* Helps future developers.
* Makes maintenance easier.
* Records important decisions.
* Supports users and team members.

Examples include:

* README files
* API documentation
* Setup instructions
* Release notes

---

## 9. Feedback and Iteration

Software development is an ongoing process.

After delivery, users and stakeholders provide feedback that may lead to improvements or new requirements.

### Why Feedback Is Important

* Identifies missing features.
* Improves user experience.
* Helps teams build better products.
* Supports continuous improvement.

---

# Example: Requirement to Delivery

## Requirement

Users should be able to mark tasks as completed in a To-Do application.

## Ticket

**Title:** Add Task Completion Feature

### Acceptance Criteria

* Users can mark a task as completed.
* Completed tasks display a visual indicator.
* Changes remain after page refresh.

## Development

A checkbox feature is added to each task.

## Testing

* Verify checkbox works.
* Verify completed tasks display correctly.
* Verify completion status is saved.

## Code Review

Another developer reviews the implementation and suggests improvements.

## Deployment

The feature is merged and released to users.

## Documentation

README is updated to explain task completion functionality.

## Feedback

Users request a filter to show only completed tasks, creating a new requirement for a future ticket.

---

# Conclusion

A software engineering task is not complete when code is written. A complete workflow includes requirements, tickets, acceptance criteria, development, testing, code review, deployment awareness, documentation, and feedback. Following this workflow helps teams build reliable and maintainable software.
 
