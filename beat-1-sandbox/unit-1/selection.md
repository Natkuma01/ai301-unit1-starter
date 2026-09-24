# Assignment 1: Issue Selection

## Current status

I selected [issue #69: Output parser crashes on a top-level JSON array fallback](https://github.com/codepath/pathreview-ai301-fa26-s1/issues/69)
in my class's Path Review repository. My skill files are in
`tools/issue-select/`. The rubric there is a copy of the installed rubric
that I used for my last targeted test. My scope file now includes my
class repository and my coding experience.

The full evaluation is blocked by my Claude account's spending limit.
I do not have a completed full-run score yet. The live issue review below
was done with Codex following my skill and rubric. It is separate from
the required full evaluation with Sonnet.

## Run history

These are the runs I can account for. I did not save the exact dates or
the total number of earlier attempts, so I have not guessed them here.

| Run | What I ran | Result | What I learned |
|---|---|---|---|
| Earlier targeted run | `--only issue-09,issue-12,issue-19,issue-20` with my installed rubric | I recorded four matching results: issue-09 accept, issue-12 reject, issue-19 accept, and issue-20 reject. The original output is not saved in this repository. | These four examples matched, but this was not a full evaluation. |
| Earlier full run | All 20 issues with `--save-run` | All 20 returned `ERROR (claude exited 1:)`. | There was no usable score or saved transcript. |
| Earlier full run with one worker | All 20 issues with `--workers 1` | The same failure continued. | Running one issue at a time did not solve it. |
| Full run during debugging | All 20 issues with `--save-run eval-run.txt` | All 20 returned the same empty error. A separate check in the restricted environment showed a login error. | The script was hiding messages that Claude sent through its normal output. |
| Full run after fixing error messages | All 20 issues with `--save-run eval-run.txt`, with access to the existing Claude login | All 20 reported that my individual spending limit had been reached. | The account limit must be resolved before I can finish the evaluation. The script correctly did not save an incomplete run. |
| Latest account check | A short Sonnet request before preparing this submission | Claude still reported the spending limit. | The final full evaluation is still pending. |
| Live issue review, September 23, 2026 (New York time) | Codex followed `tools/issue-select/SKILL.md`, `scope.md`, and `rubric.md` for Path Review issue #69 using current GitHub evidence. | Accept. All five required checks and the preferred human-activity check passed. The JSON is included below. | The issue fits my Python experience and gives me a small way to work on an AI application. This is not a Sonnet evaluation run. |

The targeted run used this command:

```sh
python3 eval/run_eval.py --rubric ~/.claude/skills/issue-select/rubric.md --only issue-09,issue-12,issue-19,issue-20
```

After credit is available, the final run should use the submitted files
and save the result in the required folder:

```sh
python3 eval/run_eval.py --rubric tools/issue-select/rubric.md --skill tools/issue-select/SKILL.md --save-run beat-1-sandbox/unit-1/eval-run.txt
```

The script must create `eval-run.txt`. I will not type or edit that file
by hand. A passing run needs at least 18 matches out of 20 and at least
one match in every category.

## Why I use these checks

These quotes come from my submitted rubric. They explain what each
check is meant to do.

### Is the project still in use?

> Fail if the repository is archived. Otherwise pass if either the last push or latest release was within 30 days of the capture date.

I want to spend time on a project that is still being used and updated.
A recent update gives me some evidence of activity. For the saved test
issues, I measure the 30 days from the date in the example, not from today.
For a live issue, I use the date when I check it.

### Does the project allow this kind of contribution?

> Pass if AI use is allowed or no policy prohibiting it is stated.

This course uses AI tools. I need to read the project's rules before
starting. If a project does not allow this kind of work, I should choose
another issue. If it asks me to explain, review, or test AI-assisted work,
I still need to follow those rules.

### Is the work small enough to understand?

> Multiple implementation steps, possible causes, or suggested approaches do not by themselves make an issue too large when they address the same outcome.

I want one clear result. A small change can still need several steps.
I do not want to reject it only because the description has a long list.
However, a list of separate features or a major redesign is too much for
a first contribution.

### Is someone already doing the work?

> Old expressions of interest or closed/abandoned PRs do not fail by themselves when there is no current owner.

An old comment does not always mean someone is still working on the issue.
I look for current ownership and open pull requests too. In the class's
Path Review repository, the course rule says other students' claim
comments do not block me from choosing the same issue.

### Does the change affect security?

> Do not fail UI, layout, text, or styling changes merely because they appear on authentication-related screens.

Changing how a login page looks is different from changing who can log
in or what they can access. I want to avoid changes to passwords, identity,
or access rules for my first contribution. A small visual change may
still be suitable.

### Are people maintaining the project?

> Pass if there is recent human maintainer or contributor activity. Otherwise grade unclear.

Human activity is a useful sign that someone may review the work. This
is a preferred check, so it helps me compare accepted issues. It does not
reject an issue by itself.

## Trade-offs

My rubric allows an issue to pass when a required check is unclear, as
long as no required check fails. This avoids rejecting an issue just
because some information is missing. The risk is that I could start work
before finding an important problem. I need to read the unclear results
and check them before I begin.

A recent push does not prove that someone will review my contribution.
The project could have recent automated updates but little human activity.
This is why I also look at human comments and commits.

The human-activity check says "recent" without giving a number of days.
That leaves room for different answers. I have kept the current rubric
unchanged for this evaluation, but this is a limitation I should revisit.

The rubric also rejects issues opened by automated accounts. This is
simple to apply, but it could reject a useful issue that a person has
already reviewed. The author alone does not tell me how difficult or
useful the work is.

## Issue link

**Selected issue:** [#69 — Output parser crashes on a top-level JSON array fallback](https://github.com/codepath/pathreview-ai301-fa26-s1/issues/69)

**Repository:** [codepath/pathreview-ai301-fa26-s1](https://github.com/codepath/pathreview-ai301-fa26-s1)

I checked the live issue on September 23, 2026, New York time
(September 24 in UTC). This is my selection, not a claim comment or a
completed fix.

## Issue analysis

The app reads feedback returned by an AI model. It can read a JSON object,
but a JSON list makes it crash. For example, a response containing
`["First feedback item", "Second feedback item"]` reaches code that calls
`.items()`. That works on a Python dictionary, but not on a list.

The issue describes the error as:

> AttributeError: 'list' object has no attribute 'items'

The expected result is simple: the app should handle a list response
without crashing. The change is focused on
[`rag/generator/output_parser.py`](https://github.com/codepath/pathreview-ai301-fa26-s1/blob/f89c06fc3ff292df2a04a39ac51319d32a76b779/rag/generator/output_parser.py)
and its
[tests](https://github.com/codepath/pathreview-ai301-fa26-s1/blob/f89c06fc3ff292df2a04a39ac51319d32a76b779/tests/unit/test_output_parser.py).
The code still calls `data.items()` without first handling a list.
The existing `test_json_array_fallback` is marked as an expected failure
for issue #69. The issue says to remove that marker when the fix works.

Another student has posted a reproduction report in the issue comments.
That supports the bug report, but I have not run the reproduction myself.
My analysis here is based on reading the issue, its comments, the current
code, and the test.

| Check | Result | Evidence and reason |
|---|---|---|
| `repo_in_use` | Pass | The repository is not archived. Its last push was September 16, 2026, within 30 days of this review. No releases were listed, but a recent push is enough under my rule. |
| `contribution_policy` | Pass | I read the contribution guide and pull request template. Neither states a ban on AI-assisted work. The guide requires tests and project checks to pass. |
| `scope_fit` | Pass | This is one clear crash with two named files and an existing test. The issue estimates 2–4 hours. It does not ask for a redesign. |
| `issue_available` | Pass | The issue was opened by Aburke225, a User account, and has no assignee. I found no open fix pull request for #69. Another student's claim and reproduction comments do not block it under the Path Review class rule. |
| `security_sensitive` | Pass | The requested change handles the shape of AI feedback. It does not change login, passwords, identity, or access rules. |
| `active_maintainer` (preferred) | Pass | Three of the five latest main-branch commits were made by Andrew Burke on September 16, 2026. This shows recent human activity. |

All required checks pass, so the verdict is **accept**.

I checked the [repository details](https://api.github.com/repos/codepath/pathreview-ai301-fa26-s1),
[five latest commits](https://api.github.com/repos/codepath/pathreview-ai301-fa26-s1/commits?per_page=5),
[issue history](https://github.com/codepath/pathreview-ai301-fa26-s1/issues/69),
and [open pull requests](https://github.com/codepath/pathreview-ai301-fa26-s1/pulls).
The only open pull request returned at the time was #74 for issue #60,
which is a different bug. The issue history also linked a closed coursework
submission, not an open fix for #69.
The [contribution guide](https://github.com/codepath/pathreview-ai301-fa26-s1/blob/f89c06fc3ff292df2a04a39ac51319d32a76b779/docs/CONTRIBUTING.md)
and [pull request template](https://github.com/codepath/pathreview-ai301-fa26-s1/blob/f89c06fc3ff292df2a04a39ac51319d32a76b779/.github/PULL_REQUEST_TEMPLATE.md)
explain the checks needed for a future contribution.

## Why I chose this issue

I have intermediate experience with Python and JavaScript. I have built
full-stack projects using React and Django, and I am comfortable with
APIs, databases, Git, and basic cloud tools. This issue lets me use my
Python experience while learning how to contribute to a larger project.

I chose #69 because the problem is clear and there is already a test to
start from. It also helps me understand a real problem in AI applications:
the model may return a different format than the code expects. I can use
AI tools to help explain the code and suggest test cases, then review
the suggestions and check the results myself.

I also looked at [#71](https://github.com/codepath/pathreview-ai301-fa26-s1/issues/71),
which fixes indentation in a Markdown test, and
[#68](https://github.com/codepath/pathreview-ai301-fa26-s1/issues/68),
which handles an empty keyword-search index. Both descriptions are focused.
I prefer #69 because it gives me practice with both application code and
tests, and it connects directly to handling AI responses. This comparison
is about fit; I did not run a full rubric review on those two alternatives.

There are trade-offs with #69. It is a small task, so it will not teach me
the whole system. The current test only checks that the result is a list;
that alone does not prove useful feedback was kept. When I work on the fix,
I should check the contents too and make sure normal JSON objects and plain
text still work. The issue allows more than one way to handle a list, so
I need to choose an approach that matches the existing code and explain it.

Another student is also interested in this issue. The class allows shared
issues, but I should still check the latest comments before starting.
I plan to make a focused change and test it before preparing a pull request.

## Verdict output

This is the live-issue verdict produced by Codex following my submitted
skill, scope, and unchanged rubric. It is not output from the Claude CLI
or a replacement for the 20-issue evaluation.

```json
{
  "item": "https://github.com/codepath/pathreview-ai301-fa26-s1/issues/69",
  "checks": [
    {
      "name": "repo_in_use",
      "grade": "pass",
      "evidence": "Checked September 24, 2026 UTC: repository is not archived; last push was September 16, 2026, within 30 days; no releases listed."
    },
    {
      "name": "contribution_policy",
      "grade": "pass",
      "evidence": "docs/CONTRIBUTING.md and .github/PULL_REQUEST_TEMPLATE.md require tests and project checks; neither states an AI contribution ban."
    },
    {
      "name": "scope_fit",
      "grade": "pass",
      "evidence": "Issue #69 asks for one JSON-list crash fix in output_parser.py and its tests, with an existing expected-failure test and a 2–4 hour estimate."
    },
    {
      "name": "issue_available",
      "grade": "pass",
      "evidence": "Opened by User account Aburke225; no assignee or open fix PR found. Student claim comments are allowed under the Path Review scope rule."
    },
    {
      "name": "security_sensitive",
      "grade": "pass",
      "evidence": "The requested fix handles AI feedback lists and does not change authentication, authorization, identity, or credentials."
    },
    {
      "name": "active_maintainer",
      "grade": "pass",
      "evidence": "Three of the five latest main-branch commits were by Andrew Burke on September 16, 2026."
    }
  ],
  "verdict": "accept"
}
```
