# Using Claude Code to finish "When Attention Becomes Thought"

*Written 2026-04-22. A phased walkthrough for doing the repo setup, GitHub push, Pages deploy, and nightly writing sessions from Claude Code.*

Claude Code is a command-line tool from Anthropic that runs Claude inside your terminal with direct access to your file system, shell, and editor. You point it at a folder, type what you want done, and it does it, asking permission before running anything destructive. Everything below is phrased as prompts you paste into Claude Code in sequence.

## 0. Install Claude Code (one time)

If you do not already have it installed:

1. Install Node.js 18+ if you do not have it.
2. Install Claude Code: `npm install -g @anthropic-ai/claude-code`
3. In your terminal, run `claude` and follow the login prompt.

If any of those steps have changed since this was written, the authoritative setup guide is at `docs.claude.com/en/docs/claude-code`.

## 1. Launch Claude Code in the book folder

Open your terminal. Change into the book folder. The folder path has a space in it, so quote it:

```bash
cd "/Users/cillianwhittecar/Desktop/When attention becomes thought /When attention becomes thought"
claude
```

You should now see the Claude Code prompt. Every step below is something you paste at that prompt.

When Claude Code asks for permission to run a command, read it and approve. You can also type `/permissions` to pre-approve categories (for example "any git command") if you want fewer interruptions.

## 2. First prompt: initialize the repo

Paste this. Replace `YOUR-GITHUB-USERNAME` with your actual GitHub username before sending.

```
Do all of the following, confirming each step before moving on:

1. Show me `git status` to confirm this folder is not already a repo.
2. Run `git init` with the default branch set to `main`.
3. Do a project-wide find-and-replace of `REPLACE-ME` with `YOUR-GITHUB-USERNAME`. Only touch `book.toml` and `README.md`. Show me the diff before committing.
4. Run `git add .` and show me what will be staged.
5. Do `git commit -m "Initial import: scaffold and Chapters 1-2"`.
```

Expected result: a committed local repo with your GitHub username baked into `book.toml` and `README.md`.

## 3. Second prompt: create the GitHub repo and push

Two paths depending on whether you have the GitHub CLI (`gh`) installed. Claude Code will detect which applies.

```
Check whether `gh` (GitHub CLI) is installed and authenticated.

If yes:
- Use `gh repo create when-attention-becomes-thought --public --source=. --remote=origin --push` to create the repo and push.
- After push, run `gh repo view --web` so I can see the repo in my browser.

If no:
- Tell me how to install `gh` on macOS (via brew) and authenticate (`gh auth login`).
- Stop and wait for me to confirm I have done that before running the commands above.
```

Expected result: a public GitHub repo named `when-attention-becomes-thought` with your commit pushed.

## 4. Third prompt: enable GitHub Pages from Actions

```
Enable GitHub Pages for this repo, sourced from GitHub Actions (not from a branch). Use `gh` if it supports this; otherwise open the repo Settings page in my browser and tell me exactly which checkboxes to click.

Then:
- Trigger the `deploy.yml` workflow by running `gh workflow run deploy.yml` (or by pushing an empty commit if that does not work).
- Show me the workflow status with `gh run watch` so I can see it build.
- When it succeeds, print the live book URL.
```

Expected result: the book is live at `https://YOUR-GITHUB-USERNAME.github.io/when-attention-becomes-thought/` within a few minutes.

## 5. Fourth prompt: install mdBook locally so you can preview while writing

```
Install mdBook on this machine so I can preview the book locally as I write.

Preferred path: if Rust is installed, `cargo install mdbook`.

If Rust is not installed and I do not want to install it, download the prebuilt mdBook binary for my platform from the mdBook GitHub releases page and put it somewhere on my PATH. Verify with `mdbook --version`.

Then start a preview server with `mdbook serve --open` so I can see the current book in my browser. Leave it running.
```

Expected result: a live local preview at `http://localhost:3000` that auto-reloads when you save a chapter.

## 6. Ongoing: reading nights

For a reading night, you do not really need Claude Code in the loop. You read the paper, open `notes/ch0X-...md`, copy the template block, and fill it in. But Claude Code can help if you want:

```
I just read {Vaswani et al. 2017, Attention Is All You Need}. Ask me the seven questions from notes/TEMPLATE.md one at a time. Transcribe my answers into notes/ch03-scaling-era.md under a new entry for that paper, preserving the template structure exactly.
```

That turns a reading night into a conversation instead of a blank page.

## 7. Ongoing: writing nights

When you are ready to draft a chapter from your notes, a good prompt is:

```
Open notes/ch03-scaling-era.md. This is my raw reading notes for Chapter 3.

Before any writing: summarize back to me, in 5 bullets, what you think the throughline of this chapter should be. Wait for me to confirm or correct before drafting.

Once I confirm, draft the chapter at src/ch03-the-scaling-era.md in the voice established in src/ch01-introduction.md and src/ch02-the-spark.md. Rules:
- No em dashes, ever.
- Introduce every technical term before using it.
- Cite every empirical claim to a paper that appears in my notes. Do not invent sources.
- Target 2500-3500 words.
- End with a "What to watch" subsection for future updates.
- Preserve the "Last updated: YYYY-MM-DD" line at the top; update the date to today.

Show me the diff. Do not push.
```

Important: treat Claude Code's draft as a starting point, not the finished chapter. Read it aloud. Cut what does not sound like you. The voice is yours. The research assistance is the value.

## 8. Ongoing: publishing a chapter

When a chapter is ready to go live:

```
I want to publish the current Chapter 3 draft.

1. Show me a diff of the staged and unstaged changes.
2. Add an entry to CHANGELOG.md and src/changelog.md summarizing what changed in the new Chapter 3. Use today's date.
3. Commit with message "Chapter 3: The Scaling Era (initial draft)".
4. Push.
5. Watch the Pages deploy workflow and print the live URL when it completes.
```

Then draft a LinkedIn post from the chapter (see below).

## 9. LinkedIn amplification

```
Draft a LinkedIn post based on src/ch03-the-scaling-era.md. Constraints:
- 250-350 words.
- Starts with a specific, concrete hook. No "I am excited to announce" openings.
- One pull quote from the chapter.
- Ends with a link to the chapter at https://YOUR-GITHUB-USERNAME.github.io/when-attention-becomes-thought/ch03-the-scaling-era.html.
- No em dashes.
- Voice should match src/ch01-introduction.md.

Save it to a new file, `social/2026-XX-XX-chapter-3-linkedin.md`.
```

Keep all LinkedIn drafts in a `social/` folder. That folder can be gitignored or committed, your call.

## 10. Habit: one-prompt weekly checkup

Run this at the end of each week to keep yourself honest:

```
Give me a status report on this book:
- Which chapters have real prose vs. scaffolding? (check the bottom of the file; scaffolds start with a status banner.)
- What is in the reading notes that has not yet made it into a chapter?
- Which chapter is currently the longest pole in the tent?
- Based on the cadence of my commits (use `git log --since="30 days ago" --oneline`), am I on track for my target completion date? My target: [set this yourself, e.g., "first full draft by 2026-08-31"].

Keep the report to 300 words.
```

## Troubleshooting

**"Claude Code is running a command I did not expect."** You can always interrupt with Ctrl-C and ask it to explain before continuing. You can also start a session with `claude --resume` to pick up where you left off if a session gets messy.

**"The GitHub Pages URL shows a 404 for five minutes."** First deploys can take a while. Check `gh run list` to confirm the workflow succeeded. If the workflow succeeded but the URL still 404s after ten minutes, you may need to visit the repo Settings, Pages section, and manually select "GitHub Actions" as the source.

**"mdBook build fails with an unknown error."** The most common cause is a stray reference in `src/SUMMARY.md` to a file that does not exist. Claude Code can diagnose: paste the error and say "figure out what mdBook is complaining about and fix it."

**"I accidentally committed a big PDF from `papers/`."** Paste the error or filename into Claude Code and say "the papers folder should be gitignored; remove the PDF from git history and confirm it is ignored going forward." It will use `git rm --cached` and may recommend `git filter-repo` if the PDF is deep in history.

## A note on staying in control

Claude Code is a tool, not a collaborator. For this project in particular, the value is in *your* reading and *your* voice. Use Claude Code for:

- Repo plumbing (setup, git, deploys).
- Transcribing your spoken or typed notes into the right files.
- Generating first drafts you then rewrite.
- Diffing and reviewing your own drafts.

Do not use Claude Code to:

- Read the papers for you.
- Make the voice calls.
- Decide what you think about the AGI argument.

That part is yours.
