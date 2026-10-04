---
name: The Editorial Ledger
colors:
  surface: '#f8f9ff'
  surface-dim: '#ccdbf4'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d4e4fc'
  on-surface: '#0d1c2e'
  on-surface-variant: '#444748'
  inverse-surface: '#223144'
  inverse-on-surface: '#eaf1ff'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1c1b1b'
  on-primary-container: '#858383'
  inverse-primary: '#c8c6c5'
  secondary: '#9d4400'
  on-secondary: '#ffffff'
  secondary-container: '#fd7b28'
  on-secondary-container: '#5f2600'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#001d33'
  on-tertiary-container: '#3289cb'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#ffdbca'
  secondary-fixed-dim: '#ffb690'
  on-secondary-fixed: '#331100'
  on-secondary-fixed-variant: '#783200'
  tertiary-fixed: '#cee5ff'
  tertiary-fixed-dim: '#97cbff'
  on-tertiary-fixed: '#001d33'
  on-tertiary-fixed-variant: '#004a76'
  background: '#f8f9ff'
  on-background: '#0d1c2e'
  surface-variant: '#d4e4fc'
typography:
  display-xl:
    fontFamily: Playfair Display
    fontSize: 56px
    fontWeight: '700'
    lineHeight: 64px
    letterSpacing: -0.02em
  display-xl-mobile:
    fontFamily: Playfair Display
    fontSize: 38px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 40px
    fontWeight: '600'
    lineHeight: 48px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 30px
    fontWeight: '600'
    lineHeight: 36px
    letterSpacing: 0em
  headline-md:
    fontFamily: Playfair Display
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
  headline-sm:
    fontFamily: Playfair Display
    fontSize: 22px
    fontWeight: '600'
    lineHeight: 28px
  stat-metric:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 52px
  stat-metric-mobile:
    fontFamily: Playfair Display
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 40px
  body-lead:
    fontFamily: Nunito Sans
    fontSize: 20px
    fontWeight: '400'
    lineHeight: 32px
  body-md:
    fontFamily: Nunito Sans
    fontSize: 17px
    fontWeight: '400'
    lineHeight: 28px
  body-sm:
    fontFamily: Nunito Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
  caption:
    fontFamily: Nunito Sans
    fontSize: 13px
    fontWeight: '600'
    lineHeight: 18px
    letterSpacing: 0.02em
  label-uppercase:
    fontFamily: Nunito Sans
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.08em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-mobile: 1rem
  margin: 3rem
  margin-mobile: 1.25rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
  space-2xl: 4rem
---

## Brand & Style

This design system embodies the intellectual rigor, analytical clarity, and visual gravitas of contemporary data-driven journalism. It addresses an audience of informed readers, researchers, policymakers, and civic-minded citizens who demand uncompromised factual fidelity and narrative elegance. 

The aesthetic is grounded in **Editorial Modernism**: a high-contrast union of classical newspaper publishing traditions and sharp, digital-first data visualization. The canvas remains an uncompromising, pristine white, allowing typography and multi-hued categorical data streams to function as the primary visual architecture. Interaction models are tuned for long-form vertical scrollytelling, narrative progression, and exploratory visual analytics without sensory overload. Every visual element communicates intent, authority, and impartiality.

## Colors

The palette is engineered around categorical accessibility and absolute clarity. Backgrounds remain pure white (`#FFFFFF`) to mimic bleached archival newsprint, anchored by rich ink black (`#111111`) for deep contrast and legibility.

Data visualizations strictly employ the **Okabe-Ito barrier-free palette**, ensuring distinct perceptual separation across all forms of color-vision deficiency:
- **Vermilion / Red-Orange**: `#D55E00` (Key contrast, alerts, focal series)
- **Sky Blue**: `#56B4E9` (Comparative baseline series, soft accents)
- **Bluish Green**: `#009E73` (Positive delta, growth metrics, environmental series)
- **Yellow**: `#F0E442` (Contextual highlight, caution markers)
- **Blue**: `#0072B2` (Primary categorical data, standard interactive links)
- **Orange**: `#E69F00` (Secondary categorical data, alternate trend lines)
- **Reddish Purple**: `#CC79A7` (Special category indicators, outliers)

Neutral tones preserve reading ergonomics:
- **Paper Light**: `#F8FAFC` (Card fills, table alternating stripes)
- **Rule / Hairline**: `#E2E8F0` (Delicate dividers, axis guides)
- **Slate Ink**: `#718096` (Annotations, axis tick labels, citation copy)

## Typography

The typographic hierarchy establishes tension between the historic editorial voice of Playfair Display and the clean, utilitarian legibility of Nunito Sans.

- **Playfair Display**: Reserved for major article headlines, section entries, pull quotes, and oversized quantitative callouts (`stat-metric`). Its high-contrast serifs evoke authoritative broadsheet heritage.
- **Nunito Sans**: Used for sustained narrative text, data table content, chart labels, UI controls, and annotations. The generous x-height and open apertures maintain high clarity at complex data densities and smaller screen dimensions.
- **All Caps Micro-Labels (`label-uppercase`)**: Applied to chart axes categories, kicker tags above headlines, and metadata stamps to establish structure without weight.

## Layout & Spacing

The layout uses an asymmetrical 12-column grid structured for editorial reading and scrollytelling:

- **Desktop (1280px+)**: The core narrative column spans 7 central columns (max 680px for optimal reading length of 65–75 characters per line). Interactive charts and comparison graphics extend out into the right 5 columns or span a full 12-column breakout canvas (1140px max) for high-density infographics.
- **Scrollytelling Staging**: The left 5 columns house pinned narrative text blocks that trigger dynamic step states in sticky visual graphics occupying the right 7 columns.
- **Tablet (768px – 1023px)**: Reflows to an 8-column grid with `1.5rem` gutters. Data visualizations sit inline between narrative blocks instead of side-by-side.
- **Mobile (< 768px)**: 4-column layout with `1rem` gutters and `1.25rem` screen margins. Full breakout components stretch edge-to-edge with negative margin bleed, ensuring chart touch points remain accessible.

## Elevation & Depth

This design system avoids skeuomorphic shadows and blur-heavy drop surfaces. Depth is established through structural editorial layering:

- **Flat Spatial Plane**: The background canvas remains flat white (`#FFFFFF`). Elements sit directly on the baseline page plane.
- **Hairline Rules**: Visual separation uses 1px solid dividers in `#E2E8F0` or `#111111` for heavy section breaks.
- **Tonal Substrates**: Embedded data callouts, interactive chart canvases, and sidebars utilize a light neutral fill of `#F8FAFC` bounded by a 1px border of `#E2E8F0`.
- **Dynamic Scrollytelling Focus**: Non-active narrative stages dim slightly (opacity `0.35`) while the active trigger retains full opacity (`1.0`), guiding reader focus downward without shifting spatial height.
- **Tooltips & Popovers**: Floating data inspect tokens utilize a crisp `#111111` fill with white text, no blur, and a subtle 2px solid offset in `#E2E8F0` to stand out against high-density charts.

## Shapes

The shape system is deliberate and reserved, using soft `0.25rem` corners for structured components and fully rounded pill shapes strictly for interactive data filters and tag toggles.

- **Data Cards & Containers**: `0.25rem` radius (`rounded-sm`), preserving a crisp, newspaper-block silhouette.
- **Charts & Frames**: `0px` radius on graph canvases, anchoring visual data to rigid horizontal and vertical axes.
- **Interactive Pills & Filter Tokens**: Full circular radius (`9999px`), distinguishing interactive inputs from static charts and content containers.

## Components

### Buttons & Interactive Filter Pills
- **Filter Pills**: Interactive chart parameters are toggled via pill buttons. Unselected state: `#FFFFFF` fill, 1px border in `#E2E8F0`, text in `#718096`. Active state: `#111111` background, `#FFFFFF` text, 1px border in `#111111`. Hover state: `#F8FAFC` background with `#111111` text.
- **Action Buttons**: Minimalist editorial style. Primary buttons use a solid ink fill (`#111111`), white text, and `0.25rem` corners. Secondary buttons use transparent backgrounds with an underlined ink label.

### Data Cards & Metric Callouts
- Contained within `#F8FAFC` backgrounds with a 1px `#E2E8F0` top border.
- Cards lead with an uppercase kicker in `label-uppercase` (`#718096`), followed by a large numeric value in `stat-metric` (`Playfair Display`, `#111111`), concluding with contextual delta text styled in the corresponding Okabe-Ito tone (e.g., `#009E73` for positive variance).

### Interactive Charts
- **Axes & Grids**: Gridlines are single-pixel dotted rules in `#E2E8F0`. Axis labels use `Nunito Sans` 12px at `#718096`.
- **Series Lines & Points**: Categorical series use Okabe-Ito colors with minimum 2.5px stroke width for visual distinction. Focused points display an active 6px circle with a 2px white halo ring.
- **Hover Inspection Tooltips**: Monolithic `#111111` container, 4px border-radius, pure white micro-copy (`12px/16px`), displaying exact coordinate values and category markers.

### Input Fields & Search Bars
- Understated rectangular inputs with a `#FFFFFF` fill and a distinct bottom-only or fully enclosed 1px `#E2E8F0` border.
- On focus: 1px outline in `#111111` with no offset or glow. Placeholder text is rendered in `#718096`.

### Checkboxes & Radio Buttons
- Precise, compact 16px controls. Checked states fill with `#111111` accompanied by high-contrast white checkmarks or center pips.

### Lists & Tables
- **Data Tables**: Stripeless white canvas by default; hover rows highlight in `#F8FAFC`. Columns separate via generous horizontal spacing rather than vertical lines. Bottom borders on header cells use a 1.5px solid `#111111` rule.
- **Narrative Lists**: Unordered items use small square bullet points in `#D55E00`. Ordered items use bold Playfair numerals in `#111111`.

### Citation Footnotes & Methodology Blocks
- Positioned at the conclusion of analyses with a top 1px solid rule in `#111111`.
- Set in `Nunito Sans` 13px (`#718096`), featuring external source links underlined in `#0072B2`.