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
| repo_in_use | Archived status, last push to any branch, and latest release under Repo facts | Fail if the repository is archived. Otherwise pass if either the last push or latest release was within 30 days of the capture date. If neither occurred within 30 days, fail. If the required dates are unavailable, grade unclear. | required |
| contribution_policy | Contribution policy under Repo facts, including CONTRIBUTING.md or other repository contribution guidance | Fail if the repository explicitly prohibits AI-generated code, AI-generated documentation, or the AI-assisted contribution workflow required for this course. Pass if AI use is allowed or no policy prohibiting it is stated. | required |
| scope_fit | Issue body and Comments section | Pass when the issue describes one bounded bug, feature, documentation change, or UI change with a clear outcome. Multiple implementation steps, possible causes, or suggested approaches do not by themselves make an issue too large when they address the same outcome. Fail for umbrella/tracking issues, multiple unrelated features, or major architectural redesigns. Issue age or an old abandoned attempt alone does not make a bounded issue out of scope. If requirements remain fundamentally unsettled, grade unclear. | required |
| issue_available | Assignees and linked PRs under Repo facts; issue author; Comments section for claim comments, maintainer responses, and dates | Fail if the issue was opened by a bot or automated account, another contributor is currently assigned and active, an active/open PR exists, or a maintainer has explicitly given the work to another contributor. Old expressions of interest or closed/abandoned PRs do not fail by themselves when there is no current owner. Pass when there is no evidence another contributor currently owns the issue. | required |
| security_sensitive | Issue body and Comments section describing the requested implementation | Fail if the contribution requires changes to authentication logic, authorization or access-control logic, roles, permissions, identity handling, or credential handling. Do not fail UI, layout, text, or styling changes merely because they appear on authentication-related screens. | required |
| active_maintainer | Last 5 default-branch commits under Repo facts and Comments section | Pass if there is recent human maintainer or contributor activity. Otherwise grade unclear. | preferred |

## Verdict rule

Accept if no required check fails. Reject if any required check fails.

An unclear required check does not automatically reject the issue. The issue may still be accepted, but the summary must clearly identify what evidence is unclear or missing so that the human can make the final decision.

Preferred checks never change the accept/reject verdict. They are used only to compare and rank issues that have already been accepted.

In the readable summary, make the status easy for the human to scan:
🟢 for a clear pass, 🔴 for a fail, and 🟡 for unclear evidence or an
important caution. The JSON output must still use only pass, fail, or
unclear for check grades and accept or reject for the final verdict.
