# brendanmccarthyactor.com

Actor site. Static HTML, no build step, no framework, no tracking.

## What is here

- 32 credits with artwork, split television and film
- 3 headshots
- Resume PDF
- Empty sections ready for the reel, short films, writing and contact

## Deploy

**GitHub Pages** — push to `main`, then Settings → Pages → Deploy from a branch →
main → / (root).

**Anything else** — it is a folder of static files. Drag it anywhere.

## Adding a short film

In `index.html`, find `<section id="films">` and add one of these per film:

```html
<a class="film" href="https://youtu.be/YOUR_ID" target="_blank" rel="noopener">
  <h3>Title</h3>
  <p>Role · Year · one line about it</p>
  <div class="go">WATCH ON YOUTUBE &rarr;</div>
</a>
```

## Adding a reel

Same pattern under `<section id="reel">`, or paste a YouTube/Vimeo embed.

## Removing a credit

Delete its `<article class="credit">` block. The poster file in `media/` can go too.

## What is deliberately not here

No phone number, no audition history, no casting office notes, no rep contact
details beyond the agency name. This is the public face; everything operational
lives elsewhere.
