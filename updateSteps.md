# Website Update Process

## Standard Update Workflow

### 1. Review Changes
```bash
git status
git diff
```

### 2. Stage Specific Files
```bash
# For redesign updates:
git add css/General_Setting.css css/index.css index.html
git add CHANGELOG.md html/updates.html

# For new features:
git add <new-file-1> <new-file-2>

# For all tracked changes:
git add -u
```

### 3. Create Commit
```bash
git commit -m "$(cat <<'EOF'
Brief description of changes

- Bullet point 1
- Bullet point 2
- Bullet point 3

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
EOF
)"
```

### 4. Push to Remote
```bash
git push
```

## Redesign Update Steps (March 2026 Pattern)

### CSS Modernization
1. **Update `General_Setting.css`:**
   - Add modern CSS reset with `box-sizing: border-box`
   - Implement responsive design with media queries
   - Add animation keyframes (`fadeIn`, `slideDown`)
   - Update navigation with sticky header and blur effects
   - Improve footer with gradient and hover effects

2. **Update `index.css`:**
   - Convert to Flexbox/Grid layout system
   - Add staggered animations with `animation-delay`
   - Implement modern card design with hover effects
   - Ensure responsive grid (4→2→1 columns)
   - Add utility classes for new features

### HTML Updates
1. **Update `index.html`:**
   - Add responsive meta tags:
     ```html
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <meta name="description" content="...">
     ```
   - Update navigation links
   - Maintain semantic structure
   - Add new sections/modules as needed

2. **Create new pages:**
   - Use template from `html/updates.html`
   - Include consistent header/footer
   - Apply same CSS structure

### Documentation Updates
1. **Update `CHANGELOG.md`:**
   - Add new version header with date
   - Document all changes by category
   - Include technical details and file list

2. **Update `html/updates.html`:**
   - Add new changelog entry
   - Maintain consistent styling
   - Update navigation links

## Testing Checklist

### Responsive Design
- [ ] Test on mobile (< 600px)
- [ ] Test on tablet (600-1150px)
- [ ] Test on desktop (> 1150px)
- [ ] Verify navigation works on all screens
- [ ] Check image scaling and layout

### Browser Compatibility
- [ ] Chrome/Edge (latest)
- [ ] Firefox (latest)
- [ ] Safari (if available)
- [ ] Mobile browsers

### Functionality
- [ ] All links work correctly
- [ ] Forms submit properly (if any)
- [ ] Images load without errors
- [ ] Animations run smoothly
- [ ] No console errors

## Quick Commands Reference

```bash
# Check current status
git status
git log --oneline -5

# Discard local changes
git checkout -- <file>
git restore <file>

# Create new branch for feature
git checkout -b feature/name
git push -u origin feature/name

# Merge changes
git checkout master
git merge feature/name

# Update from remote
git pull origin master
```

## Files to Always Update

1. `CHANGELOG.md` - Document all changes
2. `html/updates.html` - User-facing changelog
3. `index.html` - Main navigation updates
4. Relevant CSS files for styling changes

## Notes
- Always test changes locally before committing
- Use descriptive commit messages
- Keep `Co-Authored-By` line for AI-assisted work
- Push to remote immediately after committing
- Consider creating backups before major changes