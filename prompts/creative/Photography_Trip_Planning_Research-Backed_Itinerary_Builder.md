# Photography Trip Planning — Research-Backed Itinerary Builder

**Category:** creative, productivity
**Source:** github:f/awesome-chatgpt-prompts#csv
**Repo Stars:** ⭐ 100,000

---

## Prompt

# Photography Trip Planning Prompt
## Reusable Template for Travel Photographers
### v1.0

---

> **Two ways to use this template:**
>
> **Lightweight mode** — Skip all sections marked `${optional}` and the entire Technical Notes section. Fill in your style profile and trip details, then ask Claude for a text-based research brief and day-by-day schedule. No scripting required.
>
> **Full production mode** — Use every section. Claude will produce a PowerPoint slide deck (via Node.js + pptxgenjs), an Excel workbook (via Python + openpyxl), and Google Maps CSVs — all color-coded and QA'd. Requires comfort running scripts from the command line.
>
> In both modes: fill in every section marked `${fill_in}`. Sections marked `${example}` show what a completed entry looks like — replace them with your own details. Sections marked `${optional}` can be removed if not relevant to your workflow.

---

## WHO I AM

I am a travel photographer planning a trip [with / without] a companion. My name is ${fill_in}. I shoot with [FILL IN — e.g., Canon EOS R5 and Sony A7IV]. My lens kit for travel: [FILL IN — e.g., 16-35mm wide, 24-70mm standard, 100mm macro]. I travel with [FILL IN — e.g., a carbon fiber travel tripod / no tripod / a compact gorilla-pod]. My travel bag is [FILL IN — e.g., Peak Design Travel Backpack 45L with camera cube insert].

---

## MY PHOTOGRAPHIC STYLE

This is the most important section. Read it carefully before suggesting any locations.

**The core subject:** [FILL IN — Describe the through-line of your work. What do you photograph and why? What draws you to a subject?]

> ${example}: I photograph things that endure — structures, landscapes, and moments that exist outside of time. The through-line across my work is things built or lived in that now outlive their original purpose, still standing.

**Technical signatures:** [FILL IN — List your consistent compositional and technical choices.]

> ${example}:
> - Symmetrical or near-symmetrical composition with a strong central vanishing point
> - Low angle or looking straight up to exaggerate scale and eliminate horizon
> - A single human figure used for scale, not as the primary subject
> - Long exposure or slow shutter to pull motion out of water, clouds, and crowds
> - B&W for structural and decay subjects; color when the palette itself is the subject
> - Strong tonal contrast — I print dark
> - The underside, interior skeleton, and structural bones of things interest me more than facades

**Recurring subject categories:** [FILL IN — List the types of places and subjects you consistently seek out.]

> ${example}:
> - Decay and abandonment — things that have outlived their purpose
> - Sacred spaces with weight and edge — not pretty churches, spaces where something happened
> - Old-meets-industrial juxtapositions
> - Underground and subterranean spaces — crypts, tunnels, ancient layers beneath modern cities
> - Geometric structural form — bridges, piers, arches, repeating elements
> - Quiet and empty streets — I shoot before crowds arrive
> - Atlas Obscura-type locations — the unusual, the hidden, the forgotten

**What I consistently avoid:** [FILL IN — List what you do not want recommended.]

> ${example}:
> - Postcard framing of famous places
> - Posed subjects
> - Soft or sentimental light
> - Crowded tourist spots as primary targets
> - Markets as planned stops (open to stumbling upon them)

---

## TRAVEL COMPANION ${optional}

**${fill_in_or_delete_this_section}** — If you are traveling with a companion, describe their interests here so Claude can build a plan that works for both of you, not a photographer's itinerary with someone along for the ride.

> ${example}: My wife travels with me. She enjoys boutique shopping (not chains or department stores), aperitivo culture, neighborhood wandering in places that feel local, and unusual cultural experiences including ossuaries and catacombs. She is game for off-the-beaten-path locations. Build shared experiences into the plan — she is not a separate itinerary to manage.

---

## THE TRIP

**Destination:** [FILL IN — e.g., "Portugal: Lisbon, Porto, Sintra"]
**Departure:** [FILL IN — e.g., "LAX, Sept 16, 3:05 PM"]
**Return:** [FILL IN — e.g., "LHR, Sept 28, 9:50 AM"]
**Outbound arrival:** [FILL IN — e.g., "LIS (Lisbon), Sept 17, 8:30 AM"]
**Cities and nights:** [FILL IN — e.g., "Lisbon 4 nights, Porto 3 nights, Sintra day trip"]
**City-to-city transport:** [FILL IN — e.g., "Train, Lisbon to Porto ~3 hrs"]
**Base neighborhoods:** [FILL IN, or ask Claude to recommend based on your shooting targets and companion interests]

---

## WHAT I WANT CLAUDE TO BUILD

### 1. PowerPoint Slide Deck [OPTIONAL — requires Node.js and pptxgenjs]

> This deliverable is for users comfortable running Node.js scripts. If you want a simpler output, replace this section with a request for a formatted document or PDF.

**Format:** LAYOUT_WIDE (13.3 x 7.5 inches), built with pptxgenjs in Node.js. Dark header bar on content slides with accent color labels. Section divider slides are full dark background. Version number on cover and filename.

**Badges in slide header:**
- Red badge: "★ ADVANCE BOOKING REQUIRED" — for locations requiring pre-purchase tickets
- Green badge: "★ ATLAS OBSCURA" — for unusual/hidden locations in that spirit
- Gold banner: "SHARED EXPERIENCE — not a primary photography target" — for meaningful shared visits

**Slides to include:**
- Cover (trip title, cities, dates, version number)
- Itinerary overview table (date, verified day of week, event, notes)
- Light timing table per city (blue hour start, golden hour start, sunrise, sunset, golden hour end, blue hour end — calculated with Python astral library, exact coordinates, actual trip dates)
- For each city:
  - City section divider
  - Base camp slide (why this neighborhood, proximity to shooting targets, highlights nearby, transit)
  - Location slides for each confirmed shooting target (about, key notes, shot list, unconventional perspectives)
  - Shared experience slides for meaningful non-photography visits
  - High viewpoints slide (card layout, 3 viewpoints, flag confirmed closures)
  - Daily schedule slide(s) — split across multiple slides if more than 14 rows; color-coded by category
  - Optional day trips slide (card layout, flag Atlas Obscura picks)
- Tickets and booking slide (3 columns: book in advance / pay on day / free)
- Gear list slide
- Aperitivo/food bars slide — specific named venues by city, local picks only, with address and description [OPTIONAL — remove if not relevant to your destination]
- Shared activities slide (one column per city) ${optional}

**Schedule color coding:**
- Pre-Dawn Shoot: dark blue / light blue text
- Aperitivo/Food: dark purple / light purple text
- Shared Activity/Food/Shopping: dark gold / light gold text
- Free Roam/Optional: dark green / light green text
- Train Travel/Flight: dark gray / light gray text
- Rest/Breakfast/Checkout: medium gray
- Advance Booking Required: dark red / light red text

---

### 2. Excel Workbook [OPTIONAL — requires Python and openpyxl]

> This deliverable is for users comfortable running Python scripts.

5 tabs: MASTER (full trip chronologically including travel days), one tab per city, LEGEND.
Columns: Date, Day, City, Time, Activity, Category, Duration, Notes.
Same color coding as schedule slides. Freeze panes at A2, hide gridlines, auto-filter on headers.

---

### 3. Google Maps CSVs — one per city ${optional}

Columns: Name, Description, Category, Best Time, Latitude, Longitude, Address.

**Critical:** Use Python csv.writer with utf-8 encoding. No special characters — plain ASCII only. Verify coordinates before including.

Categories: Shooting Location, Shared Activity, Base, High Viewpoint, Transit, Optional Day Trip, CLOSED - DO NOT USE, Atlas Obscura Optional.

**File naming convention:** ${destination}-trip-${year}-v[N].pptx / .xlsx / city-locations.csv. Increment version number on each rebuild.

---

## LOCATION RESEARCH STANDARDS

### For each shooting location, provide:
1. **Description** — what it is, why it matters photographically, best conditions, connection to my style profile where relevant
2. **Shot list** — 4–5 standard shots worth getting
3. **Unconventional perspectives** — 3–4 angles or approaches most photographers miss, matched to my style profile above
4. **Key notes** — hours, access, cost, transit, proximity to other targets
5. **Best time** — pre-dawn / early morning / morning / afternoon / golden hour

### For each city, also research:
- The best base neighborhood (balancing proximity to shooting targets and companion interests)
- High viewpoints (highest publicly accessible, with elevation and cost; confirm current status)
- Optional day trips (3–4 options matched to both my aesthetic and companion interests)
- Atlas Obscura locations that genuinely fit my style — filter carefully, not everything qualifies
- Specific local food/drink venues: local picks only, not tourist-facing, with name, address, and what makes them worth going to

### Research and verification requirements:
- **Verify all locations exist** before including — web search any location you are not certain about
- **Confirm current access status** — search for closures before recommending any viewpoint or attraction
- **Days of week:** always calculate with Python datetime for the actual trip year. Never guess.
- **Light timing:** always calculate with Python astral library using exact city coordinates and trip dates. Never estimate.
- **Ticket prices and booking windows:** search for current prices — do not rely on training data
- **Do not hallucinate** — if uncertain about a fact, search or say so

---

## ATLAS OBSCURA APPROACH

Filter Atlas Obscura picks strictly against your style profile above. Use these as a guide for what typically works and what doesn't:

**Strong fits for unusual/hidden locations:**
- Underground or subterranean spaces (crypts, tunnels, ancient layers)
- Abandoned or decaying spaces (former institutions, industrial ruins)
- Bone chapels and ossuaries
- Hidden architectural anomalies
- Sacred spaces that have crossed into the uncanny

**Weak fits — generally avoid:**
- Quirky museums without strong visual potential
- Locations that are historically interesting but not photographically compelling
- Anything requiring illegal access — note if access is uncertain and flag for research

---

## PLANNING PROCESS

Follow this order:

1. Ask for trip dates, cities, and transport if not provided
2. Verify days of week with Python before doing anything else
3. Calculate light timing with Python astral for all shooting days
4. Research and propose shooting locations — filter against my style profile — ask to confirm before building
5. Research and propose base neighborhoods per city — ask to confirm
6. Research Atlas Obscura picks per city — propose with honest assessment of fit
7. Research specific local food/drink venues per city
8. Identify advance booking requirements and booking windows
9. Build the schedule — pre-dawn shoots, shared experiences, meals, free time
10. Build all deliverables in one go: PowerPoint, Excel, CSVs
11. QA slides before delivering: convert to PDF via soffice, then pdftoppm -jpeg -r 120, review per-slide images

**Batch changes, then rebuild.** Confirm all changes before touching any files. Avoid incremental rebuilds.

---

## TECHNICAL NOTES [OPTIONAL — relevant only if using the PowerPoint, Excel, or CSV deliverables]

### pptxgenjs:
- Never pass a lambda as a positional y argument to helper functions — use inline `s.addText()` with explicit coordinates
- Always add `valign: "top"` to bulleted list text boxes
- Every bullet array's last item must include `options: { bullet: true }` explicitly
- Never use `#` in hex color values — pass without the hash
- QA every rebuild: `soffice --headless --convert-to pdf`, then `pdftoppm -jpeg -r 120`, review before delivering

### openpyxl:
- Use `PatternFill("solid")` for all cell fills
- Freeze panes at A2 on all data sheets
- Set `showGridLines = False` on all sheets
- Auto-filter on header rows

### CSVs:
- Always use Python `csv.writer` with utf-8 encoding
- No special characters — plain ASCII only
- Verify coordinates are accurate before including

### Schedule splits:
- Split any city schedule across multiple slides if more than 14 data rows

---

## STYLE PREFERENCES

[FILL IN — describe your general planning philosophy. Examples below.]

> ${example}:
> - Quality over quantity — fewer, richer locations beat comprehensive lists
> - Minimal logistics friction — don't route across a city when targets can be clustered
> - Authentic over tourist-facing — if a less-visited equivalent exists, recommend it
> - Pre-dawn access is a priority
> - The unusual over the famous — Atlas Obscura sensibility throughout
> - When in doubt about a fact, search before answering

---

*Template adapted from a working Italy trip planning workflow. Built for travel photographers who want a research-backed, production-ready trip plan — not a listicle.*

---

*Collected by Prompt Skills Scraper · Quality verified via GitHub stars ⭐100,000*