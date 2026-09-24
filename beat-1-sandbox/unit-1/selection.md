# Assignment 1: Issue Selection

## Current status

This write-up is still in progress. My skill files are in
`tools/issue-select/`. The rubric there is a copy of the installed rubric
that I used for my last targeted test.

The full evaluation is blocked by my Claude account's spending limit.
I do not have a completed full-run score yet. I also need to confirm my
class's Path Review repository before making my final issue choice.

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

Pending: confirm the class repository and choose a live issue from it.
The saved evaluation examples are practice cases, not my final selection.

## Issue analysis

Pending the live issue and its current evidence. I need to record what
the issue asks for, the expected result, recent project activity, the
contribution rules, and any current work on the issue. I will use those
facts to explain each check.

## Why I chose this issue

Pending the issue choice and my fit profile. I need to explain why this
work fits my experience, what I want to learn, and why I prefer it over
the other issues I considered.

## Verdict output

Pending the skill's run on the selected live issue. There is no verdict
to paste yet. The four accept/reject labels from my targeted evaluation
are not the full verdict for a selected issue.
