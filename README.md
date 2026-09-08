# brendanmccarthyactor.com

Static site. No build step, no framework, no tracking, no dependencies.
Built on the COLMAC hub's own site template, so it matches what the hub produces.

## Layout

- **Header** — name left; union, management and email right
- **Reel** — empty, waiting for a link or file
- **Work** — 32 posters. Click one and a viewer opens with a clip if there is one
  on file, the key art if there is not. Escape or BACK returns you to the page.
- **Short films** — empty, one click straight to YouTube
- **Writing** — empty
- **Photographs** — 3 headshots

## Deploy

Push to `main`, then **Settings → Pages → Deploy from a branch → main → / (root)**.

## Adding a clip to a project

Drop the video in `media/` and set its `clip` in the `WORK` array near the bottom
of `index.html`:

```js
{"t":"Shooter", ... ,"clip":"media/shooter_clip.mp4"}
```

Any project with a `clip` plays it in the viewer instead of showing the poster.
The hub can export these for you — Reel Room carves clips from a master and scopes
them to a credit.

## Adding the reel

Under `Reel`, either a YouTube link or:

```html
<figure class="well solo"><video src="media/reel.mp4" controls playsinline></video></figure>
```

## Adding a short film

```html
<a class="film" href="https://youtu.be/YOUR_ID" target="_blank" rel="noopener">
  <b>Title</b><span>Role &middot; Year &middot; one line</span>
  <em>Watch on YouTube &rarr;</em></a>
```

## The email

`hello@brendanmccarthyactor.com` is linked but **the mailbox does not exist yet.**
Set it up with your domain registrar or a mail host before you publish, or the
address bounces.

## Not here, deliberately

**No resume PDF.** A resume carries a phone number and an address, and the work
speaks through the clips instead. This is a showcase, not a career document.

No audition history, no casting offices, no rep contact beyond the agency name.
Everything operational stays in the hub.
