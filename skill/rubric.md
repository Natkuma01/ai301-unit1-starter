# Rubric: is this a good first issue?

<!--
THIS IS THE PART YOU WRITE. The skill in SKILL.md executes whatever checks
you define here. It ships empty on purpose: the judgment is your work.

A filled rubric must contain:

1. At least one row in the checks table. Each row needs all four columns:
   - Check: a short name (used in the output JSON).
   - Evidence: exactly what to look at, and where. Name the source
     (repo-facts block, issue body, comment thread, or the locations in
     references/evidence-guide.md). "The repo" is not a source; "the last
     5 default-branch commit dates" is.
   - Pass condition: a condition someone else could apply and get your
     answer. Prefer thresholds with numbers ("a maintainer commented
     within 30 days") over adjectives ("maintainer is responsive").
   - Weight: `required` (a fail here rejects the issue) or `preferred`
     (never changes the verdict; a nice-to-have that helps rank the
     issues you accept).

2. A verdict rule below the table: how the check grades combine into
   accept or reject, including how `unclear` is treated. The verdict
   space is binary. If you write no rule for `unclear`, the skill treats
   it as fail.

Cover what actually kills first contributions. The lecture named four
families: the maintainer is alive, the repo is in use, the scope fits a
newcomer, and nobody else is already on it. A rubric that ignores a family
will fail eval issues designed around that family.
-->

## Checks

| Check | Evidence | Pass condition | Weight |
|---|---|---|---|
| active_maintainer | Last 5 default-branch commits under Repo facts, including commit author names; Comments section, including author_association | Pass if there is either a non-bot human commit or a comment from an Owner, Member, or Collaborator within 7 days of the capture date. Otherwise fail. | preferred |
| repo_in_use | Archived status, last push to any branch, and latest release under Repo facts | Fail if the repository is archived. Otherwise pass if either the last push or latest release was within 30 days of the capture date. If the release is within 30 days but the last push is older than 30 days, pass but clearly report both dates as a caution. Fail if neither occurred within 30 days. If the required dates are unavailable, grade unclear and explain what could not be verified. | required |
| scope_fit | Issue body and Comments section, including issue history and linked or mentioned closed, unmerged PR attempts | Pass when the issue asks for one bounded contribution, even if that contribution requires several implementation steps. Small bugs, documentation fixes, and UI fixes are acceptable. Fail for umbrella/tracking issues containing separate major work, several unrelated major features, major architecture redesigns, or stale issues with evidence of repeated abandoned attempts and no meaningful recent activity. If the feature is bounded but its design is still being discussed, grade unclear and explain the unsettled requirements. | required |
| security_sensitive | Issue body and Comments section describing the requested implementation | Fail if the contribution requires changes to authentication logic, authorization or access-control logic, roles, permissions, identity handling, or credential handling. Do not fail UI, layout, text, or styling changes merely because they appear on authentication-related screens. | required |
| issue_available | Assignees and linked PRs under Repo facts; Comments section for PR mentions, claim comments, maintainer responses, and dates | Fail if another contributor is currently assigned and has activity within 30 days, an active/open PR exists, or a maintainer has explicitly given the work to another contributor. A recent interest comment without maintainer approval, assignment, or an active PR does not fail by itself; grade unclear and report the claim. If an assignee remains but there has been no related activity for more than 30 days, grade unclear and report the stale assignment. Pass when there is no evidence that another contributor currently owns the issue. | required |

## Verdict rule

Accept if no required check fails. Reject if any required check fails.

An unclear required check does not automatically reject the issue. The issue
may still be accepted, but the summary must clearly identify what evidence
is unclear or missing so that the human can make the final decision.

Preferred checks never change the accept/reject verdict. They are used to
compare and rank issues that have already been accepted.

In the readable summary, make the status easy for the human to scan:
🟢 for a clear pass, 🔴 for a fail, and 🟡 for unclear evidence or an
important caution. The JSON output must still use only pass, fail, or
unclear for check grades and accept or reject for the final verdict.
