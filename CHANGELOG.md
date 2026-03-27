# Website Redesign Changelog

## March 27, 2026 - Dynamic Updates System

### Overview
Implemented a folder-based updates system that stores each update as a separate JSON file in `_data/updates/`. The updates page now automatically loads and displays all updates in reverse chronological order.

### Changes Made
- Created `_data/updates/` folder with JSON schema
- Modified `html/updates.html` to use Jekyll data files and Liquid templates
- Added front matter to enable Jekyll processing
- Created template with responsive design and proper styling
- Updated existing update to JSON format (`2026-03-27.json`)
- Added documentation (`_data/updates/README.md`)

### Technical Details
- Updates are stored as JSON files with date, title, overview, and categorized changes
- Liquid template handles sorting, type mapping, and Markdown rendering
- No need to edit HTML when adding new updates—just add a JSON file
- Maintains existing visual design and responsive layout

### Files Modified
- `html/updates.html` - Added front matter and Liquid template
- `_data/updates/2026-03-27.json` - Converted existing update to JSON
- `_data/updates/README.md` - Documentation
- `CHANGELOG.md` - This entry

### Impact
- Simplified update process: just add a JSON file
- Maintainable and scalable system
- No duplication of HTML code
- Preserves all existing styling and animations

## March 27, 2026 - Major Redesign

### Overview
Complete modernization of the website with improved visual design, responsive layout, and enhanced user experience.

### HTML Changes (`index.html`)

#### Added
- Responsive viewport meta tag: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- Page description meta tag for SEO
- Updated title to "Shen Zhihao - Research Notes"
- Proper HTML attribute syntax for QR Code image (`id="QR_Code"`)

#### Improved
- Removed unnecessary `<br/>` after blog title
- Enhanced semantic structure

### CSS Changes

#### `General_Setting.css` - Complete Redesign

**Reset & Base Styles:**
- Modern CSS reset with `box-sizing: border-box`
- Smooth scrolling: `scroll-behavior: smooth`
- Animation keyframes: `fadeIn` and `slideDown`

**Navigation:**
- Sticky header with blur effect (`backdrop-filter: blur(10px)`)
- Animated underline hover effect using `::after` pseudo-element
- Improved spacing and typography

**Header:**
- Gradient background: `linear-gradient(to right, #2c3e50, #4a6491)`
- Enhanced typography with text shadows and proper spacing
- Added fade-in animation

**Footer:**
- Gradient background matching header
- QR code hover animation with scale effect
- Improved copyright section styling

**Responsive Design:**
- Comprehensive media queries for all screen sizes
- Mobile-optimized navigation and layout

#### `index.css` - Modern Layout System

**Layout:**
- Flexbox/Grid layout replacing legacy float-based system
- Staggered fade-in animations for content
- `display: grid` for article cards with auto-responsive columns

**Sidebar:**
- Modern card design with hover effects
- Smooth transitions for link hover states
- Enhanced typography and spacing

**Article Cards:**
- Modern card design with shadows and rounded corners
- Hover animations: lift effect, image scaling, color change
- Improved image handling with `object-fit: cover`
- Staggered animation delays for visual appeal

**Responsive Grid:**
- Desktop: 4-column grid (min-width: 1150px)
- Tablet: 2-column grid (max-width: 1150px)
- Mobile: 1-column layout (max-width: 600px)

### Visual Enhancements

1. **Modern Aesthetic:**
   - Professional color scheme with gradients
   - Consistent spacing and typography
   - Subtle shadows and animations

2. **Interactive Elements:**
   - Hover effects on all interactive components
   - Smooth transitions (0.3-0.5s duration)
   - Visual feedback for user actions

3. **Animation System:**
   - Staggered fade-in for content
   - Smooth hover transitions
   - Performance-optimized animations

4. **Responsive Design:**
   - Fully adaptive layout
   - Mobile-first approach
   - Touch-friendly interface

### Technical Improvements

1. **Modern CSS Features:**
   - CSS Grid and Flexbox
   - CSS Custom Properties (variables)
   - CSS Animations and Transitions
   - `object-fit` for image handling

2. **Performance:**
   - Hardware-accelerated animations
   - Optimized image rendering
   - Efficient CSS selectors

3. **Accessibility:**
   - Proper semantic HTML structure
   - Sufficient color contrast
   - Keyboard-navigable interface

4. **Maintainability:**
   - Clean, organized code structure
   - Consistent naming conventions
   - Comprehensive comments

### Files Modified
- `index.html` - Main page structure and metadata
- `css/General_Setting.css` - Global styles and layout
- `css/index.css` - Homepage-specific styles

### Next Steps
Consider applying similar modern design patterns to other pages:
- `review.html`
- `My_Research.html`
- `My_Creation.html`
- `Sorting.html`
- `CFD.html`

This redesign establishes a solid foundation for future improvements and ensures the website remains visually appealing and functional across all devices.

## March 27, 2026 - Content Translation to English

### Overview
Translation of all Chinese text on the main page to English for broader accessibility.

### Changes Made
- **Navigation**: Translated "首页" to "The Beginning" and "往期" to "Previous"
- **Header**: Updated blog name to "Hello Guys"
- **Sidebar**: Translated "目 录" to "Contents", "研究" to "Research", "个人创作" to "Personal Creations", "更新日志" to "Update Log"
- **Article Titles**:
  - "几种排序算法图解" → "Several Sorting Algorithms Illustrated"
  - "离散元DEM模拟" → "Discrete Element Method (DEM) Simulation"
  - "流固耦合CFDEM模拟" → "Fluid-Solid Coupling CFDEM Simulation"
  - "计算流体力学CFD模拟" → "Computational Fluid Dynamics (CFD) Simulation"

### Files Modified
- `index.html` - Updated all Chinese text to English equivalents

### Impact
- Improved accessibility for international visitors
- Consistent English interface throughout main page
- Maintained technical accuracy in translated terminology