# Oahu Medical Group website

Source for **www.hawaiiinfectiousdisease.com**. A plain, static HTML site: no WordPress, no database, nothing to patch.

- `docs/` — the finished site that GitHub Pages serves. Don't hand-edit the HTML files here; they are regenerated.
- `src/pages.py` — the words on every page.
- `src/providers.py` — physician names, photos, bios, clinic hours and payment links.
- `docs/assets/site.css` — styles. `docs/assets/img/` — photos. `docs/forms/` — PDF forms.
- `build.py` — turns `src/` into `docs/`. Python 3, standard library only.

## Making a change

Ask Claude (in the Claude app with this repo attached, or in Claude Code), for example:

> Add Dr. X to the providers page with this bio and these clinic hours.
> Change the Friday afternoon hours for Dr. Majewski to 1–4 PM.
> Replace the new patient form PDF with the attached file.

Claude edits the file in `src/`, runs `python3 build.py`, and commits. GitHub Pages publishes the change within a minute or two.

To do it by hand: edit `src/pages.py` or `src/providers.py`, run `python3 build.py`, commit and push both `src/` and `docs/`.

## Things that live outside this repo

- **Domain name**: Squarespace Domains (domains.squarespace.com). Renews every February.
- **DNS**: currently at DreamHost; moves to point at GitHub Pages at launch (see below).
- **Appointment request form**: delivered by Formspree. The form ID is in `src/pages.py` (`FORMSPREE_ID`). Submissions go to the email address set in the Formspree account. The form deliberately collects no medical or insurance details.
- **Payment links**: CardPointe pages, one per physician entity, in `src/providers.py`.

## Launch checklist (DNS)

In DreamHost (or wherever DNS lives), set:

| Type  | Name | Value |
| ----- | ---- | ----- |
| A     | @    | 185.199.108.153 |
| A     | @    | 185.199.109.153 |
| A     | @    | 185.199.110.153 |
| A     | @    | 185.199.111.153 |
| CNAME | www  | ranmyaku81.github.io |

Then in the GitHub repo: Settings → Pages → Custom domain `www.hawaiiinfectiousdisease.com`, and tick "Enforce HTTPS" once the certificate is issued (usually under an hour). The `docs/CNAME` file is already in place.
