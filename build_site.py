#!/usr/bin/env python3
"""Build the App Publishing Academy swipe site.

Captured 1 Aug 2026. The whole funnel was walked as the research identity and the
entire 2h05m webinar pulled down, so everything below is read off the recording
rather than inferred from the landing page.

Run: python3 build_site.py
"""
import sys, os, glob, subprocess
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/Swipes/APP_PUBLISHING_Swipe")


def _probe(p):
    try:
        return int(float(subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", p], capture_output=True, text=True, timeout=60).stdout.strip()))
    except Exception:
        return 0


def video_library():
    rows = []
    for p in sorted(glob.glob(os.path.join(PKG, "Recording/*.mp4"))):
        mb = os.path.getsize(p) / 1e6
        rows.append((os.path.basename(p), _probe(p),
                     f"{mb/1000:.1f} GB" if mb >= 1000 else f"{mb:.0f} MB",
                     "The full workshop, pulled straight from the Vimeo file the "
                     "&ldquo;live&rdquo; room plays. 1080p, complete, including the close."))
    return rows


CONFIG = {
    "SITE": "App Publishing Academy — AI App Publishing",
    "CREATOR": "David (App Publishing Academy)",
    "ADS_KEY": "app_publishing",
    "FUNNEL_IDS": [],
    "CAPTURED": "1 August 2026",
    "REPO": REPO,
    "PACKAGE": "~/Downloads/Swipes/APP_PUBLISHING_Swipe",
    "BLURB": "A webinar that is not live, selling Apple App Store income at "
             "<b>$997</b> against a $6,000 anchor. No call, no application — the "
             "pitch goes straight to a checkout. <b>2h 05m captured in full.</b>",

    "PAGES": [
        ("index.html", "Overview"),
        ("analysis.html", "Analysis"),
        ("transcripts.html", "Transcript"),
        ("videos.html", "Video library"),
    ],

    "STATS": [
        ("Price", "$997"),
        ("Anchor", "$6,000"),
        ("Discount claimed", "$5,000 off"),
        ("Scarcity", "33 spots"),
        ("Captured", "2h 05m"),
        ("Words", "25,785"),
        ("Slides", "716"),
        ("Live?", "No"),
    ],

    "OFFER": [
        ("Product", "AI App Publishing — publish Apple App Store apps without code"),
        ("Front end", "Free 2-hour &ldquo;workshop&rdquo;, run as a fake-live WebinarJam"),
        ("Price", "<b>$997</b> one time"),
        ("Anchor", "&ldquo;normally costs $6,000&rdquo; &mdash; framed as $5,000 off"),
        ("Scarcity", "&ldquo;only 33 spots available today&rdquo;, and a second tier for the "
                     "<i>first 10</i>"),
        ("Checkout", "joinaiapp.com — the button appears on screen mid-pitch"),
        ("Upsell", "A done-for-you option shown on the order page to the first 10 only"),
        ("The call", "Not a sales call. A team member helps <i>process the payment</i> — "
                     "explicitly for splitting the $997 across two cards"),
        ("Risk reversal", "&ldquo;my team take on all of the risk and essentially guarantee "
                          "your success&rdquo;"),
        ("Company", "Accelerator Next Gen Information Technology Consultants EST, Dubai "
                    "(trade licence 1586544)"),
    ],

    "FINDINGS": [
        ("The webinar is not live, and we proved it",
         "The WebinarJam room plays a <b>Vimeo progressive MP4</b> (id 1204801381). The "
         "attendee counter read <b>401</b> and the clock was running, both fabricated. "
         "Because it is a plain file, the entire 2h05m was downloadable in one go — no "
         "screen recording, no waiting for a session."),
        ("They sell at $997 with no call and no application",
         "Every other funnel in this file routes to a booked call or an application. This "
         "one puts a button on screen mid-pitch and sends the buyer to a checkout. The only "
         "human contact offered is <i>after</i> the decision, to help split the payment "
         "across two cards."),
        ("A paid ad that targets no-shows",
         "They run a retargeting ad at people who registered and did not attend: "
         "<i>&ldquo;I noticed you registered for my training but didn't actually make it. No "
         "judgment. Life is busy.&rdquo;</i> They spend money on the exact leak we have, and "
         "point it at an encore page."),
        ("The phone number is asked for second, not first",
         "The opt-in takes name and email, and only reveals the phone field <b>after</b> that "
         "first submit. The visitor is already committed before the highest-friction field "
         "appears. Cheap to test against our own reg page."),
        ("The bonus is gated on staying to the end",
         "The bonus vault is delivered by instructions given live, late in the session. "
         "Attendance is not the goal — <i>completion</i> is."),
        ("A published minute-by-minute agenda",
         "The waiting room breaks the first ten minutes into 00:00-04:00, 04:00-07:00 and "
         "07:00-10:00, and warns that joining late means being lost. Manufactured punctuality "
         "for a session that is a recording anyway."),
    ],

    "FUNNEL": [
        ("Opt-in", "apppublishing.ai/clean",
         "Name and email, then the phone field appears <b>after</b> submitting."),
        ("Waiting room", "apppublishing.ai/waiting-room",
         "Minute-by-minute agenda, bonus vault teased, single CTA into the room."),
        ("The room", "event.webinarjam.com — webinar_id 55",
         '<span class="tag bad">fake live</span> Plays Vimeo MP4 1204801381. '
         'Fabricated 401-attendee counter.'),
        ("Checkout", "joinaiapp.com",
         "$997, revealed on screen during the pitch. Never submitted."),
        ("No-show encore", "apppublishing.ai/webinar-other-times",
         "Paid retargeting ad drives non-attendees here."),
    ],

    "TRANSCRIPT_GROUPS": [
        ("The workshop — 2h 05m, 25,785 words",
         sorted(glob.glob(os.path.join(PKG, "Transcript/*.md")))),
    ],

    "SLIDE_PAGES": [],
    "VIDEOS": video_library(),

    "DECKS": [
        ("The workshop deck (2h05m)", 716,
         "https://docs.google.com/presentation/d/1q61ePLUtExoiOld4HkLqgvOVI_85lmPWbFXuW6iUVW0/edit"),
    ],

    "ANALYSIS": """
<div class="note"><b>Why this one is worth reading even though the offer is nothing like ours.</b>
It is the cleanest example in the file of a <i>direct-sale</i> webinar — no call, no
application, no gatekeeping. Everything is engineered to get a card out during the session.
The mechanics transfer even though the product does not.</div>

<h2 class="sec">How the close works</h2>
<div class="tablewrap"><table>
<tr><th>Beat</th><th>What he does</th></tr>
<tr><td>Anchor</td><td>&ldquo;normally costs $6,000&rdquo;</td></tr>
<tr><td>Price</td><td><b>$997</b>, framed as $5,000 off</td></tr>
<tr><td>Scarcity</td><td>&ldquo;only 33 spots available today&rdquo;</td></tr>
<tr><td>Second tier</td><td>a done-for-you option, <i>first 10 only</i>, revealed on the order page</td></tr>
<tr><td>Friction removal</td><td>a team member will help split the payment across two cards</td></tr>
<tr><td>Enforcement</td><td>book after the spots fill and &ldquo;we're just going to cancel&rdquo;</td></tr>
</table></div>
<p style="margin-top:12px">The order page reveals the second tier only <i>after</i> the buyer
has arrived — the upsell is never mentioned while they are still deciding whether to click.</p>

<h2 class="sec">What we should actually take</h2>
<div class="grid g2">
<div class="card"><h3>Ask for the phone number second</h3><p>Name and email first, phone only
after that submit. The visitor is committed before the field they resist most appears. This is
a one-line change to our reg page and a real test.</p></div>
<div class="card"><h3>Pay to bring back no-shows</h3><p>They run ads at people who registered
and did not attend, with copy that forgives them for it. We treat a no-show as lost. They treat
it as a warm audience they already paid for.</p></div>
<div class="card"><h3>Gate the bonus on finishing</h3><p>Instructions given live and late. It
converts &ldquo;show up&rdquo; into &ldquo;stay to the end&rdquo;, which is the metric that
actually precedes a close.</p></div>
<div class="card"><h3>Remove the payment obstacle out loud</h3><p>Offering to split the cost
across two cards, on the webinar, names the real reason people stall at a checkout. Nobody has
to admit it privately.</p></div>
</div>

<h2 class="sec">Read carefully</h2>
<p>The transcript is machine-made and prices lose their separators — <b>$997</b> can appear as
&ldquo;997&rdquo; and the $6,000 anchor as &ldquo;6,000&rdquo; or &ldquo;6000&rdquo;. The
figures above were read back against the recording. The $500 that appears 42 times is not the
price; it is used throughout the teaching section as an example of per-app revenue.</p>

<p>One more caution: the company is registered in <b>Dubai</b>, and the presenter is credited
only as &ldquo;David&rdquo;. There is no surname anywhere in the funnel or the webinar.</p>
""",
}

if __name__ == "__main__":
    build(CONFIG)
