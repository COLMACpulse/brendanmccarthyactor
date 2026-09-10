#!/usr/bin/env python3
"""
Run this before you push.

GitHub refuses any single file over 100MB, and Pages starts complaining
somewhere around a gigabyte. Both of those are easy to trip by dropping in a
camera export, and you find out when the push is rejected rather than when you
made the mistake. This tells you first.

    python3 check-media.py

It reads nothing but file sizes and the clip paths in index.html. It changes
nothing.
"""
import os, re, json, sys

HARD_FILE   = 100 * 1024 * 1024   # GitHub blocks the push above this
WARN_FILE   =  50 * 1024 * 1024   # GitHub warns above this
SITE_SOFT   = 1024 * 1024 * 1024  # Pages soft limit for a published site

HERE  = os.path.dirname(os.path.abspath(__file__))
MEDIA = os.path.join(HERE, 'media')
VIDEO = ('.mp4', '.mov', '.m4v', '.webm')


def mb(n):
    return '%.1f MB' % (n / 1048576.0)


def main():
    if not os.path.isdir(MEDIA):
        print('No media/ folder next to this script. Nothing to check.')
        return 0

    files, total = [], 0
    for root, _dirs, names in os.walk(HERE):
        if '.git' in root:
            continue
        for n in names:
            p = os.path.join(root, n)
            try:
                sz = os.path.getsize(p)
            except OSError:
                continue
            total += sz
            files.append((os.path.relpath(p, HERE), sz))

    blocked = [f for f in files if f[1] > HARD_FILE]
    heavy   = [f for f in files if WARN_FILE < f[1] <= HARD_FILE]
    vids    = sorted([f for f in files if f[0].lower().endswith(VIDEO)],
                     key=lambda x: -x[1])

    print('SITE TOTAL      %s' % mb(total))
    print('VIDEO FILES     %d, %s' % (len(vids), mb(sum(v[1] for v in vids))))
    print()

    ok = True

    if blocked:
        ok = False
        print('WILL BE REJECTED BY GITHUB  (over 100 MB each)')
        for f, s in blocked:
            print('   %-52s %s' % (f, mb(s)))
        print()

    if heavy:
        print('BIG, BUT ALLOWED  (GitHub will warn)')
        for f, s in heavy:
            print('   %-52s %s' % (f, mb(s)))
        print()

    if total > SITE_SOFT:
        ok = False
        print('SITE IS OVER 1 GB. Pages will still serve it, but you are past the')
        print('size they publish as a limit, and every visitor pays for it in load')
        print('time. Re-encode the largest clips, or move them off to YouTube.')
        print()

    # Which credits actually point at a file, and does that file exist
    idx = os.path.join(HERE, 'index.html')
    if os.path.exists(idx):
        html = open(idx, encoding='utf-8').read()
        m = re.search(r'const WORK=(\[.*?\]);', html, re.S)
        if m:
            try:
                work = json.loads(m.group(1))
            except ValueError:
                work = []
            withclip = [w for w in work if w.get('clip')]
            missing = [w for w in withclip
                       if not os.path.exists(os.path.join(HERE, w['clip']))]
            print('CREDITS         %d of %d have a clip' % (len(withclip), len(work)))
            if missing:
                ok = False
                print('POINTING AT NOTHING  (clip is set, file is not there)')
                for w in missing:
                    print('   %-34s -> %s' % (w.get('t', '?')[:34], w['clip']))
            print()

    reel = os.path.join(MEDIA, 'reel.mp4')
    print('REEL            %s' % (mb(os.path.getsize(reel))
                                  if os.path.exists(reel)
                                  else 'not in place yet (media/reel.mp4)'))

    if vids:
        print()
        print('LARGEST FILES')
        for f, s in vids[:6]:
            print('   %-52s %s' % (f, mb(s)))

    print()
    if ok:
        print('Good to push.')
    else:
        print('Fix the above first. To bring a file down:')
        print('   ffmpeg -i IN.mov -vf scale=-2:720 -c:v libx264 -crf 23 \\')
        print('          -preset slow -c:a aac -b:a 128k -movflags +faststart OUT.mp4')
        print()
        print('-movflags +faststart matters: without it the browser downloads the')
        print('whole file before the first frame appears.')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
