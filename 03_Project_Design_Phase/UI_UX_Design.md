# UI / UX Design Specification

## 1. Visual Design Philosophy & Aesthetics
PocketSmart AI features a tailored, high-contrast **Dark Mode** user interface crafted to evoke a modern, financial-tech aesthetic. The visual hierarchy utilizes deep slate foundations, luminous gradient accents, frosted glassmorphism overlays, and crisp typography.

---

## 2. Color System & Design Tokens

| Token Name | Hex Value | Usage |
|---|---|---|
| `--bg-primary` | `#0f172a` | Deep slate canvas background |
| `--bg-secondary` | `#1e293b` | Elevated cards, container backgrounds |
| `--bg-card` | `rgba(30, 41, 59, 0.75)` | Glassmorphism card fill with backdrop blur |
| `--border-color` | `rgba(255, 255, 255, 0.1)` | Subtle structural separators |
| `--text-primary` | `#f8fafc` | Main headings, primary values |
| `--text-secondary` | `#94a3b8` | Subtitles, helper text, form labels |
| `--accent-indigo` | `#6366f1` | Primary call-to-action buttons, active states |
| `--accent-purple` | `#a855f7` | Gradient endpoints, jewelry highlights |
| `--accent-cyan` | `#06b6d4` | Home planning badges, progress bars |
| `--accent-amber` | `#f59e0b` | Party planning badges, warning notes |
| `--accent-emerald` | `#10b981` | Budget balance indicators, success states |

---

## 3. Typography
- **Primary Typeface**: Modern sans-serif stack (`system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`).
- **Heading 1 (`h1`)**: 2.25rem (36px), font-weight 700, letter-spacing -0.025em.
- **Heading 2 (`h2`)**: 1.5rem (24px), font-weight 600.
- **Body Text**: 0.95rem (15px), line-height 1.6, color `#94a3b8`.
- **Numbers / Currencies**: Monospaced tabular numerals for financial alignment.

---

## 4. Key Component Designs

### 4.1 Navigation Bar (`header`)
- Fixed top positioning with backdrop-filter blur (`12px`).
- Brand logo with gradient icon badge.
- Navigation links with hover underlines and active tab indicators.
- User profile chip with username and one-click logout button.

### 4.2 Planner Input Cards
- Responsive grid containers (2-column on desktop, 1-column on mobile).
- Input groups with integrated FontAwesome icons.
- Instant feedback validation on numeric ranges.
- Drag-and-drop file upload target with live image preview (Jewelry Planner).

### 4.3 Budget Calculation Tables
- High-contrast financial table with alternating subtle row fills.
- Proportional percentage badges (`15%`, `20%`, `35%`, `40%`).
- Summary footer highlighting total allocated vs. remaining contingency funds.

### 4.4 Vendor Shopping Buttons
- Color-branded platform pills:
  - **Amazon**: Warm Amber badge with shopping cart icon.
  - **Flipkart**: Bright Blue badge with box icon.
  - **IKEA**: Cobalt Blue / Yellow badge.
  - **Swiggy / Zomato**: Vibrant Orange / Red badge.
  - **Tanishq / CaratLane**: Rich Maroon / Emerald badge.

### 4.5 History & Details Modal
- Centered popup modal with smooth backdrop fade-in.
- Tabular cost inspection view with direct copyable links.
